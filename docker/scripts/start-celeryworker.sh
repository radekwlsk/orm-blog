#!/bin/sh
# https://docs.celeryproject.org/en/latest/userguide/workers.html

set -o errexit
set -o nounset

celery -A orm_blog.taskapp worker \
        --loglevel=${CELERY_LEVEL:-INFO} \
        --concurrency=${CELERY_CONCURRENCY:-2}
