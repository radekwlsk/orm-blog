#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

python manage.py runserver_plus 0.0.0.0:8000
