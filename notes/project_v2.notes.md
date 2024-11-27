# Atlas AirBnB Clone v2

## Environment Variables

```bash
HBNB_ENV = {dev, test, production}
HBNB_MYSQL_USER = user
HBNB_MYSQL_PWD = pwd/
HBNB_MYSQL_HOST = 
HBNB_MYSQL_DB =
HBNB_TYPE_STORAGE = {FileStorage, db, DBStorage}
```

## Resources

- [python docs: cmd](https://docs.python.org/3/library/cmd.html) 
- [python docs: unit testing](https://docs.python.org/3/library/unittest.html#module-unittest) 
- [args and kwargs in python](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/) 
- [SQLAlchemy docs](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) 
- [MySQL: Users and Permissions](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql) 
- [Python doc: OS](https://docs.python.org/3/library/os.html#os.getenv) 
- [MySQL doc: 15-Statements](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html) 

## Goals

- what is unit-testing and how to implement it in large project
- what `*args` and `**kwargs`
- how to handle named arguments in a function
- how to create a mysql database
- how to create mysql users and grant privileges
- what is an orm
- how to map a python class to a mysql table
- how to handle 2 different storages engines withh the same codebase
- how to use environment variables

## Python Unittesting

- store all testfiles in `tests`
- use the `unittest` module
- files should be prefixed with `test_`
- testfile organization should mirror the organization of the main project files
- execute testfiles using 
```bash
python3 -m unittest discover tests
```
- document all modules, classes, and functions

## SQL Scripts

- sql scripts should start with descriptive comment of the task
- sql queries should be preceded by a descriptive comment
