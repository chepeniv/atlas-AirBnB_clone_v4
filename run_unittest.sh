clear -x;

echo path supplied $1

HBNB_ENV=test \
HBNB_MYSQL_USER=hbnb_test \
HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_test_db \
HBNB_TYPE_STORAGE=db \
python3 -m unittest $1 | tee unittest.log
