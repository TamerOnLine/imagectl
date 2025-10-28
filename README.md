# 🖼️ ImageTool — Batch Resize, Mask & Compress Images

<p align="center">
  <a href="https://github.com/TamerOnLine/imagetool/stargazers"><img src="https://img.shields.io/github/stars/TamerOnLine/imagetool?style=for-the-badge" /></a>
  <a href="https://github.com/TamerOnLine/imagetool/issues"><img src="https://img.shields.io/github/issues/TamerOnLine/imagetool?style=for-the-badge" /></a>
  <a href="https://github.com/TamerOnLine/imagetool"><img src="https://img.shields.io/github/license/TamerOnLine/imagetool?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Web%20UI-Streamlit-orange?style=for-the-badge" />
</p>

<p align="center">
  <a href="https://pypi.org/project/imagetool/"><img src="https://img.shields.io/pypi/v/imagetool?style=for-the-badge" /></a>
  <a href="https://pypi.org/project/imagetool/"><img src="https://img.shields.io/pypi/pyversions/imagetool?style=for-the-badge" /></a>
  <a href="https://pypi.org/project/imagetool/"><img src="https://img.shields.io/pypi/dm/imagetool?style=for-the-badge" /></a>
</p>

**ImageTool** is a lightweight yet powerful tool for batch image processing.  
Resize, apply circle/ellipse masks, compress, and filter images by filename ranges — all through an intuitive **Streamlit Web UI**.

Ideal for creators, developers, photographers, e-commerce, thumbnails, social media, and bulk image optimization.

---

## ✨ Features

✅ Batch resize images to **px** or **cm @ DPI**  
✅ Apply **circle** or **ellipse** cutout masks  
✅ Target size compression (auto-adjusts JPEG quality)  
✅ Works with JPG, PNG, WebP, BMP  
✅ Smart filename range selection:
```
Examples: 1,3-5,7-, -4, 1,3,6-9,12-
```
✅ Optional auto-indexing for files without numbers  
✅ Export all processed images as a single **ZIP**  
✅ Clean and easy Web UI built with Streamlit  

---

## 🎥 Demo GIF (Placeholder)

> _Insert a short 6–10 sec GIF here demonstrating:_  
✔ Upload images → choose size & mask → download ZIP

**Suggested filename:** `demo.gif`  
**Recommended size:** 900×500

```
[ PLACEHOLDER FOR DEMO GIF ]
```

---

## 🚀 Installation

### Using pip

```bash
pip install imagetool
```

### Using uv (recommended for speed)

```bash
uv pip install imagetool
```

---

## 🧑‍💻 Usage

### Launch the Web UI

```bash
imagetool-web
```

Default port: `8501`

Run on another port:

```bash
imagetool-web --port 8600
```

Then open in your browser:

```
http://localhost:8600
```

---

## 🖥️ Screenshots (Placeholders)

> Add 2–3 images that show the UI

| Upload & Preview | Settings Panel | Download Result |
|------------------|----------------|-----------------|
| *(screenshot 1)* | *(screenshot 2)* | *(screenshot 3)* |

---

## 📦 Project Structure

```
imagetool/
├── src/imagetool/
│   ├── app.py        # Main Streamlit application
│   ├── web.py        # Launcher for the Web UI
│   ├── runner.py     # Dev entrypoint
│   ├── ranges.py     # Range parsing utility
│   └── __init__.py   # Package metadata
├── tools/            # Dev tools (publish, changelog, etc.)
├── pyproject.toml    # Project configuration
└── README.md
```

---

## 🧠 How Range Selection Works

You can filter images based on numeric values in filenames:

| Expression | Meaning |
|------------|----------|
| `5`        | only #5 |
| `2-6`      | 2 to 6 |
| `-4`       | 1 to 4 |
| `7-`       | 7 to end |
| `1,3,6-9,12-` | combine multiple rules |

If a filename has no number, you can auto-index based on upload order.

---

## 🗺️ Roadmap

| Status | Feature |
|--------|----------|
| ✅ | Initial release with batch processing |
| 🔜 | Add CLI batch processing (without UI) |
| 🔜 | Add image watermark removal |
| 🔜 | Add filters (sharpness, contrast, background removal) |
| 🧪 | API mode for developers to integrate in Python apps |

Want to request a feature? → Open an Issue

---

## 🤝 Contributing

Contributions are welcome!  
Please:

1. Open an issue to discuss changes
2. Fork the repo
3. Create a feature branch
4. Submit a pull request

---

## 🪪 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this useful, consider:

✅ ⭐ Starring the repo  
🐞 Creating issues for bugs or suggestions  
📣 Sharing it with others

---

## 📍 Links

- PyPI: https://pypi.org/project/imagetool/
- GitHub: https://github.com/TamerOnLine/imagetool

