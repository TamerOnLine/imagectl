# 🖼️ imagectl — Batch Resize, Mask & Compress (Web UI)

<p align="center">
  <a href="https://github.com/TamerOnLine/imagectl/stargazers"><img src="https://img.shields.io/github/stars/TamerOnLine/imagectl?style=for-the-badge" /></a>
  <a href="https://github.com/TamerOnLine/imagectl/issues"><img src="https://img.shields.io/github/issues/TamerOnLine/imagectl?style=for-the-badge" /></a>
  <a href="https://github.com/TamerOnLine/imagectl/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TamerOnLine/imagectl?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Web%20UI-Streamlit-orange?style=for-the-badge" />
</p>

**imagectl** is a lightweight and fast batch image processing tool with a clean **Streamlit Web UI**.  
Resize (px or cm with DPI), apply circle/ellipse masks, smart compression to target size, and range‑based selection by filename — then download all results as a single ZIP.

> Perfect for creators, e‑commerce, thumbnails, social media, and bulk optimization.

---

## ✨ Features
- Resize using **px** or **cm @ DPI**
- **Mask:** Circular or elliptical cut‑out (with transparency)
- **Compression:** Auto‑adjusts JPEG quality to reach max KB
- Supported formats: **JPG / PNG / WebP / BMP**
- Smart **range filter** based on numbers in filenames:
  - Examples: `5`, `2-6`, `-4`, `7-`, `1,3,6-9,12-`
- **Auto‑index** option for files without numbers (1..N)
- Export all results as a single **ZIP**

---

## 🚀 Quick Start

> Recommended: use **uv** for fast development, or pip normally.  
> (PyPI install section will be added after publishing)

### Using uv (local dev)
```bash
git clone https://github.com/TamerOnLine/imagectl.git
cd imagectl
uv sync
uv run imagectl --port 8600
```

### Using pip (local dev)
```bash
git clone https://github.com/TamerOnLine/imagectl.git
cd imagectl
pip install -e .
imagectl --port 8600
```

> Default port: 8501. Use `--port 8600` to change.

---

## 🧑‍💻 CLI / Commands

Two console scripts are provided:

- **`imagectl`** → Launch Web UI (Streamlit)
- **`imagectl-web`** → Same as above (explicit Web name)

Examples:
```bash
imagectl
imagectl --port 8600
imagectl-web --port 9000
```

Then open:
```
http://localhost:8501
# or
http://localhost:8600
```

---

## 📥 Usage (inside UI)
1) Upload one or multiple images (JPG/PNG/WebP/BMP)  
2) Choose size: px or cm + DPI  
3) Optional: Circle or Ellipse mask  
4) Set **Max size (KB)** for smart compression  
5) Optional: enter a **Range** to filter which images to process  
   - `5`, `2-6`, `-4`, `7-`, `1,3,6-9,12-`  
6) Click **Process ✨** and download the ZIP

If filenames lack numbers, enable **Auto‑index** to number them by upload order.

---

## 🖼️ Screenshots / Demo (Placeholders)

| Upload & Preview | Settings | Download ZIP |
|---|---|---|
| *(screenshot 1)* | *(screenshot 2)* | *(screenshot 3)* |

Add a short GIF (6–10s) showing: upload → adjust → download.  
Suggested size: 900×500  
Filename: `demo.gif`

---

## 🗺️ Roadmap
- [x] Initial release: resize/mask/compress + ranges
- [ ] CLI batch processing (no UI)
- [ ] Improved PNG & WebP compression
- [ ] Basic filters (sharpness / contrast / bg remove)
- [ ] API mode for integration

---

## 🤝 Contributing
Contributions are welcome!

1. Open an issue
2. Fork the repo
3. Create a feature branch
4. Submit a PR

---

## 🪪 License
MIT — see [LICENSE](./LICENSE)

---

## 🔗 Links
- Repo: https://github.com/TamerOnLine/imagectl
- Issues: https://github.com/TamerOnLine/imagectl/issues

<!-- PyPI badges to add after publishing:
<a href="https://pypi.org/project/imagectl/"><img src="https://img.shields.io/pypi/v/imagectl?style=for-the-badge" /></a>
<a href="https://pypi.org/project/imagectl/"><img src="https://img.shields.io/pypi/pyversions/imagectl?style=for-the-badge" /></a>
<a href="https://pypi.org/project/imagectl/"><img src="https://img.shields.io/pypi/dm/imagectl?style=for-the-badge" /></a>
-->
