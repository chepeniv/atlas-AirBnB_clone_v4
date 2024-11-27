#!/bin/bash

clear;
#export HBNB_SH_TEST_DIR=$PWD/tests/sh_tests/;
#to change modes set HBNB_ENV to dev or test
HBNB_ENV=dev \
HBNB_MYSQL_DB=hbnb_$HBNB_ENV\_db \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_PWD=hbnb_$HBNB_ENV\_pwd \
HBNB_MYSQL_USER=hbnb_$HBNB_ENV \
HBNB_TYPE_STORAGE=db \
python3 console.py
# 2> /dev/null

