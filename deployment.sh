#!/bin/bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createcachetable
bash api/ml_models/background_train.sh &