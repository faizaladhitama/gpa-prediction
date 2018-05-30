#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py createcachetable
python manage.py populate_db
python manage.py train_model
