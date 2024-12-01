#!/usr/bin/python3
'''
the entry point of the api_v1 app for airbnb
'''

import os
from api.v1.views import app_views, storage
from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.register_blueprint(app_views)
cors_setup = CORS(app, send_wildcard=True, origins=["0.0.0.0"])


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
    storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')
    storage_mode = os.environ.get('HBNB_ENV', 'json')
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
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = os.environ.get('HBNB_API_PORT', 5000)
    app.run(
        host=host,
        port=port,
        threaded=True
        # ssl_context='adhoc'
    )
