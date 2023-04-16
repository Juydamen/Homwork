#ЭТОТ ФАЙЛ НУЖЕН ЧТОБЫ ВЕБСЕРВЕР СМОГ ЗАПУСТИТЬ НАШЕ DJANGO ПРИЛОЖЕНИЕ

"""
WSGI config for prroject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djcd angoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prroject.settings')

application = get_wsgi_application()
