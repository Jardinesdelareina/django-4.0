# django-4.0

pip install django  --установка фреймфорка
django-admin startproject myapp  --загрузка файлов, старт проектаб последнее слово - название
Название не должно совпадать с именем директории, в которой находится проект

/myapp
--/myapp          --пакет конфигураций
----__init__.py  --пустой файл, точка входа в проект, по требованиям языка python
----asgi.py      --модуль, связывающий проект с веб-сервером
----settings.py  --модуль с настройками проекта
----urls.py      --модуль с маршрутами проекта
----wsgi.py      --модуль, связывающий проект с веб-сервером
--manage.py      --служит для создания файлов, выполнения команд 
                 (создания миграций, приложений, запуска сервера и тд),
                 вызывает django-admin и передает ей введенную команду

cd myapp  --переход в папку с проектом
python manage.py runserver  --запуск веб-сервера, порт можно назначить приписав число, например 4000
http://127.0.0.1:8000/ и localhost:8000/ один и тот же адрес локального сервера

pyclean .  --очищает проект от кэша (__pycache__)
clear  --очищает терминал PowerShell

python manage.py startapp blog  --создание нового приложения, последнее слово - название

/blog
--/migrations     --папка с миграциями приложения
--__init__.py     --инициализация приложения, определяющая директорию как пакет
--admin.py        --модуль настроек админки
--apps.py         --модуль настроек приложения
--models.py       --модели приложения
--tests.py        --модуль с тестирующими процедурами
--views.py        --контроллеры приложения

Созданное приложение зарегистрировать в settings.py:
blog.apps.BlogConfig

python manage.py makemigrations  --создание миграций** Миграции - "контроль версий" для моделей
python manage.py migrate  --применение миграций
python manage.py createsuperuser  --создание суперюзера (админа)
python manage.py collectstatic --собирает всю статику в один файл, путь указывается в settings.py

Django Debug Toolbar  https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

pip install django-ckeditor  --пакет CKEditor (расширенный функционал текстового редактора админки)
pip install django-simple-captcha  --капча
