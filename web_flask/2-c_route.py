#!/usr/bin/python3
'''
task 2 - c is fun

- application should be listening to 0.0.0.0:5000
- use the option 'strict_slashes=False' within the route definition
- route '/' should display 'Hello HBNB!'
- route '/hbnb' should display 'HBNB'
- route '/c/<text>' should display 'C' followed by the value of <text>
    (replace underscores with spaces)
'''

from flask import Flask
from markupsafe import escape

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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''
    process the given url and serve the resulting text on route /c/<text>
    '''
    text = text.replace("_", " ")
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
