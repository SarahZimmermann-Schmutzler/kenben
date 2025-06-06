#!/usr/bin/env bash

# Exit immediately if any command exits with a non-zero status
set -e


# Step 1: Run database migrations
echo "Running database migrations..."
python manage.py makemigrations || { echo "Makemigrations failed"; exit 1; }
python manage.py migrate || { echo "Migration failed"; exit 1; }


# Step 2: Check if superuser already exists
echo "Checking if superuser exists..."

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
import sys
sys.exit(0) if User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists() else sys.exit(1)
"

if [ $? -ne 0 ]; then
  echo "Creating superuser..."
  python manage.py createsuperuser --noinput \
    --email "$DJANGO_SUPERUSER_EMAIL" \
    --username "$DJANGO_SUPERUSER_USERNAME"
else
  echo "Superuser already exists, skipping creation."
fi

# Step 3: Start the Django server 
#echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000