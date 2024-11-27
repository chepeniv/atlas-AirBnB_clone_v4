# AirBnB Clone

## Video Resources
- [AirBnB Overview](https://www.youtube.com/watch?v=QTwmCB_AWqI)
- [2 - console](https://www.youtube.com/watch?v=jeJwRB33YNg)
- [3 - ORM](https://www.youtube.com/watch?v=ZwCD8cNZk9U)
- [4 - API](https://www.youtube.com/watch?v=LrQhULlFJdU)
- [Final Product (video no longer available)]()

## Final Product
the completed product will be composed of
- a command interpreter that manipulates data without a gui
- a website fronend showcasing the final product 
	- madeup of both static and dynamic components
- either a database or files that store objects
- an API providing a communication interface between the frontend and the backend for CRUD operations
![components](../assets/components_diagram.png)

## Concepts
- collaborative `unittest`
- python packages
- serialization/deserialization
- `*args`, `**kwarg`
- `datetime`

## Building Blocks
### the console
- create data model
- manage (CRUD) objects via concole (CLI)
- store and persist objects with a JSON file

#### manipulating a storage system
this storage system will provide an abstraction between objects and their storage.
meaning that from the console code, the front-end, and the RESTful API attention will
not be needed to how an object is stored. such implementation allows for the type of 
storage system to be changed easily without having to update the entire codebase.

the console will validate the storage engine

### web static
- create the HTML and CSS for the application
- create a template for each object

### MySQL storage
- replace the `.json` file storage with an sql database
- map models to a database table using an ORM

### web framework - templating
- create a python webserver
- use objects stored in the database to make the HTML dynamic

### RESTful API
- expose objects stored in a json file via a web-interface
- manipulate objects via the RESTful API

### web dynamic
- learn JQuery
- load objects from the client-side by using your own RESTful API

## Files and Directories
- `models/` will contain all classes
- `test/` will contain all `unittest`
- `console.py` is the entry point to the CLI
- `models/base_model.py` will be the base class for all models with common elements
	- attributes: `id`, `created_at`, and `updated_at`
	- methods: `save()` and `to_json()`
- `models/engine/` will contain all storage classes using the same prototype
	- `file_storage.py` will be stored here

## Storage

persistency allows for a program to use and reference objects created from other instances of its execution. this project makes use of two different storage types:
file and database

separating by functionality and responsibility is a great way to make code modular and independent. which allows us to swap out one component for another

### use class attributes over instance attributes
- straightforward class descriptions -- it will be apparent what a model should contain
- providing default values
- providirng the same model behaviour regardless of storage

### How to store instances
example:
```python
users = reload() # rereate list of objects from a file
user = User("A")
users.append(user)
save(users) # save all objects in list to a file
```
implementation-wise is a JSON representation since it is the common standard.
json allows various programs written in differen laguages to share data.

### JSON-serialization File-storage 
write to a file all objects created and updated in the CLI and restore them when
started again. pyhon objects cannot be stored and restored as "bytes" -- the
best way is serialize to a data structure

serialization : 
- `an_instance.to_json()` first converts the object to another python built-in serializable data structure (a dictionary) and returns it
- this sructure is then converted to a string with `a_string = JSON.dumps(a_dict)`
- finally this string is saved to a file in storage

the process of de-serializaion is the same but the other way around :
- read strings from file in storage
- convert string to data structure `a_dict = JSON.loads(a_string)`
- convert this data structure to an instance `an_instance = AnObject(a_dict)`

## `*args`, `**kwargs`

- `*args` is a tuple containing all arguments
- `**kwargs` is a dictionary containing arguments in a key=value form
these argument forms make functions more dynamic.
the order of arguments passed onto a function is anonymous arguments first followed
by all the named arguments

```python
def print_args(*args, **kwargs):
	print("{} -- {}".farmat(args, kwargs))
	
a_dict = { 'A' : 1, 'B' : 2, 'C' : 3 }

func(a_dict)		# ({ 'A' : 1, 'B' : 2, 'C' : 3 }) -- {}
func(*a_dict)		# ( 'A', 'B', 'C' ) -- {}
func(**a_dict)		# () -- { 'A' : 1, 'B' : 2, 'C' : 3 }
```

## `datetime`

```python
from datetime import datetime, timedelta

now = datetime.now()
print(type(now))		# <class 'datetime.dateime'>
print(now)				# 2024-08-27 07:00:43.114552
```
`now` in an object and it can be manipulated

```python
tomorrow = now + timedelta(days=1)
```
`strfime` can make datetime objects readable
```python
print(now.strftime("%A")) 	# Thursday
```


## Data Diagram
![classes](../assets/class_relations.jpg)
