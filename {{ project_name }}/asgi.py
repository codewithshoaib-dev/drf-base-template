

import os

from django.core.asgi import get_asgi_application

app_env = os.getenv('APP_ENV', 'dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{{ project_name }}.settings.{app_env}')

application = get_asgi_application()
