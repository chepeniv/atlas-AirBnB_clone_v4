# delegations

add more subtask for any issues that arise

## in progress

### top priority

- [ ] fix text display css issue with `.filters > div > h4`

### bottom priority

- [ ] implement no-caching for all indirectly loaded assets from the
	  stylesheets

## queue

## extra

- [ ] add a `required` list to the attributes of `BaseModel`
- [ ] implement `destroy all` in console for convenience
- [ ] reformat `data/7-states_list.sql`
- [ ] create `data/100-dump.txt` based on `data/100-dump.sql`

## completed

- [x] update `README.md` with instructions on how to setup and run the web app
- [x] create sql-reset sh-script
- [x] reformat `data/100-hbnb.sql` and rename to `data/100-dump.sql`

- [x] install `flasgger`

- [x] 0. (6pt) last clone --  `README.md`
	- [x] update authors

- [x] 1. (10pt) cash only
- `0-hbnb.py`
- `templates/0-hbnb.html`
	- [x] copy and rename needed files from `web_flask`
	- [x] in `0-hbnb.py` replace the exist route to `/0-hbnb/`

- [x] 2. (30pt) select amenities
 `1-hbnb.py`
- `templates/1-hbnb.html`
- `static/scripts/1-hbnb.js`

- [x] 3. (30pt) api status
- `api/v1/app.py`
- `web_dynamic/2-hbnb.py`
- `web_dynamic/templates/2-hbnb.html`
- `web_dynamic/static/styles/3-header.css`
- `web_dynamic/static/scripts/2-hbnb.js`

- [x] 4. (24pt) fetch places
- `web_dynamic/3-hbnb.py`
- `web_dynamic/templates/3-hbnb.html`
- `web_dynamic/static/scripts/3-hbnb.js`
- [x] `api/v1/views/places.py`
	- [x] complete `places.py def search_places()`

- [x] 5. (24pt) filter places by amenity
- `web_dynamic/4-hbnb.py`
- `web_dynamic/templates/4-hbnb.html`
- `web_dynamic/static/scripts/4-hbnb.js`