# Django

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### venv

1.  Создание виртуального окружения
>python -m venv venv

2.  Активация виртуального окружения
* cmd
>venv\scripts\activate.bat

* PowerShell
>venv\scripts\activate.ps1

3.  Деактивация виртуального окружения
>deactivate

### Django

1.  Загрузка Django
>pip install django

2.  Старт проекта, создание файловой структуры Django
>django-admin startproject myapp

Название не должно совпадать с именем директории, в которой находится проект

3.  Переход в директорию проекта
>cd myapp

4.  Запуск веб-сервера
>python manage.py runserver

5.  Создание нового приложения
>python manage.py startapp blog

* Создание миграций
>python manage.py makemigrations

* Проведение миграций
>python manage.py migrate

* Создание суперпользователя (администратора) и админпанели в текущей базе данных
>python manage.py createsuperuser

* Сбор всей статики в одну директорию, путь к которой лежит в settings.py
>python manage.py collectstatic

##### Django Debug Toolbar  
https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

* Пакет CKEditor (расширение функционала текстового редактора админпанели)
>pip install django-ckeditor

* Капча
>pip install django-simple-captcha

###### Обучающие материалы
[Django полный курс 2021](https://www.youtube.com/playlist?list=PLmC7X4gkQWCeyIdLxHZdts-3tkcrxP4-o)
