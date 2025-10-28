# -*- coding: utf-8 -*-
"""
This script delegates execution to `imgctl.web.main`.

Note:
    Intended for development use only.
"""

from .web import main as web_main


def main():
    """
    Entrypoint function that calls the main interface from imgctl.web.

    This wrapper allows local development execution by invoking
    the web-based interface directly.
    """
    web_main()


if __name__ == "__main__":
    main()
