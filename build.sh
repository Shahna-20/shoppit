#!/user/bin/env bash

set -o errexit # exite on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate