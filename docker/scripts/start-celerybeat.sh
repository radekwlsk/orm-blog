#!/bin/sh

set -o errexit
set -o nounset

celery -A orm_blog.taskapp beat -l INFO --pidfile=
