#!/usr/bin/python3
'''
definitions and import for the flask app
'''

from flask import Blueprint
from models import storage
from models.engine import valid_models

app_views = Blueprint('views', __name__, url_prefix='/api/v1')
storage = storage
valid_models = valid_models

from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.index import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.states import *
from api.v1.views.users import *
