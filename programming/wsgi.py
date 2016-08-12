"""
WSGI config for programming project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 실서비스 단계에서는 wsgi부터 시작, 개발환경에서는 manage.py에서 시작
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings.prod")

application = get_wsgi_application()
