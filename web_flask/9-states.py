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


@app.route("/states", strict_slashes=False)
def all_states():
    '''
    serves a template that displays all State objects by name in alphabetical
    order
    '''
    states = storage.all(State).values()
    states = list(states)
    if len(states) > 0:
        return render_template("9-states.html", states=states, single=False)
    else:
        abort(404)


# determine how a state with no cities should be displayed
@app.route("/states/<idnum>", strict_slashes=False)
def state_by_id(idnum):
    '''
    serves a template that displays a single State denoted by its id as well as
    all of its cities in alphabetical order
    '''
    states = storage.all(State).values()

    state = None
    for s in states:
        if s.id == idnum:
            state = s
            break

    if state is not None:
        return render_template("9-states.html", states=[state], single=True)
    else:
        return render_template("9-states.html", states=[], single=False)

@app.teardown_appcontext
def close_database(self):
    '''
    close the database after each serve
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
