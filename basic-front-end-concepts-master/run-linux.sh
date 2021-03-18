#!/bin/bash
pip3 install virtualenv
virtualenv venv
/bin/bash -c ". venv/bin/activate; exec /bin/bash -i"
cd learning-app/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
