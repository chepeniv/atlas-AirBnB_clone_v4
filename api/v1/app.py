#!/usr/bin/python3
'''
the entry point of the api_v1 app for airbnb
'''

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.register_blueprint(app_views)
cors_setup = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# @cross_origin(send_wildcard=True)
@app.route("/", strict_slashes=False)
def landing_page():
    '''
    returns a welcome message to ensure that
    the flask server is working as expected
    '''
    return render_template('welcome.html')


@app.route("/storage", strict_slashes=False)
def storage_info():
    '''
    returns information about the storage
    type and mode currently being used
    '''
    storage_type = environ.get('HBNB_TYPE_STORAGE', 'file')
    storage_mode = environ.get('HBNB_ENV', 'json')
    storage_info = {"type": storage_type, "mode": storage_mode}
    return storage_info


@app.teardown_appcontext
def close_database(self):
    '''
    close the database after each serve
    '''
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """
    handles all 404 errors to return a json 404 file
    """
    return make_response(jsonify({"error": "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"
    app.run(
        host=host, port=port, threaded=True)
