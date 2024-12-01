# Atlas AirBnB v4

## 0. last clone

- `README.md`
	- [ ] update authors
	- [ ] update description

## 1. cash only

write a script that starts a Flask web app\
this task is based on `web_flask`

- `web_flask/__init__.py`
- `web_flask/100-hbnb.py` --> `0-hbnb.py`
- `web_flask/templates/100-hbnb.html` --> `0-hbnb.html`
- `web_flask/static/*`

- [ ] copy and rename needed files from `web_flask`
- [ ] in `0-hbnb.py` replace the exist route to `/0-hbnb/`
- [ ] prevent asset caching done by flask
	- [ ] add a query string to each asset
	- [ ] add variable `cache_id` with a `uuid4()` value to `render_template`
	- [ ] in `0-hbnb.html` add this same `uuid4()` value to each `<link>`
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

- [ ] in `1-hbnb.py` replace the route `0-hbnb` with `1-hbnb`
- [ ] update `1-hbnb.html`
	- [ ] import jquery and `static/scripts/1-hbnb.js` in the `<head>` tag
	- [ ] add `<input type="checkbox">` to each amenity `<li>`
		- [ ] checkbox must be 10px to the left of the amenity name
	- [ ] for each `input` tag of amenities
		- [ ] add `data-id":amenity_id`
		- [ ] add `data-name":amenity_name`
- [ ] write `static/scripts/1-hbnb.js`
	- [ ] must be executed only when the dom is loaded
	- [ ] must use jquery
	- [ ] listen to changes on each input checkbox
		- [ ] if the checkbox is checked, store the amenity id in a variable
		- [ ] if the checkbox is unchecked, remove the amenity id from a variable
		- [ ] update the `h4` tag inside the `div` amenities with the list of
			  checked amenities

## 3. api status

- `api/v1/app.py`
- `web_dynamic/2-hbnb.py`
- `web_dynamic/templates/2-hbnb.html`
- `web_dynamic/static/styles/3-header.css`
- `web_dynamic/static/scripts/2-hbnb.js`

## 4. fetch places

- `web_dynamic/3-hbnb.py`
- `web_dynamic/templates/3-hbnb.html`
- `web_dynamic/static/scripts/3-hbnb.js`

## 5. filter places by amenity

- `web_dynamic/4-hbnb.py`
- `web_dynamic/templates/4-hbnb.html`
- `web_dynamic/static/scripts/4-hbnb.js`
