#!/bin/sh
python api/infra/manage.py migrate
exec "$@"