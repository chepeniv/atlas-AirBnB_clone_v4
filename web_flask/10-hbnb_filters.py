#!/usr/bin/python3
'''
task 10 - hbnb filters
'''

import sys
sys.path.append('../')
from models import storage, storage_type
from models.state import State
from models.amenity import Amenity
from flask import Flask, abort, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''
    homepage landing that redirects to hbnb_filters()
    '''
    return redirect(url_for('hbnb_filters'))


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    '''
    serves a template that displays a single State denoted by its id as well as
    all of its cities in alphabetical order
    '''
    states = storage.all(State).values()
    states = list(states)

    amenities = storage.all(Amenity).values()
    amenities = list(amenities)

    return render_template(
            "10-hbnb_filters.html",
            states=states,
            amenities=amenities)


@app.teardown_appcontext
def close_database(self):
    '''
    close the database after each serve
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
