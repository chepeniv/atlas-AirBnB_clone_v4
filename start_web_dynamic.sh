#!/usr/bin/bash
# run with sudo

clear;
echo "usage : "
echo "sudo sh start_web_dynamic.sh path/to/script.py"

module=$(basename $1 .py);

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
