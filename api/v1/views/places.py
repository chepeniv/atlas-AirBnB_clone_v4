#!/usr/bin/python3
"""
Handles app_views for Place class
"""
from api.v1.views.service_calls import *
from models.state import State
from models.city import City
from models.place import Place


def extract_id(item):
    return item['id']

@view_route('/places_search', 'POST')
def search_places():
    '''
    retrieves places based on a given json object of the form
    { states: [state_ids], cities: [city_ids], amenities: [amenity_ids]}
    '''
    # if json is invalid this should abort the entire call
    data = extract_json()

    # if all keys are empty then flow of logic should still return all places
    if data == {}:
        return get_all_objects(Place)

    given_cities = data.get('cities')
    given_states = data.get('states')
    given_amenities = data.get('amenities')

    all_cities = set()          # city_ids
    all_places = set()          # Place.to_dict()'s
    filtered_places = list()    # Place.to_dict()'s

    if given_cities is not None:
        all_cities.update(set(given_cities))

    if given_states is not None:
        for state_id in given_states:
            state_cities = get_all_objects_from(State, state_id, 'cities')
            state_cities = map(extract_id, state_cities)
            all_cities.update(set(state_cities))

    if len(all_cities) > 0:
        for city_id in all_cities:
            city_places = get_places(city_id)
            all_places.update(set(city_places))
    else:
        all_places = get_all_objects(Place)

    if given_amenities is not None:
        given_amenities = set(given_amenities)
        for place in all_places:
            place_amenities = get_all_objects_from(
                Place,
                place.get('id'),
                'amenities')
            place_amenities = set(map(extract_id, place_amenities))
            if given_amenities.issubset(place_amenities):
                filtered_places.append(place)
    else:
        filtered_places = list(all_places)

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
            'user_id',
            'description',
            'number_rooms',
            'number_bathrooms',
            'max_guest',
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
    return get_single_object(Place, place_id)


@view_route('/places/<place_id>', 'PUT')
def update_place(place_id):
    '''
    updates the place object found via the place_id
    if not such place exist 404 error is raised
    '''
    return update_object(Place, place_id)


@view_route('/places/<place_id>', 'DELETE')
def delete_place(place_id):
    '''
    deletes the place object found via the place_id
    if not such place exist 404 error is raised
    '''
    return delete_object(Place, place_id)
