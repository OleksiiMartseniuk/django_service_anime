# Django service anime
Web service - which allows you to get anime schedules from the site (animevost.org),
announcements, displaying a full description, viewing episodes. Using the admin panel to keep statistics, collect data.

#### Сlient
* Getting anime
* Getting announcements
* Getting anime by day of the week
* Get episodes to watch
#### Admin panel 
* Parser
    * Anime record
    * Schedule update
    * Delete anime
    * Series recording
    * Series update
    * Delete series
* Statistics
* Download file log 
* Views file log

#### Technology
* Python => 3.10 
* Django
* Django Rest Framework
* Celery
* Redis
* Sqlite 
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

