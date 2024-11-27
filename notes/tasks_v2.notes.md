# tasks

## task 0 - fork me if you can

common questions when working with a prexisting codebase:
- who wrote it 
- how does it work
- what are the unittest
- where is it stored
- why is it written the way that it is

although tempting one should refrain from rewritting everything.
regardless, trust should not be granted automatically.
always view it with a critical eye

whether the repo is forked or cloned, update the name as well as the README.
do not remove the original authors.

## task 1 - bug free

regardless of the storage engine used, all unittest must pass without errors

running the test with predefined environment variables
```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
```
due to their irrelevance, some test might need to be skipped with the `skipif` [feature](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)

for any skipped test, be sure to write a new one

### testing with mysql

create a specific database for testing. 

(1) assert the current state, (2) execute an action, and (3) validate the state changes performed by the action

when testing various components functionality it is better to do so in isolation

## task 2 - console improvements

update `def do_create(self, arg)` of the command interpreter `console.py` to allow for object creation with given parameters

command syntax : `create <class> <param1> <param2> <param3> ...`
parameter syntax : `<key>=<value>`
value syntax : `"<value>"`
	- double quotes within can be escaped with `\`
	- values passed will be deliniated by underscores. internally, replace theses with spaces
	- floats must contain dots otherwise an integer will be the default interpretation
uninterpretable parameters must be skipped

in the checker, this will be tested with the original `FileStorage` engine

FILE: `console.py`, `models/`, and `tests/`

## task 3 - mysql setup development

write an sql script to prepare a mysql server for the project

- database : `hbnb_dev_hb`
- user : `hbnb_dev` in `localhost`
- password : `hbnb_dev_pwd`
- the new user should have **all** privileges to the new db **only**
- add the `SELECT` privilege for the new user on `performance_schema`
- if either the db or the user already exist, the script should not fail

## task 4 - mysql setup test

write an sql script to prepare a mysql server for the project

- database : `hbnb_test_hb`
- user : `hbnb_test` in `localhost`
- password : `hbnb_test_pwd`
- the new user should have **all** privileges to the new db **only**
- add the `SELECT` privilege for the new user on `performance_schema`
- if either the db or the user already exist, the script should not fail

## task 5 - delete object

update `FileStorage` in `model/engine/file_storage.py`
add a new public instance method : `def delete(self, obj=None):` that deletes `obj` from `__objects` if it exist within. if `obj` is `None` don't do anything

update the prototype `def all(self)` to `def all(self, cls=None)` that returns a list of objects of the type of class determined by `cls` optional filter

FILE: `models/engine/file_storage.py`

## task 6 - dbstorage - states and cities

FILES: `base_model.py`, `city.py`, `state.py`, `models/engine/db_storage.py`, and `models/__init__.py`

![database schema](../assets/AtlasAirBnB-DB-Schema.jpg)

here we will transition from `FileStorage` to `DBStorage`.

it is not adviced that a service work with multiple backend storage systems
simultaneously. but it is common to have the storage layer abstracted in order to
be able to swap out the implementation as need be

add class attributes to `SQLStorage` with values for description and mapping to the 
database. modifying these values, or adding or removing attributes to the model will
force you to delete and reconstruct the database. although not optimal, it's fine 
for development purpsoses.

### steps

#### update : `models/base_model.py:BaseModel`

create `Base = declarative_base()` before `class BaseMode`.

- `BaseModel`: 
	- `id` - 60 char, unique, not null, primary key
	- `created_at` - datetime, not null, default is `datetime.utcnow()`
	- `updated_at` - datetime, not null, default is `datetime.utcnow()`
- move `models.storage.new(self)` from `def __init__(self, *args, **kwargs):` over to `def save(self):` and call it just before `model.storage.save()`
- in `def __init__(self, *args, **kwargs)` use `**kwargs` to create instance attributes
	- example: `kwargs={ 'name': 'value' }` --> `self.name = 'value'`
- update `to_dict()`
	- remove `_sa_instance_state` from the dictionary recturned if it exist
- add the public instance method `def delete(self)` to remove the current instance from `models.storage` by calling the mothod `delete`

#### update : `models/city.py:City`

- `City` inherits from `BaseModel` and then `Base` (order is important)
- `City`:
	- `__tablename__` represents the table name `cities`
	- `name` - string of 128 chars, can't be null
	- `state_id` 60 char, not null, foreign key to `state.id`

#### update : `models/state.py:State`

- `State` inherits from `BaseModel` and then `Base` (order is important)
- `State`:
	- `__tablename__` represents the table name `states`
	- `name` - string of 128 chars, can't be null
	- in `DBStorage` :
		- `cities` attribute must represent a relationship with class `Cities`
		- if a `State` object is deleted, then all linked `City` must be deleted as well
		- the reference from a `City` object to it's `State` should be named `state`
	- in `FileStorage` :
		- the getter attribute `cities` should return a list of `City` instances with `state_id` equal to the current `State.id` -- the relationship between `State` and `City` in `FileStorage`

#### new engine: `model/engine/db_storage.py:DBStorage`

private class attributes :
- `__engine` set to `None`
- `__session` set to `None`

public instance methods :
- `__init__(self)` :
	- create engine `self.__engine`
	- link this engine to the mysql database and user : `hbnb_dev` and `hbnb_dev_db`:
		- dialect : `mysql` ; driver `mysqldb`
	- retrieve values from the given environment variables :
		- mysql user from `HBNB_MYSQL_USER`
		- mysql password from `HBNB_MYSQL_PWD`
		- mysql host from `HBNB_MYSQL_HOST` (=`localhost`)
		- mysql database from `HBNB_MYSQL_DB`
	- set the option `pool_pre_ping=True` when calling `create_engine`
	- drop all tables if `HBNB_ENV` is equal to `test`
- `all(self, cls=None)`:
	- query the current database session `self.__session` to extract all objects dependant on the class name `cls`
	- if `cls=None` query all types of objects
	- method must return a dictionary with elements of the form :
		- `'<class>.<id>': <object>`
- `new(self, obj)` : adds the object to the current database session (`self.__session`)
- `save(self)` : commit all changes to the current database session
- `delete(self, obj=None)` : if not `None`, delete given object from the current database session
- `reload(self)`:
	- create all tables in the database (sqlalchemy)
		- **ALL** classes that inherit from `Base` **MUST** be imported before calling `Base.metadata.create_all(engine)`
	- create the current database session `self.__session` from the engine `self.__engine` by using a `sessionmaker`
		- `expire_on_commit` must be set to `False`
		- `scoped_session` to ensure the session is thread-safe

#### add `models/__init__.py`

- add a conditional that depends on the value `HBNB_TYPE_STORAGE`
	- if equal to `db`:
		- import `DBStorage`
		- create and instance of `DBStorage` and store it in the variable `storage`
		- execute `storage.reload()` afterwards
	- this switch permits the changing of the storage type directly by manipulating an environment variable

## task 7 - dbstorage - user

#### update : `models/user.py:User`
- inherit from `BaseModel` and `Base` in order
- implement the class `User`
class attributes : 
- `__tablename__` the table `users` to map to
- `email` (column-field) 128 char string, can't be null
- `password` (column-field) 128 char string, can't be null
- `first_name` (column-field) 128 char string, can't be null
- `last_name` (column-field) 128 char string, can't be null

## task 8 - dbstorage - place

#### update : `models/place.py:Place`

- inherit from `BaseModel` and `Base` in order

implement the class `Place`

class attributes : 
- `__tablename__` the table `places` to map to
- `city_id` (column-field) 60 char string, can't be null, foreign key to `cities.id`
- `user_id` (column-field) 60 char string, can't be null, foreign key to `users.id`
- `name` (column-field) 60 char string, can't be null
- `description` (column-field) 1024 char string, can't be null
- `number_rooms` (column-field) integer, can't be null, default value `0`
- `number_bathrooms` (column-field) integer, can't be null, default value `0`
- `max_guest` (column-field) integer, can't be null, default value `0`
- `price_by_night` (column-field) integer, can't be null, default value `0`
- `latitude` (column-field) float, can't be null
- `longitude` (column-field) float, can't be null

#### update : `models/user.py`

- class attribute `places` represents a relationship the class `PLace`
- if the `User` object is deleted so too must all linked `Place` objects automatically
- the reference from a `Place` to its `User` should be named `user`

#### update : `models/city.py:City`

- class attribute `places` must represent a relationship with the class `Place`
- if the `City` object is deleted so too must all linked `Place` objects automatically
- the reference from `Place` to `City` should be named `cities` (plural?)

## task 9 - dbstorage - review

#### update : `models/review.py:Review`

inherit from `BaseModel` and `Base` in order

`Place` class attributes :
- `__tablename__` name of the table to map to, `reviews`
- `text` (column-field) 1024 char string, can't be null
- `place_id` (column-field) 60 char string, can't be null, foreign key mapped to `places.id`
- `user_id` (column-field) 60 char string, can't be null, foreign key mapped to `users.id`

#### update : `models/user.py:User`

- add class attribute `reviews` that represents a relationship with the class `Review`
- if a `User` is deleted then so too must all linked `Review`s automatically
- the reference from `Review` to its `User` is `user`

#### update : `models/place.py:Place`

for `DBStorage`
- class attribute `reviews` represents a relationship with the class `Review`
- if a `Place` is deleted then so too must all linked `Review`s automatically
- the reference from `Review` to its `Place` is `place`

for `FileStorage`
- getter attribute `reviews` returns a list of `Review` instances with `place_id` equal to current `Place.id` -- this will be the `FileStorage` relationship between `Place` and `Review`

## task 10 - dbstorage - amenity

#### update : `models/amenity.py:Amenity`

inherit from `BaseModel` and `Base` in order

`Amenity` class attributes :
- `__tablename__` name of the table to map to, `amenities`
- `name` (column-field) 128 char string, can't be null
- `place_amenities` (column-field) represents a many-to-many relationship between `Place` and `Amenity`

#### update : `models/place.py:Place`

- add an instance of an sqlalchemy-table called `place_amenity` for creating the 
  many-to-many relationship
	- table name `place_amenity`
	- `metadata = Base.metadata`
	- `place_id` (column-field) 60 char string, foreign key to `places.id`, primary key, never null
	- `amenity_id` (column-field) 60 char string, foreign key to `amenities.id`, primary key, never null

for `DBStorage` :
- the class attribute `amenities` represents a relationship with the class `Amenity`, but also as `secondary` to `place_amenity` with option `viewonly=False` 

for `FileStorage` :
- getter attribute `amenities` returns a list of `Amenity` instances based on the attribute `amenity_ids` containing all `Amenity.id` linked to `Place`
- setter attribute `amenities` handles `append` method for adding an `Amenity.id` to the attribute `amenity_ids`. this method should only accept `Amenity` object - otherwise do nothing

### many-to-many relationships

these relationships are implemented by creating a table that references the two tables to link. each entry is a unique pairing of records from each table. this ways the original tables can retain their simpler format
