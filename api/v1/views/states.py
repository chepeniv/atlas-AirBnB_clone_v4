#!/usr/bin/python3
'''
a view for `State` objects that handles
all default ESTful API actions
'''

from api.v1.views.service_calls import *
from models.state import State


# @app_views.route(
#     '/states',
#     methods=['GET'],
#     strict_slashes=False)
@view_route('/states', 'GET')
def get_states():
    '''
    returns json list of all states
    '''
    return get_all_objects(State)


@view_route('/states/<state_id>', 'GET')
def get_state(state_id):
    '''
    returns json dict state found provided state_id
    if not such state exist 404 error is raised
    '''
    return get_single_object(State, state_id)


@view_route('/states/<state_id>', 'DELETE')
def delete_state(state_id):
    '''
    deletes the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    return delete_object(State, state_id)


@view_route('/states', 'POST')
def create_state():
    '''
    creates a new state object from the provided json
    if successful a json representation is returned
    '''
    required = ['name']
    return create_object(State, required)


@view_route('/states/<state_id>', 'PUT')
def update_state(state_id):
    '''
    updates the state object found via the state_id
    if not such state exist 404 error is raised
    '''
    return update_object(State, state_id)
