# tasks v3

## 0. restart from scratch

**DONE**

## 1. never fail

`atlas-AirBnB_clone_v3/tests`

- all previous test must pass (don't remove them)
- add as many new test as you can (they are mandatory for some tasks)

the importance of unittest is that they can help ensure that when new features
are added or a refactoring is done that previous functionality isn't broken

## 2. code review

`code_review.txt`

- review a peers pull request on the branch `storage_get_count` (task 3)
- accept the pull request with your review in the comments

### expectations

- `code_review.txt` must contain the github username of who's being reviewed
- it must be done on github in the comments for the pull request
	- created from the branch `storage_get_count`
	- only the reviewer can approve the pull
	- the branch must **not** be deleted after approval
- comments must be _useful_
	- questions for difficult-to-understand code
	- styling issues
	- error handling
	- duplicate code
	- potential bugs
	- efficiency
	- typographical errors

### what is a code review ?

when one developer finishes working on an issue, another developer looks over
the result and considers amongst other things :
- logical errors
- requirements and their implementation (or lack thereof)
- are the new automated tests sufficient ? should they be re-written ?
- does it conform to styleguides ?
all this helps developers familiarise themselves with the codebase as well as
learning new technologies and strategies

#### resources

- [why code-reviews matter](https://www.atlassian.com/agile/software-development/code-reviews)
- [best practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices)
- [reviewing changes in pull](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests)
- [youtube: how to review the right way](https://www.youtube.com/watch?v=lSnbOtw4izI)
- [effective pull request](https://codeinthehole.com/tips/pull-requests-and-other-good-practices-for-teams-using-github/)
- [merging vs rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

## 3. improve storage

`models/engine/db_storage.py`\
`models/engine/file_storage.py`\
`test/test_models/test_engine/test_file_storage.py`\
`test/test_models/test_engine/test_db_storage.py`

create branch `storage_get_count` and update `DBStorage` and `FileStorage`

- add method to retrieve one object
	- `def get(self, kind, idnum):`
	- returns `None` if not found
- add method to count the number of objects in storage
	- `def count(self, kind=None)`
	- returns number of items found for the given class `kind` otherwise
	  the total number of all objects in storage
- add new test for these new methods for each storage engine

## 4. status of your api

`api/__init__.py`\
`api/v1/app.py`\
`api/v1/__init__.py`\
`api/v1/views/__init__.py`\
`api/v1/views/index.py`

the first endpoint (route) should return the status of your api
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
```
on another terminal
```bash
curl -X GET http://0.0.0.0:5000/api/v1/status
```

### instructions

- create directories `api` and `api/v1` with empty `__init__.py` files in each
- in `v1/` create `app.py`
	- create variable `app` instance of `Flask`
	- `from models import storage`
	- `from api.v1.views import app_views`
	- register the blueprint `app_views` to the `Flask` instance `app`
	- declare a method to handle `@app.teardown_appcontext`
		- call `storage.close()`
	- within `if __name__ == "__main__":`
		- run the Flask server `app`
		- set `host=HBNB_API_HOST` or `0.0.0.0` if not defined
		- set `port=HBNB_API_PORT` or `5000` if not defined
		- set `threaded=True`
- create directory `v1/views` and nonempty file `__init__.py`
	- `from flask import Blueprint`
	- create variable `app_views` instance of `Blueprint` (url prefix `/api/v1`)
	-  add a wildcard import of everything in the package `api.v1.views.index`
		- pep8 will dislike this, but `__init__.py` wont be checked
		- this will prevent circular imports later
	- create `index.py`
		- `from api.v1.views import app_views`
		- create route `/status` on the object `app_views` that returns json:
			- `"status": "OK"`

## 5. some stats

`api/v1/views/index.py`

create an endpoint that retrieves the number of each object by type

- route : `/api/v1/stats`
- use `count` from `storage`

## 6. not found

`api/v1/app.py`

create a handler for `404` errors that returns a json-formatted `404` status
code response. content: `"error": "Not found"`

## 7. state

`api/v1/views/states.py`
`api/v1/views/__init__.py`

create a new view for `State` objects that handles all default RESTful API
actions

in `api/v1/views/states.py` :
- use `to_dict()` to retrieve an object into valid json
- update `__init__.py` to import this file

- `GET /api/v1/states` retrieves the list of all states
- `GET /api/v1/states/<state_id>` retrieves the matching `State` object
	- if no match found raise `404`
- `DELETE /api/v1/states/<state_id>` deletes the matching `State` object
	- if successful, return an empty dictionary along with the status code `200`
	- if no match found raise `404`
- `POST /api/v1/states` create a `State` object
	- use `request.get_json` from Flask to transform the http body request
	  to a dictionary
	- if invalid json is provided raise a `400` error with the message
	  `Not a JSON`
	- if the key `name` isn't provided raise a `400` error with the message
	  `Missing name`
	- if successful return a new `State` with the status code `201`
- `PUT /api/v1/states/<state_id>` updates a `State` object
	- if `state_id` is invalid raise `404` error
	- use `request.get_json` from flask to transform the http body request to
	  dictionary
	- if the http body is not valid json raise a `400` error with the message
	  `Not a JSON`
	- update the `State` object with all key-value pairs of the dictionary
	- ignore the keys: `id`, `created_at`, and `updated_at`
	- return the `State` object with the code `200`

## 8. city

`api/v1/views/cities.py`
`api/v1/views/__init__.py`

in `api/v1/views/cities.py` :
- use `to_dict()` to retrieve an object into valid json
- update `__init__.py` to import this file

### restful api

- `GET /api/v1/states/<state_id>/cities` retrieves all cities of the given
  state object
	- if the `state_id` is in valid raise `404` error
- `GET /api/v1/cities/<city_id>` retrieves the matching `City` object
- `DELETE /api/v1/cities/<city_id>` deletes the matching `City` object from
  storage
- `POST /api/v1/states/<state_id>/cities` creates a new city for state
- `PUT /api/v1/cities/<city_id>` update the matching `City` object from

## 9. amenity

`api/v1/views/amenities.py`
`api/v1/views/__init__.py`

in `api/v1/views/amenities.py` :
- use `to_dict()` to retrieve an object into valid json
- update `__init__.py` to import this file

### restful api

- `GET /api/v1/amenities` retrieves all amenities
- `GET /api/v1/amenities/<amenity_id>` retrieves the given amenity
- `DELETE /api/v1/amenities/<amenity_id>` deletes the matching amenity from
  storage
- `POST /api/v1/amenities` creates and stores a new instance of `Amenity`
- `PUT /api/v1/amenities/<amenity_id>` update the matching amenity object

## 10. user

`api/v1/views/users.py`
`api/v1/views/__init__.py`

in `api/v1/views/users.py` :
- use `to_dict()` to retrieve an object into valid json
- update `__init__.py` to import this file

### restful api

- `GET /api/v1/users` retrieves all amenities
- `GET /api/v1/users/<user_id>` retrieves the given user
- `DELETE /api/v1/users/<user_id>` deletes the matching user from
  storage
- `POST /api/v1/users` creates and stores a new instance of `user`
- `PUT /api/v1/users/<user_id>` update the matching user object

## 11. place

`api/v1/views/places.py`
`api/v1/views/__init__.py`

in `api/v1/views/places.py` :
- use `to_dict()` to retrieve an object into valid json
- update `__init__.py` to import this file

### restful api

- `GET /api/v1/cities/<city_id>/places` retrieves all places of a given city
- `GET /api/v1/places/<place_id>` retrieves the given place
- `DELETE /api/v1/places/<place_id>` deletes the matching place from
  storage
- `POST /api/v1/cities/<city_id>/places` creates and stores a new instance of `place`
- `PUT /api/v1/places/<place_id>` update the matching places object

## 12. reviews

`api/v1/views/places_reviews.py`
`api/v1/views/__init__.py`

in `api/v1/views/reviews.py` :
- use `to_dict()` to retrieve an object into valid json
- update `__init__.py` to import this file

### restful api

- `GET /api/v1/places/<place_id>/reviews` retrieves all amenities
- `GET /api/v1/reviews/<reviews_id>` retrieves the given reviews
- `DELETE /api/v1/reviews/<reviews_id>` deletes the matching reviews from
  storage
- `POST /api/v1/places/<place_id/reviews` creates and stores a new instance of `reviews`
- `PUT /api/v1/reviews/<reviews_id>` update the matching reviews object

## 13. http access control (cors)

cross-origin http request is made when a resource request another resource from
a domain or port that is different from the one the first resource is hosted on

[definition of CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

this is needed because it allows a web client to make request on your api.
without correctly setup CORS, a web client wont be able to access the data

install `pip3 install flask_cors` and use the `CORS` class from the
module `flask_cors`

update `api/v1/app.py` and create a `CORS` instance allowing `/*` for `0.0.0.0`

this will be updated when the API is deployed to production
