# -*- coding: utf-8 -*-
from __future__ import annotations
import io, os, re, zipfile
from typing import List, Tuple, Iterable
import streamlit as st
from PIL import Image, ImageDraw

# ---------------- Basic UI ----------------
st.set_page_config(page_title="ImageTool", page_icon="🖼️", layout="centered")
st.title("🖼️ ImageTool — Resize + Mask + Compress (Batch + Ranges)")

st.caption(
    "Upload one or many images → choose dimensions → optional circle/ellipse mask → compress.\n"
    "Supports **range filtering** for numbered filenames (1-based): `5`, `2-6`, `-4`, `7-`, `1,3,6-9,12-`."
)

# ---------------- Helpers ----------------
def cm_to_px(cm: float, dpi: int) -> int:
    return max(1, round((cm * dpi) / 2.54))

_num_re = re.compile(r"(\d+)")
def extract_index(name: str) -> int | None:
    """
    Extract the last number in a filename to use as index.
    e.g. IMG_0012.jpg -> 12 ;  photo-7.png -> 7
    Returns None if no number is found.
    """
    nums = _num_re.findall(name)
    return int(nums[-1]) if nums else None

def parse_range_expr(expr: str, max_n: int) -> List[int]:
    """
    Parse 1-based range expression like: '1,3-5,7-, -4'
    Returns sorted unique indices within [1..max_n].
    """
    if not expr.strip():
        return list(range(1, max_n + 1))

    parts = [p.strip() for p in expr.split(",") if p.strip()]
    selected: set[int] = set()

    def clamp(a: int) -> int:
        return min(max(a, 1), max_n)

    for p in parts:
        if "-" in p:
            start, end = p.split("-", 1)
            if start == "" and end == "":  # "-" (all)
                selected.update(range(1, max_n + 1))
            elif start == "":              # "-b" → 1..b
                b = clamp(int(end))
                selected.update(range(1, b + 1))
            elif end == "":               # "a-" → a..max
                a = clamp(int(start))
                selected.update(range(a, max_n + 1))
            else:                         # "a-b"
                a = clamp(int(start)); b = clamp(int(end))
                if a <= b:
                    selected.update(range(a, b + 1))
                else:
                    selected.update(range(b, a + 1))
        else:
            # single number
            try:
                i = int(p)
                if 1 <= i <= max_n:
                    selected.add(i)
            except ValueError:
                continue

    return sorted(selected)

def process_image(img: Image.Image, w: int, h: int, max_kb: int, shape: str) -> Tuple[bytes, str, int, bool]:
    """
    Resize + optional shape mask + compress to <= max_kb if possible.
    Returns: (bytes, ext, size_kb, ok_within_limit)
    """
    work = img.resize((w, h), Image.LANCZOS)
    has_alpha = False

    if shape in ("circle", "ellipse"):
        mask = Image.new("L", (w, h), 0)
        d = ImageDraw.Draw(mask)
        if shape == "circle":
            s = min(w, h); x0 = (w - s)//2; y0 = (h - s)//2
            d.ellipse([x0, y0, x0 + s, y0 + s], fill=255)
        else:
            d.ellipse([0, 0, w, h], fill=255)
        work = work.convert("RGBA"); work.putalpha(mask); has_alpha = True

    if has_alpha:
        buf = io.BytesIO()
        work.save(buf, format="PNG", optimize=True)
        size_kb = buf.tell() // 1024
        return buf.getvalue(), ".png", size_kb, (size_kb <= max_kb)

    quality = 95
    best = b""; best_kb = 0
    while quality >= 10:
        buf = io.BytesIO()
        work.convert("RGB").save(buf, format="JPEG", quality=quality, optimize=True)
        size_kb = buf.tell() // 1024
        best, best_kb = buf.getvalue(), size_kb
        if size_kb <= max_kb:
            break
        quality -= 5
    return best, ".jpg", best_kb, (best_kb <= max_kb)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("Settings")

    unit = st.selectbox("Unit", ["px", "cm"], index=0)
    if unit == "cm":
        dpi = st.number_input("DPI", min_value=1, value=300, step=50)
        w_val = st.number_input("Width (cm)", min_value=0.1, value=5.0, step=0.1)
        h_val = st.number_input("Height (cm)", min_value=0.1, value=5.0, step=0.1)
    else:
        w_val = st.number_input("Width (px)", min_value=1.0, value=512.0, step=1.0)
        h_val = st.number_input("Height (px)", min_value=1.0, value=512.0, step=1.0)

    lock = st.checkbox("Square 1:1", value=False)
    if lock:
        h_val = w_val

    shape = st.radio("Output shape", ["rectangle","circle","ellipse"], index=0)
    max_kb = st.number_input("Max size (KB)", min_value=1, value=999, step=10)

    st.divider()
    st.subheader("Batch selection (optional)")
    range_expr = st.text_input(
        "Number range (1-based) — e.g. 1,3-5,7-, -4",
        value=""
    )
    fallback_by_order = st.checkbox(
        "If filename has no number, order by upload order and index them 1..N",
        value=True
    )

    run_btn = st.button("Process ✨", use_container_width=True)

# ---------------- Uploader ----------------
files = st.file_uploader(
    "Upload image(s) (JPG/PNG/WebP/BMP)",
    type=["jpg","jpeg","png","webp","bmp"],
    accept_multiple_files=True
)

# preview (first few)
if files:
    st.write(f"**{len(files)} file(s) uploaded**")
    st.image(files[0], caption="Preview (first)", use_container_width=True)

# ---------------- Processing ----------------
if run_btn:
    if not files:
        st.warning("Please upload at least one image.")
        st.stop()

    # Build an index for files:
    # 1) If filename has number → use it
    # 2) Else, if fallback_by_order → use upload order index
    # 3) Else, skip files without numbers
    items: list[tuple[int, str, bytes]] = []  # (index, filename, raw bytes)
    no_number: list[tuple[int, str, bytes]] = []
    for i, f in enumerate(files, start=1):
        name = f.name
        raw = f.getvalue()
        idx = extract_index(name)
        if idx is None:
            if fallback_by_order:
                no_number.append((i, name, raw))  # temp, will reindex later
            else:
                continue
        else:
            items.append((idx, name, raw))

    # If fallback mode → append no-number files with sequential indices after the max index
    if fallback_by_order and no_number:
        start = (max([x[0] for x in items]) if items else 0) + 1
        for j, (orig_i, name, raw) in enumerate(no_number, start=0):
            items.append((start + j, name, raw))

    if not items:
        st.error("No numbered files found (and fallback disabled).")
        st.stop()

    # Sort by index
    items.sort(key=lambda t: t[0])

    # Apply range filter (1-based over the *sorted* list)
    # Here max_n = count of items, indices are remapped to 1..N for range selection
    max_n = len(items)
    chosen_positions = parse_range_expr(range_expr, max_n)
    if not chosen_positions:
        st.warning("Range resulted in an empty selection. Nothing to process.")
        st.stop()

    # Take the chosen items by their position in the sorted sequence (1-based)
    chosen = [items[pos - 1] for pos in chosen_positions]

    # Dimensions
    if unit == "cm":
        W = cm_to_px(float(w_val), int(dpi))
        H = cm_to_px(float(h_val), int(dpi))
        dim_label = f"{w_val}x{h_val}cm@{dpi}dpi"
    else:
        W = int(round(float(w_val)))
        H = int(round(float(h_val)))
        dim_label = f"{W}x{H}px"

    # Process and zip
    zip_buf = io.BytesIO()
    failed = []
    with zipfile.ZipFile(zip_buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for _, name, raw in chosen:
            try:
                img = Image.open(io.BytesIO(raw))
                data, ext, size_kb, ok = process_image(img, W, H, int(max_kb), shape)
                base = os.path.splitext(name)[0]
                out_name = f"{base}_{dim_label}{ext}"
                zf.writestr(out_name, data)
                if not ok:
                    failed.append(out_name)
            except Exception as e:
                failed.append(f"{name} (error: {e})")

    zip_bytes = zip_buf.getvalue()
    st.success(f"Processed {len(chosen)} image(s). ZIP size: {len(zip_bytes)//1024} KB")
    if failed:
        st.info("Some items may exceed size limit or had errors:\n- " + "\n- ".join(failed))

    st.download_button(
        "⬇️ Download ZIP",
        data=zip_bytes,
        file_name=f"imagetool_batch_{dim_label}.zip",
        mime="application/zip",
        use_container_width=True,
    )
