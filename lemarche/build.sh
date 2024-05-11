#!/bin/bash

# Display message indicating the start of the build process
echo "Building the project..."

# Install Python dependencies from requirements.txt
python3.9 pip install Django
python3.9 -m pip install -r requirements.txt

# Run Django migrations
echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
