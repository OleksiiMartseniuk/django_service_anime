#!/bin/sh

echo "Waiting for web..."

while ! nc -z web 8000; do
    sleep 0.1
done

echo "Beat started"

celery -A config beat -l info

exec $cmd
