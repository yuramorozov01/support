#!/bin/bash

docker-compose --env-file ./support/src/.env exec support python3 ./src/manage.py createsuperuser
