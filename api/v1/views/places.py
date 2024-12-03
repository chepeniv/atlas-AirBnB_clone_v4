#!/usr/bin/python3
"""
Handles app_views for Place class
"""
import json
from api.v1.views.service_calls import *
from models.state import State
from models.city import City
from models.place import Place


@view_route('/places_search', 'POST')
def search_places():
    '''
    retrieves places based on a given json object of the form
    { states: [state_ids], cities: [city_ids], amenities: [amenity_ids]}
    '''
    # if json is invalid this should abort the entire call
    data = extract_json();

    # or if all keys are empty
    if data.values() is None:
        return get_all_objects(Place)

    given_cities = data.get('cities')
    given_states = data.get('states')
    given_amenities = data.get('amenities')

    all_cities = set()
    all_places = set()
    filtered_places = list()

    if given_cities is not None:
        given_cities = set(given_cities)
        all_cities.union(given_cities)

    # change from city objects to only city_ids
    # use map ?
    if given_states is not None:
        for state_id in given_states:
            state_cities = get_all_objects_from(State, state_id, 'cities')
            state_cities = json.loads(state_cities)
            state_cities = set(state_cities)
            all_cities.union(state_cities)

    # change from place objects to only place_ids
    # use map ?
    if all_cities is not None:
        for city_id in all_cities:
            city_places = get_all_objects_from(City, city_id, 'places')
            city_places = json.loads(city_places)
            city_places = set(city_places)
            all_places.union(city_places)
    else:
        all_places = get_all_objects(Place)

    for place in all_places:
        for amenity_id in given_amenities:
            if amenity_id not in place.get('amenities'):

    #       [under construction]
    #       if no amenity, from amenities given, is absent in place
    #       add to filtered_places

    filtered_places = json.dumps(filtered_places)
    return filtered_places


@view_route('/cities/<city_id>/places', 'POST')
def create_place(city_id):
    '''
    creates a new city object from the provided json
    if successful a json representation is returned
    '''
    return create_object_for(
        parent=City,
        child=Place,
        required=[
            'name',
            'user_id'
            'description'
            'number_rooms'
            'number_bathrooms'
            'max_guest'
            'price_by_night'
        ],
        parent_id={'city_id': city_id})


@view_route('/cities/<city_id>/places', 'GET')
def get_places(city_id):
    '''
    returns json list of all places found for a given state
    '''
    return get_all_objects_from(City, city_id, 'places')


@view_route('/places/<place_id>', 'GET')
def get_place(place_id):
    '''
    returns json dict place found provided place_id
    if not such place exist 404 error is raised
    '''
    return get_single_object(place, place_id)


@view_route('/places/<place_id>', 'PUT')
def update_place(place_id):
    '''
    updates the place object found via the place_id
    if not such place exist 404 error is raised
    '''
    return update_object(place, place_id)


@view_route('/places/<place_id>', 'DELETE')
def delete_place(place_id):
    '''
    deletes the place object found via the place_id
    if not such place exist 404 error is raised
    '''
    return delete_object(place, place_id)
