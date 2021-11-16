Media library
===

*Проект написанный для понимания взаимодействия с API разных сервисов авторизации*
___

:white_check_mark: Свой кастомный класс авторизации    
:white_check_mark: Авторизация через Google    
:white_check_mark: Авторизация через Spotify

[comment]: <> (:o:)

#### Использованные технологии:
```text
- Django
- Django Rest Framework
- PyJWT
- DRF yasg
```
Менеджер зависимостей используется
[poetry](https://python-poetry.org/docs)

API Сервисов:    
[Google](https://console.cloud.google.com/home/dashboard)    
[Spotify](https://developer.spotify.com/documentation/web-api/)

Создать файл .env, в папке config, для запуска проекта:

```dotenv
PROJECT_NAME=your_name_app
DEBUG=on/off 
SECRET_KEY=<app_secret_key>

# добавляем хосты без пробела и скобочек
ALLOWED_HOSTS=127.0.0.1,localhost,

# GOOGLE AUTH
GOOGLE_CLIENT_ID=<your_app_google_client_id>.apps.googleusercontent.com
# SPOTIFY AUTH
SPOTIFY_CLIENT_ID=<your_app_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_app_spotify_client_secret>
```

Команды для запуска проекта:

```shell
# Создать и активировать виртуальную среду
 poetry shell
# Создать миграции
./manage.py makemigrations 
# Запустить миграции
./manage.py migrate
# Создать суперпользователя
./manage.py createsuperuser
# Запустить сервер
./manage.py runserver
```
