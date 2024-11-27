# run with sudo

# rm json.file;

export HBNB_ROOT=~/Learning/AtlasSchool/Sandbox/atlas-AirBnB_clone_v2/
export HBNB_SH_TEST_DIR=$HBNB_ROOT/tests/sh_tests/
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db

cat $HBNB_ROOT/setup_mysql_dev.sql | sudo mysql;

$HBNB_SH_TEST_DIR/console_cmds.sh | ./console.py &> $HBNB_SH_TEST_DIR/console_err

cat $HBNB_SH_TEST_DIR/mysql_cmds.sql | sudo mysql
