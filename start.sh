#!/bin/sh
# Started by OceanLaunch (start command "sh start.sh"): bring the database up to date, then serve with gunicorn.
# exec hands over to gunicorn, so it gets the stop signal and shuts down cleanly.
set -e
python manage.py migrate --noinput
exec gunicorn config.wsgi --bind "0.0.0.0:${PORT:-8080}" --workers 2 --access-logfile -
