"""
PathGuide - Launcher
Starts the main application in backend/app.py, so `python app.py`
still works from the Code folder.
"""
import os
import sys
import runpy

BACKEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
sys.path.insert(0, BACKEND_DIR)

runpy.run_path(os.path.join(BACKEND_DIR, 'app.py'), run_name='__main__')
