#!/bin/bash

set -e

if [ $# -eq 0 ]; then
    echo "Usage: ./create_django_app.sh <app_name>"
    exit 1
fi

APP_NAME=$(echo "$1" | tr '[:upper:]' '[:lower:]')

mkdir -p apps/$APP_NAME

touch apps/$APP_NAME/__init__.py

cat > apps/$APP_NAME/apps.py <<EOL
from django.apps import AppConfig


class ${1^}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.$APP_NAME'
EOL

echo "App '$APP_NAME' created successfully."

SETTINGS_FILE="config/settings/base.py"
APP_CONFIG="'apps.$APP_NAME.apps.${1^}Config',"

if grep -q "$APP_CONFIG" "$SETTINGS_FILE"; then
    echo "App '$APP_NAME' is already added to INSTALLED_APPS."
else
    sed -i "/^INSTALLED_APPS = \[/a \    $APP_CONFIG" "$SETTINGS_FILE"
    echo "App '$APP_NAME' added to INSTALLED_APPS."
fi
