#!/bin/bash
pip3 install virtualenv
virtualenv venv
chsh -s /bin/zsh -c ". venv/bin/activate; exec /bin/bash -i"
cd learning-app/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

