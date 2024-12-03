#!/usr/bin/python3
"""
Handles app_views for Place class
"""
from api.v1.views.service_calls import *
from models.city import City
from models.place import Place

@view_route('/places_search', 'POST')
def search_places():
    '''
    retrieves places based on given json object
    '''
    #### DESC: ####
    #
    # json keys states, cities, amenties
    #
    #### LOGIC: ####
    #
    # extract given json
    # if json invalid
    #       return 400 with message 'Not a JSON'
    #
    # if json is empty (or all keys are empty)
    #       get and return all places
    #
    # declare data structure with only unique items all_cities
    # or call method on it later to remove duplicates
    #
    # add every city from each state to all_cities
    # add cities explicitly given to all_cities as well
    #
    # declare all_places
    # if all_cities is not empty
    #       for each city fetch places and add to all_places
    # else add all places to all_places
    #
    # declare filtered_places
    # iterate through each place in all_places
    #       if no amenity, from amenities given, is absent in place
    #       add to filtered_places
    # return filtered_places
    pass


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
    return get_all_objects_from(City, city_id, 'cities')


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
