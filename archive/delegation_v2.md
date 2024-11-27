# delegation

add more subtask for any issues that arise

## priority

- [ ] task1 - bug free - **Ariel**, **chepe**
	- reference: [feature](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)

----

## in progress

----

## extra

### console

- [ ] implement `destroy all` -- for convenience

----

## completed

- [x] task0 - fork

- [x] task2 - console improvements - **chepe**

- [x] task3 - mysql setup dev - **Ariel**

- [x] task4 - mysql setup test - **Ariel**

- [x] task5 - delete object - **chepe**

- [x] task6 - dbstorage states and cities - **chepe**
	- [x] update `models/__init__.py`
	- [x] update `models/base_model.py`
		- [x] `kwargs={ 'name': 'value' }` --> `self.name = 'value'`
	- [x] create new engine `models/engine/db_storage.py`
		- [x] `__init__(self)`
		- [x] `all(self, cls=None)`
		- [x] `new(self, obj)`
		- [x] `save(self)`
		- [x] `reload(self)`
		- [x] `delete(self, obj=None)`
	- [x] update `models/state.py`
		- [x] implement storage-dependent behavior
	- [x] update `models/city.py`
	- [x] get code to work
	- [x] fix bugs
		- [x] fixed `_sa_instance_state` issue

- [x] task7 - dbstorage user - **Ariel**

- [x] task8 - dbstorage place - **Ariel**
	- [x] add the required columns
	- [x] contrary to instruction: don't rename `user_id` to `user`
	- [x] contrary to instruction: don't rename `city_id` to `cities`
	- [x] `models/user.py:User`
		- [x] `places = relationship('Place', cascade='all, delete')`
	- [x] `models/city.py:City`
		- [x] `places = relationship('Place', cascade='all, delete')`

- [x] task9 - dbstorage review - **Ariel**
	- [x] add the required columns
	- [x] contrary to instruction: don't rename `user_id` to `user`
	- [x] contrary to instruction: don't rename `place_id` to `place`
	- [x] `models/user.py:User`
		- [x] `reviews = relationship('Review', cascade='all, delete')`
	- [x] `models/place.py:Place`
		- [x] check out how state is written for this one

- [x] task10 - dbstorage amenity - **Ariel**, **chepe**
	- [x] add the required columns
	- [x] `models/place.py:Place` - **chepe**
		- [x] create new table `place_amenity`
		- [x] update class

- [x] add `do_models` -- list all models available
- [x] `console_util.py` - **chepe**
- [x] `console.py`
- [x] reintegrate `file_storage.py` - **chepe**
	- [x] implement `create Class key1="value1" key2="value2" ...` format
- [x] ensure `create Class key1="value1" key2="value2" ...` doesn't crash with `DB_Storage` when an invalid attribute is given
- [x] get `create Class key1="value1" key2="value2" ...` to not create false attributes with `FileStorage`
