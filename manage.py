#!/usr/bin/env python
# Useful Commands:

# Create virtual environment
# py -3 -m venv .venv

# Start virtual environment
# .venv\scripts\activate

# Updgrade pip in the env
# python -m pip install --upgrade pip

# Install django in the env
# python -m pip install django

# Create project
# django-admin startproject web_project .

# Start app
# python manage.py startapp <name>

# Set up sqlite
# python manage.py migrate

# Start server
# python manage.py runserver

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
