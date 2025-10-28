# -*- coding: utf-8 -*-
"""
web.py — Streamlit launcher for ImageTool
Usage:
    imagetool-web --port 8600
"""
import os, argparse
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description="Run imagetool web UI")
    p.add_argument("--port", type=int, default=8501)
    args = p.parse_args()
    app = Path(__file__).with_name("app.py").resolve()
    print(f"[info] Starting Streamlit on port {args.port} …")
    print(f"[info] Launching app: {app}")
    os.execvp("streamlit", ["streamlit", "run", str(app), "--server.port", str(args.port)])

if __name__ == "__main__":
    main()
