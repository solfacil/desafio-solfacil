#!/bin/sh

set -e

. /opt/pysetup/.venv/bin/activate

python manage.py migrate

"$@"
