# usage:
# sudo sh init_hbnb_dev.sh

# reset database
cat data/reset_hbnb_dev.sql | mysql

# start console for it to structure the database
echo exit | sh start_console.sh 2>error.log 1>/dev/null

# dump data into new database
cat data/100-dump.sql | mysql
