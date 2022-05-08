"""myapp URL Configuration

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app
    2. Добавьте URL-адрес в urlpatterns: path('', views.home, name='home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL-адрес в шаблоны URL-адресов: path('', Home.as_view(), name='home')
Включение другой конфигурации URL
    1. Импортируйте функцию include(): из django.urls import include, path
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
