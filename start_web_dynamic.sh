#!/usr/bin/bash
# run with sudo

clear;

HBNB_API_HOST=0.0.0.0 \
HBNB_API_PORT=5001 \
HBNB_ENV=dev \
HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_USER=hbnb_dev \
HBNB_TYPE_STORAGE=db \
python3 -m web_dynamic.0-hbnb
