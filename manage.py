#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

def main():
    """Run administrative tasks."""
    env = environ.Env()
    environ.Env.read_env()

    app_env = env('APP_ENV', default='dev')

 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{{ project_name }}.settings.{app_env}')
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
