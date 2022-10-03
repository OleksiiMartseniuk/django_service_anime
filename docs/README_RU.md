<p align="center">
      <img src="https://i.ibb.co/CQtKPmb/pngwing-com.png" width="200">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.10.6-blue" alt="License">
   <img src="https://img.shields.io/badge/Framework-Django%204.0.5-blueviolet">
   <img src="https://img.shields.io/badge/Version-v1.0-blue" alt="Game Version">
   <img src="https://img.shields.io/badge/License-MIT-brightgreen" alt="License">
</p>

## О проекте
---

Веб сервис позволяющий получать, обновлять данные с сайта <b>animevost.org</b>. Контролировать процесс сбора данных с помощью панели администратора. Взаимодействовать с telegram ботом, собирать статистику пользователей и переодически напоминать о выходе новых серий.

## Документация
---
Язык [en](../README.md)
```
http://0.0.0.0/api/v1/
```
|Метод|Свободные эндпоинты|	Описания|
|-----|--------------------|---------|
|<b>GET</b>|**`/anime/`** |Получения списка аниме, фильтр `[genre, day_week, anons, indefinite_exit] `сортировка `[rating, votes]`|
|<b>GET</b>|**`/anime/genre/`**|Получения списка жанров|
|<b>GET</b>|**`/anime/series/`**| Получения списка жанров по `[id_anime]`|
|<b>GET</b>|**`/anime/{id}/`**| Получения полного описания|
||<b>Администратор telegram бота<b>|<b>Authorization: Token [<u>ApiKey</u>](#bавторизацияb)</b>|
|<b><b>POST</b></b>|**`/bot/create-user/`**| Регистрация пользователя telegram|
|<b>GET</b>|**`/bot/user-bot/`**| Получения списка пользователей telegram, фильтр `[user_id, staff]` |
|<b>POST</b>|**`/bot/statistic/`**| Запись статистики |
|<b>POST</b>|**`/bot/message/`**| Отправка сообщения пользователем|
|<b>POST</b>|**`/bot/add-anime/`**|Добавить аниме в отслеживаемые пользователем|
|<b>POST</b>|**`/bot/remove-anime/`**|Удаления аниме с отслеживаемых пользователем|
|<b>GET</b>|**`/bot/get-anime/{user_id}/{subscriber}/`**|Получения списка аниме отслеживаемые пользователем. <br>`subscriber (bool) - True:` Получения список подписок. <br>`subscriber (bool) - False:` Получения список возможных подписок|

### <b>Авто документация</b>

>`http://0.0.0.0/swagger/`<br>
>`http://0.0.0.0/redoc/`<br>

### <b>Авторизация</b>

<b>POST</b> **`/api-token-auth/`** Получения токена доступа `[username, password]` <u>ApiKey</u><br>
**`-H Authorization: Token ApiKey`**

### <b>Спецификаторы доступа</b>
**`Superuser`** - Создания пользователей, выписка спецификации доступа <br>
**`Admin-bot`** - Взаимодействие с telegram ботом<br>
**`User/Anonim`** - Доступны только свободные эндпоинты

### <b>Админ панель</b>

- Запись/Обновления аниме расписания
- Запись/Обновления  аниме анонсов
- Запись/Обновления  серий
- Обновления аниме с неопределенным сроком выхода
- Удаления всех файлов изображений
- Загрузка изображений на сервер telegram
- Статистика операций админа
- Просмотр/Загрузка логов
- Включения/Отключения авто обновлений

### <b>Телеграм</b>

- Отправка напоминаний о выходе новой серии пользователя телеграм при подписке на аниме

[Перейти к телеграм боту](https://github.com/OleksiiMartseniuk/bot_anime)

### <b>Технологии</b>

![Python](https://img.shields.io/badge/-Python-blue?style=flat-square)
![Django](https://img.shields.io/badge/-Django-blueviolet?style=flat-square)
![DRF](https://img.shields.io/badge/-DRF-red?style=flat-square)
![Celery](https://img.shields.io/badge/-Celery-important?style=flat-square)
![Redis](https://img.shields.io/badge/-Redis-critical?style=flat-square)
![Postgres](https://img.shields.io/badge/-Postgres-yellow?style=flat-square)
![NGINX](https://img.shields.io/badge/-NGINX-success?style=flat-square)
![Docker](https://img.shields.io/badge/-Docker-informational?style=flat-square)

<br>

### <b>Установка</b>

Создать файл в корне проекта `.env.docker`

```
export DEBUG=0
export SECRET_KEY='your_secret_key'
export DJANGO_SETTINGS_MODULE=config.settings
export DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 0.0.0.0'


# Redis
export REDIS_CLOUD_URL=redis://django_anime_service_redis:6379/0

# Data Base
export POSTGRES_DB=your_name_db
export POSTGRES_USER=your_name_user
export POSTGRES_PASSWORD=your_passwor
export HOST_DB=django_anime_service_database
export PORT_DB=5432

# Nginx
export TZ='your_timezone'
```

Создайте образ и запустите контейнер

```bash
docker-compose up --build
```

Создать суперпользователя

```bash
docker exec -it django_anime_service_web bash
python manage.py createsuperuser
```

Если вам нужно очистить базу данных

```bash
docker-compose down -v
```


### <b>Тест</b>


```bash
docker exec -it django_anime_service_web bash
```
Pytest
```bash
pytest src/tests/test_animevost
```
UnitTest Django
```bash
python manage.py test src/tests/test_app
```

## Разработчики

- [Martseniuk Oleksii](https://github.com/OleksiiMartseniuk)


## Лицензия

Проект DjangoServiceAnime распространяется под MIT лицензией.
