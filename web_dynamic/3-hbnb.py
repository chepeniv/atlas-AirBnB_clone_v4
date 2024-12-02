#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.amenity import Amenity
from uuid import uuid4
from flask import Flask, abort, render_template

app = Flask(__name__)

# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    ''' Remove the current SQLAlchemy Session '''
    storage.close()


@app.route("/", strict_slashes=False)
def landing_page():
    '''
    returns a welcome message to ensure that
    the flask server is working as expected
    '''
    return render_template('welcome.html')


@app.route('/2-hbnb', strict_slashes=False)
def hbnb():
    ''' HBNB is alive! '''
    states = storage.all(State).values()
    states = list(states)
    amenities = storage.all(Amenity).values()
    amenities = list(amenities)

    return render_template('2-hbnb.html',
                           cache_id=uuid4(),
                           states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
