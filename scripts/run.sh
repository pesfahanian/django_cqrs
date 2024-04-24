#!/bin/bash

set -e

watch="watchmedo auto-restart --directory=./ --pattern='*.py' --recursive --"

gnome-terminal --title="Dajngo-CQRS Django Server" -- /bin/sh -c \
    "python manage.py runserver 0.0.0.0:8666"
