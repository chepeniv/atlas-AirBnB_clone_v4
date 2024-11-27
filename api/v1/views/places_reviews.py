#!/usr/bin/python3
''' '''
from api.v1.views.service_calls import *
from models.review import Review
from models.place import Place


@view_route('/reviews/<review_id>', 'GET')
def get_review(review_id):
    ''' '''
    return get_single_object(Review, review_id)


@view_route('/reviews/<review_id>', 'PUT')
def update_review(review_id):
    ''' '''
    return update_object(Review, review_id)


@view_route('/reviews/<review_id>', 'DELETE')
def delete_review(review_id):
    ''' '''
    return delete_object(Review, review_id)


@view_route('places/<place_id>/reviews', 'GET')
def get_reviews_from(place_id):
    '''
    returns json list of all cities found for a given state
    '''
    return get_all_objects_from(Place, place_id, 'reviews')


@view_route('places/<place_id>/reviews', 'POST')
def create_review(place_id):
    ''' '''
    # the validity of 'user_id' has not been verified here
    return create_object_for(
        parent=Place,
        child=Review,
        required=['text', 'user_id'],
        parent_id={'place_id': place_id})
