"""
Конфигурация WSGI для проекта myapp.

Он предоставляет вызываемый WSGI как переменную уровня модуля с именем ``application``.

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

application = get_wsgi_application()
