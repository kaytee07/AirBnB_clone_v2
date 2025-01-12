#!/usr/bin/python3
"""
from the route we display the value assigned to the text variable
and assign a default value of "is cool"
"""
from flask import Flask, escape, render_template
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ returns value assigned to the text variable """
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """check if variable part is a number and return it"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """render an html file"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """return URL variable if integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
