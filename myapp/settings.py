"""
Настройки Django для проекта myapp.

Сгенерировано «django-admin startproject» с использованием Django 4.0.4.

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/4.0/topics/settings/

Полный список настроек и их значений см.
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path


# Создавайте пути внутри проекта следующим образом: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки быстрого старта разработки — не подходят для продакшена
# См. https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: держите секретный ключ, используемый в производстве, в секрете!!
SECRET_KEY = 'django-insecure-ht&0_x8vv4r52&ipetvhpz#_+zg(mhcyx)uv2q_iippue8z(p0'

# SECURITY WARNING: не запускайте с включенной отладкой в ​​​​продакшене!
# DEBUG = True - режим разработки, DEBUG = False - режим продакшена
DEBUG = True

ALLOWED_HOSTS = []


# Определение приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'myapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myapp.wsgi.application'


# База данных
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Проверка пароля
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Интернационализация
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp/static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ['127.0.0.1']


# Подключение к smtp

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'django-project1@mail.ru'
EMAIL_HOST_PASSWORD = 'w7aSs1MvtqJWTqxQNgdk'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


# Загрузка файлов пользователями через ckeditor

CKEDITOR_UPLOAD_PATH = 'uploads/'


# Параметры капчи

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # Математические примеры
CAPTCHA_NOISE_FUNCTIONS = None  # Шум
CAPTCHA_LETTER_ROTATION = None  # Наклон символов