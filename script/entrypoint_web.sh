#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $HOST_DB $PORT_DB; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000

exec "$@"
