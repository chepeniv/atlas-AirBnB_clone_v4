#!/usr/bin/python3
'''
task 0 - hello flask!

- application should be listening to 0.0.0.0:5000
- route '/' should display 'Hello HBNB'
- use the option 'strict_slashes=False' within the route definition
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''
    output text, upon request, to 0.0.0.0:5000
    '''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
