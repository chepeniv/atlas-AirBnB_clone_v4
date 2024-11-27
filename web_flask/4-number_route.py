#!/usr/bin/python3
'''
task 4 - python is cool

- application should be listening to 0.0.0.0:5000
- use the option 'strict_slashes=False' within the route definitions
- route '/' should display 'Hello HBNB!'
- route '/hbnb' should display 'HBNB'
- route '/c/<text>' should display 'C' followed by the value of <text>
    (replace underscores with spaces)
- route '/python/<text>' should display 'Python' followed by the value of
    <text> with default value "is cool" (replace underscores with spaces)
- route '/number/<n>' should display '<n> is a number' only if <n> is an
    integer
'''

from flask import Flask, abort
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    '''
    process the given url and serve the resulting text on route /python/<text>
    '''
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    '''
    process the given url and output the result on route /number/<n>
    '''
    if n.isdecimal():
        n = int(n)
        return f"{n} is a number"
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
