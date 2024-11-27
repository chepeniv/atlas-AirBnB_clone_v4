# Atlas AirBnB Clone

## Resources
- [(youtube) HBnB Project Overview](https://www.youtube.com/watch?v=E12Xc3H2xqo)
- [(youtube) HBnB the console](https://www.youtube.com/watch?v=p00ES-5K4C8)
- [concept: AirBnB clone](https://intranet.atlasschool.com/concepts/74)
- [concept: python packages](https://intranet.atlasschool.com/concepts/66)
- [8.1. datetime](https://docs.python.org/3.4/library/datetime.html)
- [21.20. uuid](https://docs.python.org/3.4/library/uuid.html)
- [24.2. cmd](https://docs.python.org/3.4/library/cmd.html)
- [26.3. unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [pythonsheets : test](https://www.pythonsheets.com/notes/python-tests.html)
- [args and kwargs in python explained](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

## Background

### First Steps
- create parent class `BaseModel` that handles initialization, serialization and de-serialization
- create simple serialization/de-serialization flow:
	- Instance <--> Dictionary <--> `JSON` <--> string <--> file
- create child classes: `User`, `State`, `City`, `Place`, etc
- create an abstracted storage engine : File storage
- create `unittest` to validate all classes and the storage engine

### Command Interpreter Functionality
- create objects
- retrieve objects
- operate on objects
- update object attributes
- destroy objects

## Learning Goals

- how to create a python package
- how to create a command interpreter using the `cmd` module
- how to implement `unittest` on a large project
- how to serialize and de-serialize a class
- how to write and read a `json` file
- how to manage `datetime`
- what is an `uuid`
- what are `*args` and `**kwargs` and how to use them
- how to handle named arguments in a function

## Execution

the console script should run in both interactive and non-interactive mode :
`$ ./console.py`
`$ echo <cmd> | ./console.py`

test : `python3 -m unittest tests/test_models/test_base_model.py`
test should also pass none-interactive mode :
`$ echo "python3 -m unittest discover tests" | bash`

----

Command (cmd) notes and ideas for use.
Cmd.cmdqueue
A list of queued input lines. The cmdqueue list is checked in cmdloop() when new input is needed; if it is nonempty, its elements will be processed in order, as if entered at the prompt.

Cmd.intro
A string to issue as an intro or banner. May be overridden by giving the cmdloop() method an argument.

Circular Imports:
Circular imports occur when two or more modules depend on each other. This can be tricky and lead to import errors.
Solution:
Use import statements inside functions or methods, where they are only executed when the function is called.
Reorganize your code to reduce dependencies between modules.
