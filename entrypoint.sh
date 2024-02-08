#!/bin/sh
python3 manage.py makemigrations
python3 manage.py migrate
celery -A crypto_tracker worker -l info
