# Atlas AirBnB v4

## 0. last clone

- `README.md`
	- [x] update authors
	- [ ] update description

## 1. cash only

write a script that starts a Flask web app\
this task is based on `web_flask`

- `web_flask/__init__.py`
- `web_flask/100-hbnb.py` --> `0-hbnb.py`
- `web_flask/templates/100-hbnb.html` --> `0-hbnb.html`
- `web_flask/static/*`

- [x] copy and rename needed files from `web_flask`
- [x] in `0-hbnb.py` replace the exist route to `/0-hbnb/`
- [x] prevent asset caching done by flask
	- [x] add a query string to each asset
	- [x] add variable `cache_id` with a `uuid4()` value to `render_template`
	- [x] in `0-hbnb.html` add this same `uuid4()` value to each `<link>`
		- example :
`<link
rel="stylesheet"
type="text/css"
href="../static/styles/4-common.css?e211c9eb-7d17-4f12-85eb-4d50fa50cb1d"
/>`

## 2. select amenities

make the filters section dynamic

- `1-hbnb.py`
- `templates/1-hbnb.html`
- `static/scripts/1-hbnb.js`

- [x] in `1-hbnb.py` replace the route `0-hbnb` with `1-hbnb`
- [x] update `1-hbnb.html`
	- [x] import jquery and `static/scripts/1-hbnb.js` in the `<head>` tag
	- [x] add `<input type="checkbox">` to each amenity `<li>`
		- [x] checkbox must be 10px to the left of the amenity name
	- [x] for each `input` tag of amenities
		- [x] add `data-id=":amenity_id"`
		- [x] add `data-name=":amenity_name"`

- [x] write `static/scripts/1-hbnb.js`
	- [x] must be executed only when the dom is loaded
	- [x] must use jquery
	- [x] listen to changes on each input checkbox
		- [x] if the checkbox is checked, store the amenity id in a variable
		- [x] if the checkbox is unchecked, remove the amenity id from a variable
		- [x] update the `h4` tag inside the `div` amenities with the list of
			  checked amenities

## 3. api status

- `api/v1/app.py`
- `web_dynamic/2-hbnb.py`
- `web_dynamic/templates/2-hbnb.html`
- `web_dynamic/static/styles/3-header.css`
- `web_dynamic/static/scripts/2-hbnb.js`

- [x] update `app.py`
	- [x] replace `CORS(app, origins="0.0.0.0")` with
		  `CORS(app, resources={r"/api/v1/*": {"origins": "*"}})`

- [x] create duplicate `2-hbnb.py`
	- [x] update route to `2-hbnb`

- [x] create duplicate `2-hbnb.html`
	- [x] replace js import to `2-hbnb.js` in `<head>`
	- [x] in `<header>` add new `<div>`
		- [x] attribute id should be `api_status`
		- [x] align to the right
		- [x] circle of 40px diameter
		- [x] center vertically
		- [x] at 30px of the right border
		- [x] background color #cccccc

		- [x] for this new element add the class `available` to `3-header.css`
			- [x] background color #ff545f

- [x] create duplicate `2-hbnb.js`
	- [x] request `http://0.0.0.0:5001/api/v1/status`
		- [x] if 'OK' add the class `available` to `div#api_status`
		- [x] remove the class `available` from `div#api_status`

start the api on port 5001:
```sh
HBNB_MYSQL_USER=hbnb_dev \
HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_TYPE_STORAGE=db \
HBNB_API_PORT=5001 \
python3 -m api.v1.app
```

## 4. fetch places

- `web_dynamic/3-hbnb.py`
- `web_dynamic/templates/3-hbnb.html`
- `web_dynamic/static/scripts/3-hbnb.js`

- [x] create duplicate `3-hbnb.js`
	- [x] replace route with `3-hbnb`

- [x] create duplicate `3-hbnb.html`
	- [x] replace import in `<head>` with `3-hbnb.js`
	- [x] "remove the entire jinja section of displaying all places" (`<article>`)

- [x] create duplicate `3-hbnb.js`
	- [x] request `http://0.0.0.0:5001/api/v1/places_search`
		- [x] construct this endpoint via the link provided (`places.py`)
		- [ ] send a `POST` request with `content-type: application/json` with an
			  empty dictionary in the body
		- `curl "http://0.0.0.0:5001/api/v1/places_search" -XPOST -H "Content-Type: application/json" -d '{}'`
		- [ ] loop through the result of the request and create an `<article>` tag
			  representing a `Place` in the `section.places` (the owner tag in the
			  place description may be removed)

places should now be loaded from the front-end instead of from the back-end

### 4.16 search

- [ ] update `api/v1/views/places.py`
	- [x] add endpoint `POST /api/v1/places_search` that retrieves all `Place`
		  objects dependant on the json body request
		- json may contain
			- `states`: list of `State` ids
			- `cities`: list of `Cities` ids
			- `amenities`: list of `Amenity` ids
		- search rules :
			- [x] if the http request body is not valid json, raise `400` error
				  with message `Not a JSON`
			- [x] if the json body is empty or each of the keys are empty,
				  retrieve all `Place` objects
			- [x] if `cities` list is not empty, include all `Place` for each city
				  id listed
			- [x] keys `cities` and `states` are related by set union
				- CAUTION: do not list `cities`'s `Places` items twice
			- [ ] if `amenities` list is not empty, limit search results ONLY to
				  `Place` objects that match ALL `Amenity` ids listed
				- this key relates to the others via set intersection

## 5. filter places by amenity

- `web_dynamic/4-hbnb.py` based an `3-hbnb.py`
- [x] replace route with `4-hbnb`

- `web_dynamic/templates/4-hbnb.html` based on `3-hbnb.html`
- [x] replace js import with `4-hbnb.js` in `<head>`

- `web_dynamic/static/scripts/4-hbnb.js` based on `3-hbnb.js`
- [ ] when `button` tag is clicked a new `POST` request is made to
	  `places_search` with the list of amenities checked
