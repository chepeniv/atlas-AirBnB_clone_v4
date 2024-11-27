# task1 - test list

## `pycodestyle`

things to check:
- line length < 80
- no trailing whitespace
- correct indentation
- add documentation
- use explicit `except` statements

- [ ] console
- [ ] models
- [ ] engine
- [ ] tests

## `FileStorage`

- [ ] test number >= 50
- [ ] discover tests success
- [ ] test `console.py`
- [ ] test `BaseModel`
- [ ] test `models/`
- [ ] test `FileStorage`

## `DBStorage`

- [ ] test number >= 50
- [ ] discover tests success
- [ ] test `console`
- [ ] test `BaseModel`
- [ ] test `models/`
- [ ] test `FileStorage`

----

### Task 7

- [ ] File exists
- [ ] Table users correctly created
- [ ] Can create User with email, password,
      first name and last name via the console
- [ ] Can create User with email and password via the console
- [ ] Can’t create User with only email via the console
- [ ] Can’t create User with only password via the console
- [ ] Can’t create User without email and password via the console

----

### Task 8

- [ ] Files exist
- [ ] Test
- [ ] Rollback code
- [ ] Table places correctly created
- [ ] Can create Place with city id (existing),
      user id (existing), name, description, number rooms,
      number bathrooms, max guest, price by night, latitude
      and longitude via the console
- [ ] Can create Place with city id (existing), user id (existing),
      name, number rooms, number bathrooms, max guest, price by night,
      latitude and longitude via the console
- [ ] Can create Place with city id (existing), user id (existing),
      name, number bathrooms, max guest, price by night, latitude and
      longitude via the console
- [ ] Can create Place with city id (existing), user id (existing),
      name, max guest, price by night, latitude and longitude via the console
- [ ] Can create Place with city id (existing), user id (existing),
      name, price by night, latitude and longitude via the console
- [ ] Can create Place with city id (existing), user id (existing),
      name, latitude and longitude via the console
- [ ] Can create Place with city id (existing), user id (existing),
      name and longitude via the console
- [ ] Can create Place with city id (existing), user id (existing)
      and name via the console
- [ ] Can’t create Place with only city id (existing) and user id (existing) via the console
- [ ] Can’t create Place with city id (not existing), user id (existing) and name via the console
- [ ] Can’t create Place with city id (existing), user id (not existing) and name via the console
- [ ] Can’t create Place without parameters via the console
- [ ] Can list all Place in MySQL

----

### Task 9

- [ ] Files exist
- [ ] Table reviews correctly created
- [ ] Can create Review with place id (existing),
      user id (existing) and text via the console
- [ ] Can’t create Review with only place id (existing)
      and user id (existing) via the console
- [ ] Can’t create Review with place id (not existing),
      user id (existing) and text via the console
- [ ] Can’t create Review with place id (existing),
      user id (not existing) and text via the console
- [ ] Can’t create Review with only place id (existing)
      and text via the console
- [ ] Can’t create Review with only user id (existing)
      and text via the console
- [ ] Can list all Review in MySQL
