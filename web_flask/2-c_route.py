#!/usr/bin/python3
"""from the route we display the text in it"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ return C and whatever is in the text route """
    return f"C {escape(text).replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
