#!/bin/sh

# Prepare log files and start outputting logs to stdout
echo "STARTING DJANGO SERVER"
mkdir -p /app/logs
touch /app/logs/gunicorn.log
touch /app/logs/gunicorn-access.log
tail -n 0 -f /app/logs/gunicorn*.log &

python manage.py collectstatic --noinput
npm run build:prod
sleep 10
python manage.py migrate


exec gunicorn appemail.wsgi:application \
    --name appemail \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=info \
    --log-file=/app/logs/gunicorn.log \
    --access-logfile=/app/logs/gunicorn-access.log \
    "$@"