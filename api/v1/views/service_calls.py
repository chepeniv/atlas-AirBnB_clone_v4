#!/usr/bin/python3
'''
definition of functions used to process RESTful api request
'''

from models import storage
from flask import abort, request
from api.v1.views import app_views


def view_route(*params):
    '''
    decorator simplifying the implementation of another decorator
    '''
    route = params[0]
    call = params[1]

    def inner(func):
        '''
        application of decorator app_views.route to function
        '''
        func = (app_views.route(
            route,
            methods=[call],
            strict_slashes=False))(func)
    return inner


def get_all_objects(model_class):
    '''
    returns json list of all objects of a given type found in storage
    '''
    objects = storage.all(model_class)
    json_objects = []
    for obj in objects.values():
        json_objects.append(obj.to_dict())
    return json_objects


def get_all_objects_from(ParentClass, parent_id, children):
    '''
    returns json list of all objects belonging to the given parent
    '''
    parent = storage.get(ParentClass, parent_id)
    if parent:
        children = getattr(parent, children)
        json_children = []
        for child in children:
            json_children.append(child.to_dict())
        return json_children
    else:
        abort(404)


def get_single_object(model_class, obj_id):
    '''
    returns json dict city found provided city_id
    if not such city exist 404 error is raised
    '''
    obj = storage.get(model_class, obj_id)
    if obj:
        obj = obj.to_dict()
        return obj
    else:
        abort(404)


def delete_object(model_class, obj_id):
    '''
    deletes the object found via the obj_id
    if not such object exist 404 error is raised
    '''
    obj = storage.get(model_class, obj_id)
    if obj:
        obj.delete()
        storage.save()
        return {}, 200
    else:
        abort(404)


def create_object(model_class, required):
    '''
    creates a new object from the provided json
    if successful a json representation is returned
    '''
    if not request.is_json:
        abort(400, "Not a JSON")

    json_data = request.get_json()
    for key in required:
        if key not in json_data.keys():
            abort(400, f"Missing {key}")

    new_obj = model_class(**json_data)
    if new_obj:
        storage.new(new_obj)
        storage.save()
        return new_obj.to_dict(), 201


def create_object_for(
        parent=None,
        child=None,
        required=None,
        parent_id=None):
    '''
    creates a new object from the provided json
    if successful a json representation is returned
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    parent_id_value = parent_id.values()
    parent_id_value = list(parent_id_value)
    parent_id_value = parent_id_value[0]
    parent = storage.get(parent, parent_id_value)
    if not parent:
        abort(404)

    json_data = request.get_json()
    json_data.update(parent_id)

    for key in required:
        if key not in json_data.keys():
            abort(400, f"Missing {key}")

    new_obj = child(**json_data)
    if new_obj:
        storage.new(new_obj)
        storage.save()
        return new_obj.to_dict(), 201


def update_object(model_class, obj_id):
    '''
    updates the object found via the obj_id
    if not such object exist 404 error is raised
    '''
    if not request.is_json:
        return "Not a JSON", abort(400)

    json_data = request.get_json()
    obj = storage.get(model_class, obj_id)
    if obj:
        for key, value in json_data.items():
            if (key not in {'id', 'created_at', 'updated_at'}
                    and hasattr(obj, key)):
                setattr(obj, key, value)
        storage.save()
        return obj.to_dict(), 200
    else:
        abort(404)
