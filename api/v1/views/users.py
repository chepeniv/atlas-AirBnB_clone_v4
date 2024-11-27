#!/usr/bin/python3
"""
Handles app_views for User class
"""
from api.v1.views.service_calls import *
from models.user import User


@view_route('/users', 'POST')
def create_user():
    ''' '''
    return create_object(user, required=['password', 'email'])


@view_route('/users', 'GET')
def get_all_users():
    ''' '''
    return get_all_objects(user)


@view_route('/users/<user_id>', 'GET')
def get_user(user_id):
    ''' '''
    return get_single_object(user, user_id)


@view_route('/users/<user_id>', 'PUT')
def update_user(user_id):
    ''' '''
    return update_object(user, user_id)


@view_route('/users/<user_id>', 'DELETE')
def delete_user(user_id):
    ''' '''
    return delete_object(user, user_id)
