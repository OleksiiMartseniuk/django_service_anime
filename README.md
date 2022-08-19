# Django service anime
Web service - which allows you to get anime schedules from the site (animevost.org),
announcements, displaying a full description, viewing episodes. Using the admin panel to keep statistics, collect data.

#### Сlient
* Getting anime
* Getting list anime
* Filter on genre, anons, day week
* Search name anime
* Getting list announcements
* Getting list genre
* Get list episodes to watch
* Get list anime with an unspecified release date
* Sorting by rating, votes, time updated
#### Admin panel 
* Parser
    * Anime record
    * Schedule update
    * Delete anime
    * Series recording
    * Series update
    * Delete series
    * Auto update
* Statistics
* Download file log 
* Views file log

#### Technology
* Python => 3.10 
* Django
* Django Rest Framework
* Celery
* Redis
* Postgres 
* Requests
* BeautifulSoup
* Logging
* NGINX
* Docker

#### Test
`docker exec -it django_anime_service_web bash`
* Pytest
    * Run test(module animevost) `pytest src/tests/test_animevost`
* UnitTest Django
    * Run test(app) `python manage.py test src/tests/test_app`

#### Docs
* Swagger `http://localhost/swagger/`

#### Instructions

Сreate a file at the root of the project `.env.docker`

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

Build the image and run the container

`docker-compose up --build`

Create superuser
 
```
docker exec -it django_anime_service_web bash
python manage.py createsuperuser
```

If you need to clear the database

`docker-compose down -v`
