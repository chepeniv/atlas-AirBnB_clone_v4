echo "DROP DATABASE IF EXISTS hbnb_dev_db;" | mysql;
cat setup_mysql_dev.sql | mysql;
echo "quit" | sh run_console.sh

echo "USE hbnb_dev_db;\
SHOW CREATE TABLE place_amenity;\
SHOW CREATE TABLE reviews;\
SHOW CREATE TABLE amenities;\
SHOW CREATE TABLE places;\
SHOW CREATE TABLE users;\
SHOW CREATE TABLE cities;\
SHOW CREATE TABLE states;" | mysql > create_hbnb_dev_db.log

######## order of table drops ########
#
# DROP TABLE IF EXISTS place_amenity;
# DROP TABLE IF EXISTS reviews;
# DROP TABLE IF EXISTS amenities;
# DROP TABLE IF EXISTS places;
# DROP TABLE IF EXISTS users;
# DROP TABLE IF EXISTS cities;
# DROP TABLE IF EXISTS states;
#
