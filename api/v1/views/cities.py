#!/usr/bin/python3
'''
a view for `City` objects that handles
all default RESTful API actions
'''

from api.v1.views.service_calls import *
from models.city import City
from models.state import State


@view_route('states/<state_id>/cities', 'POST')
def create_city(state_id):
    '''
    creates a new city object from the provided json
    if successful a json representation is returned
    '''
    return create_object_for(
        parent=State,
        child=City,
        required=['name'],
        parent_id={'state_id': state_id})


@view_route('states/<state_id>/cities', 'GET')
def get_cities(state_id):
    '''
    returns json list of all cities found for a given state
    '''
    return get_all_objects_from(State, state_id, 'cities')


@view_route('/cities/<city_id>', 'GET')
def get_city(city_id):
    '''
    returns json dict city found provided city_id
    if not such city exist 404 error is raised
    '''
    return get_single_object(City, city_id)


@view_route('/cities/<city_id>', 'PUT')
def update_city(city_id):
    '''
    updates the city object found via the city_id
    if not such city exist 404 error is raised
    '''
    return update_object(City, city_id)


@view_route('/cities/<city_id>', 'DELETE')
def delete_city(city_id):
    '''
    deletes the city object found via the city_id
    if not such city exist 404 error is raised
    '''
    return delete_object(City, city_id)
