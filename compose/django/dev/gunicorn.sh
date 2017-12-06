#!/bin/sh

python3 manage.py makemigrations --settings=chordifyme.settings.local
python3 manage.py migrate --settings=chordifyme.settings.local
python3 manage.py collectstatic --noinput --settings=chordifyme.settings.local

# worker = 2 * CPUs + 1.
gunicorn chordifyme.wsgi:application -w 5 --worker-class 'gevent' --log-level debug --access-logfile logs/gunicorn/access.log --log-file logs/gunicorn/gunicorn.log -e DJANGO_SETTINGS_MODULE=chordifyme.settings.local -b :8000

#python3 manage.py runserver 0.0.0.0:8000 --settings=chordifyme.settings.local