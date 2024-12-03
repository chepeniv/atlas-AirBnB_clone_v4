#!/usr/bin/bash

clear;

echo "usage : "
echo "sudo sh start_web_dynamic.sh path/to/script.py\n"

# if you don't know how to track down and terminate orphaned process
# just run start_api_v1.sh first on a separate terminal before
# executing this script and leave the following commented-out

# sh start_api_v1.sh & cat api_v1.out

echo " **** web dynamic flask started **** "

module=$(basename "$1" .py);

# HBNB_MODELS_ROOT=../models \
# HBNB_API_HOST=0.0.0.0 \
# HBNB_API_PORT=5001 \
# HBNB_ENV=dev \
HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_USER=hbnb_dev \
HBNB_TYPE_STORAGE=db \
python3 -m web_dynamic.$module
