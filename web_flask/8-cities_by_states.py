#!/usr/bin/python3
'''
task 9 - cities by states
'''

import sys
sys.path.append('../')
from models import storage, storage_type
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_all_states():
    '''
    serves a template that displays all State objects by name in alphabetical
    order
    '''
    states = storage.all(State).values()
    states = list(states)
    if len(states) > 0:
        return render_template("8-cities_by_states.html", states=states)
    else:
        abort(404)


@app.teardown_appcontext
def close_database(self):
    '''
    close the database after each serve
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
