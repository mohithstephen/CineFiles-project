
@echo off
cd /d D:\CineFilesProject

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install django djangorestframework

echo Creating Django project...
if not exist manage.py (
    django-admin startproject cinefiles_project .
) else (
    echo Django project already exists, skipping creation...
)

echo Creating Django app...
if not exist cinefiles_app (
    django-admin startapp cinefiles_app
) else (
    echo Django app 'cinefiles_app' already exists, skipping creation...
)

echo Running migrations...
if exist manage.py (
    python manage.py migrate
) else (
    echo Error: manage.py not found in D:\CineFilesProject
    exit /b 1
)

echo Creating superuser...
set DJANGO_SUPERUSER_USERNAME=admin
set DJANGO_SUPERUSER_EMAIL=cinefiles@admin.com
set DJANGO_SUPERUSER_PASSWORD=cinefilespass
python manage.py createsuperuser --noinput


echo Starting Django server...
python manage.py runserver
