#!/bin/sh

until nc -z $DB_HOST $DB_PORT; do
    sleep 1
done

cd src

gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:${ROOT_PORT}
