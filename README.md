<p align="center">
      <img src="https://i.ibb.co/CQtKPmb/pngwing-com.png" width="200">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.10.6-blue" alt="License">
   <img src="https://img.shields.io/badge/Framework-Django%204.0.5-blueviolet">
   <img src="https://img.shields.io/badge/Version-v1.0-blue" alt="Game Version">
   <img src="https://img.shields.io/badge/License-MIT-brightgreen" alt="License">
</p>

## About

Web service that allows you to receive, update data from the site <b>animevost.org</b>. Manage the data collection process using the admin panel. Interact with the telegram bot, collect user statistics and periodically remind you of the release of new episodes.

## Documentation

Language [ru](./docs/README_RU.md)
```
http://0.0.0.0/api/v1/
```
|Method|Free endpoints|	Descriptions|
|-----|--------------------|---------|
|<b>GET</b>|**`/anime/`** |Getting a list of anime, filter `[genre, day_week, anons, indefinite_exit] `sorting `[rating, votes]`|
|<b>GET</b>|**`/anime/genre/`**|Getting a list of genres|
|<b>GET</b>|**`/anime/series/`**| Getting a list of series by `[id_anime]`|
|<b>GET</b>|**`/anime/{id}/`**| Get a full description|
||<b>Telegram bot administrator<b>|<b>Authorization: Token [<u>ApiKey</u>](#authorization)</b>|
|<b><b>POST</b></b>|**`/bot/create-user/`**| Telegram user registration|
|<b>GET</b>|**`/bot/user-bot/`**| Getting a list of telegram users, filter `[user_id, staff]` |
|<b>POST</b>|**`/bot/statistic/`**| Recording statistics |
|<b>POST</b>|**`/bot/message/`**| Sending a message by a user|
|<b>POST</b>|**`/bot/add-anime/`**|Add anime to subscriber list|
|<b>POST</b>|**`/bot/remove-anime/`**|Removing anime from a subscriber|
|<b>GET</b>|**`/bot/get-anime/{user_id}/{subscriber}/`**|Getting the list of anime followed by the user. <br>`subscriber (bool) - True:` Getting a list of subscriptions. <br>`subscriber (bool) - False:` Getting a list of possible subscriptions|

### <b>Auto documentation</b>

>`http://0.0.0.0/swagger/`<br>
>`http://0.0.0.0/redoc/`<br>

### <b>Authorization</b>

<b>POST</b> **`/api-token-auth/`** Getting an access token `[username, password]` <u>ApiKey</u><br>
**`-H Authorization: Token ApiKey`**

### <b>Access Specifiers</b>
**`Superuser`** - Creating users, issuing an access specification <br>
**`Admin-bot`** - Interaction with telegram bot<br>
**`User/Anonim`** - Only free endpoints are available

### <b>Admin panel</b>

- Record/Update anime schedule
- Recording/Updating anime announcements
- Record/Update series
- Anime updates with an unspecified release date
- Deleting all image files
- Uploading images to the telegram server
- Admin Statistics
- View/Download logs
- Enable/Disable auto updates

### <b>Telegram</b>

- Sending new series release reminders to telegram user when subscribing to anime

[Go to telegram bot](https://github.com/OleksiiMartseniuk/bot_anime)

### <b>Technology</b>

![Python](https://img.shields.io/badge/-Python-blue?style=flat-square)
![Django](https://img.shields.io/badge/-Django-blueviolet?style=flat-square)
![DRF](https://img.shields.io/badge/-DRF-red?style=flat-square)
![Celery](https://img.shields.io/badge/-Celery-important?style=flat-square)
![Redis](https://img.shields.io/badge/-Redis-critical?style=flat-square)
![Postgres](https://img.shields.io/badge/-Postgres-yellow?style=flat-square)
![NGINX](https://img.shields.io/badge/-NGINX-success?style=flat-square)
![Docker](https://img.shields.io/badge/-Docker-informational?style=flat-square)

<br>

### <b>Installation</b>

Сreate a file at the root of the project `.env`

```
export DEBUG=0
export SECRET_KEY='your_secret_key'
export DJANGO_SETTINGS_MODULE=config.settings
export DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 0.0.0.0'


# Redis
export REDIS_PASSWORD=yourpassword
export REDIS_HOST=django_anime_service_redis
export REDIS_PORT=6379

# Data Base
export POSTGRES_DB=your_name_db
export POSTGRES_USER=your_name_user
export POSTGRES_PASSWORD=your_password
export HOST_DB=django_anime_service_database
export PORT_DB=5432

# Nginx
export TZ='your_timezone'
```

Build the image and run the container

```bash
docker-compose up --build
```

Create superuser

```bash
docker exec -it django_anime_service_web bash
python manage.py createsuperuser
```

If you need to clear the database

```bash
docker-compose down -v
```


### <b>Test</b>


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

## Developers

- [Martseniuk Oleksii](https://github.com/OleksiiMartseniuk)


## License

Project DjangoServiceAnime is distributed under the MIT license.
