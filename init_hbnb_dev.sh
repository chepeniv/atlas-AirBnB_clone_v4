# usage:
# sudo sh init_hbnb_dev.sh

# reset database
cat reset_hbnb_dev.sql | mysql

# start console for it to structure the database
echo exit | sh start_console.sh

# dump data into new database
cat data/100-dump.sql | mysql
