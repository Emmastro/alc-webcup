#!/bin/bash
# empty database
python manage.py flush
# make migration
python manage.py makemigration
# migrate
python manage.py migrate
# populate database
