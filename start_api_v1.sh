#!/usr/bin/bash

clear;

# HBNB_MODELS_ROOT=../models \
HBNB_ENV=dev \
HBNB_API_HOST=0.0.0.0 \
HBNB_API_PORT=5000 \
HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_USER=hbnb_dev \
HBNB_TYPE_STORAGE=db \
python3 -m api.v1.app

#curl -X GET 0.0.0.0:5000/api/v1/status
