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

#### Test
* Pytest
    * Run test(module animevost) `pytest src/tests/test_animevost`
* UnitTest Django
    * Run test(app) `python manage.py test src/tests/test_app`

#### Docs
* Swagger

