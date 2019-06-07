#!/bin/sh

# Prepare log files and start outputting logs to stdout

mkdir -p /app/logs
touch /app/logs/gunicorn.log
touch /app/logs/gunicorn-access.log
tail -n 0 -f /app/logs/gunicorn*.log &

echo "Building Frontend"
python manage.py collectstatic --noinput
npm install
npm run build:prod
sleep 5
python manage.py migrate

echo "STARTING DJANGO SERVER"
exec gunicorn appemail.wsgi:application \
    --name appemail \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=info \
    --log-file=/app/logs/gunicorn.log \
    --access-logfile=/app/logs/gunicorn-access.log \
    "$@"