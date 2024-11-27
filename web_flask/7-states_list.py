#!/usr/bin/python3
'''
task 8 - list of states
'''

import sys
sys.path.append('../')
from models import storage, storage_type
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


def by_name(state):
    '''
    function to indicate to .sort()
    '''
    return state.name


def get_sorted_states():
    '''
    returns a sorted list of value pairs containing a name and id each
    '''
    states_list = []
    states = storage.all(State).values()

    if len(states) == 0:
        return None

    for state in states:
        states_list.append(state)

    states_list.sort(key=by_name)
    return states_list


@app.route("/states_list", strict_slashes=False)
def list_all_states():
    '''
    serves a template that displays all State objects by name in alphabetical
    order
    '''
    states = get_sorted_states()
    if State:
        return render_template("7-states_list.html", states=states)
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
