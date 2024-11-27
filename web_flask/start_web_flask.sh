#!/usr/bin/bash

file_name=$(basename $1 .py);

HBNB_ENV=dev \
HBNB_MYSQL_USER=hbnb_$HBNB_ENV \
HBNB_MYSQL_PWD=hbnb_$HBNB_ENV\_pwd \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_$HBNB_ENV\_db \
HBNB_TYPE_STORAGE=db \
python3 -m web_flask.$file_name
#curl 0.0.0.0:5000 ; echo "" | cat -e
