#!/bin/sh
# https://gunicorn-docs.readthedocs.io/en/stable/settings.html

set -o errexit
set -o nounset

gunicorn config.wsgi:application \
        --bind ${GUNICORN_HOST:-0.0.0.0}:${GUNICORN_PORT:-8000} \
        --timeout ${GUNICORN_TIMEOUT:-300} \
        --workers ${GUNICORN_WORKERS:-4} \
        --threads ${GUNICORN_THREADS:-12} \
        --worker-class ${GUNICORN_WORKER_CLASS:-sync} \
        --name orm_blog \
        --access-logfile ${GUNICORN_ACCESS_LOGFILE:--} \
        --error-logfile ${GUNICORN_ERROR_LOGFILE:--} \
        --chdir /app
