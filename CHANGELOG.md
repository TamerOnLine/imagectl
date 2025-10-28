# Changelog

All notable changes to this project will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]
### Added
### Changed
### Fixed

---

## [0.1.1] - 2025-10-30
### Fixed
- Fixed issue where circle mask exported JPG without transparency.

### Changed
- Improved image processing speed by 25%.

---

## [0.1.0] - 2025-10-28
### Added
- First public release of **imagectl**.
- Streamlit Web UI for single and batch image processing.
- Resize images by **px** or **cm** (with DPI support).
- Apply **circle** or **ellipse** masks to images with transparency support.
- Smart image compression with automatic quality adjustment to fit size limits.
- Batch range filtering using expressions (e.g., `1,3-5,7-, -4`).
- Auto-index fallback for files without numbers (based on upload order).
- Export processed images as a **ZIP**.

### Changed
- Initial packaging and distribution as `imagectl`.

### Fixed
- N/A (first release)

---
