#!/usr/bin/env python
import os
import sys
from os.path import join, dirname
import warnings

from dotenv import load_dotenv

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            load_dotenv(dotenv_path)
        except Warning:
            pass
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
