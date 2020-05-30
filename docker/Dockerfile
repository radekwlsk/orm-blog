FROM python:3.8-alpine

# User ID for the django user we're creating. The builder can set this to the
# host user's ID to avoid file permissions problems.
ARG USER_ID=1000

# Whether we're running in local development mode
ARG DEV_MODE=0

# Explicitly set the application user's home folder
ENV HOME=/home/django
ENV \
# Disable buffering on writing to stdout/stderr. This is to avoid loss of logs in
# the event of an application crash.
    PYTHONUNBUFFERED=1 \
# Disable Pipenv's spinner to stop it from filling logs with garbage
    PIPENV_NOSPIN=1 \
# Increase the pipenv timeout, it can take a while to lock dependencies
    PIPENV_TIMEOUT=900 \
# And a location for the application virtualenv based on the above
    VIRTUAL_ENV=$HOME/venv \
# Add virtualenv bin folder to the PATH
    PATH="$HOME/venv/bin:$PATH" \
# Add the project folder to PYTHONPATH so the main package is always importable
    PYTHONPATH="/app:$PYTHONPATH" \
# Save the lock file here if this is the first build
    BUILD_PIPFILE_LOCK=$HOME/Pipfile.lock.build

RUN apk update \
  # psycopg2 dependencies
  && apk --no-cache add \
    linux-headers gcc python3-dev musl-dev postgresql-dev \
  # Pillow dependencies
  jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  libffi-dev py-cffi \
  # Translations dependencies
  gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  postgresql-client \
  # Jupyter dependencies
  build-base \
  # Ops tools
  vim curl

# Install pipenv globally
RUN HOME=/tmp pip install --no-cache-dir pipenv==2018.11.26

# Create the user and group to run the Django application as
RUN addgroup --system --gid $USER_ID django \
    && adduser --system --home $HOME --uid $USER_ID --ingroup django django

# Copy the start scripts, make them executable, and set ownership
COPY ./docker/scripts/ /
RUN chown -R django /*.sh && chmod +x /*.sh

# Pipenv needs writable access to /app directory to be able to install dependencies
RUN mkdir -p /app && chown django /app

USER django


# Pull in Pipfile and Pipfile lock. This is done separately for layer caching reasons.
# We copy Pipfile.lock using a wildcard because it might not exist.
COPY ./backend/Pipfile ./backend/*.lock /app/
WORKDIR /app

# Prepare virtualenv and install dependencies
RUN python3 -m venv $VIRTUAL_ENV \
    && if [ $DEV_MODE -eq 1 ]; then \
    # dev mode, install dev dependencies
    # We'd like this to fail if the Pipfile.lock is out of date, but also to generate
    # the lockfile if it doesn't exist, which it won't on the first build.
        pipenv install --dev --deploy; \
    else \
    # normal (production) mode, install non-dev dependencies while verifying that
    # Pipfile.lock is up to date. Manually check if Pipfile.lock exists because --deploy
    # will still generate a new one if it's not there.
        [ -f Pipfile.lock ] || { echo 'No Pipfile.lock found' ; exit 1; }; \
        pipenv install --deploy; \
    fi \
    && rm -rf $HOME/.cache/*

# Copy the application data in
COPY ./backend /app/
COPY ./shared /app/shared/

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start-gunicorn.sh"]
