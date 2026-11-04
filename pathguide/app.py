"""Gunicorn entry point for the PathGuide Flask application."""

import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = PROJECT_DIR / "Code" / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app import app  # noqa: E402

application = app
