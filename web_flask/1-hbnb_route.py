#!/usr/bin/python3
'''
task 1 - hbnb

- application should be listening to 0.0.0.0:5000
- route '/' should display 'Hello HBNB!'
- route '/hbnb' should display 'HBNB'
- use the option 'strict_slashes=False' within the route definition
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''
    serve text, upon request, to route /
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    serve text, upon request, to route /hbnb
    '''
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
