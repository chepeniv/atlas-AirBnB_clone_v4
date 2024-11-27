#!/usr/bin/python3
''' '''
from api.v1.views.service_calls import *
from models.amenity import Amenity


@view_route('/amenities', 'POST')
def create_amenity():
    ''' '''
    return create_object(Amenity, required=['name'])


@view_route('/amenities', 'GET')
def get_all_amenities():
    ''' '''
    return get_all_objects(Amenity)


@view_route('/amenities/<amenity_id>', 'GET')
def get_amenity(amenity_id):
    ''' '''
    return get_single_object(Amenity, amenity_id)


@view_route('/amenities/<amenity_id>', 'PUT')
def update_amenity(amenity_id):
    ''' '''
    return update_object(Amenity, amenity_id)


@view_route('/amenities/<amenity_id>', 'DELETE')
def delete_amenity(amenity_id):
    ''' '''
    return delete_object(Amenity, amenity_id)
