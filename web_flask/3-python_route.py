"""
from the route we display the value assigned to the text variable
and assign a default value of "is cool"
"""
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


 @app.route("/python", strict_slashes=False)
 @app.route("/python/<text>", strict_slashes=False)
 def python(text="is cool"):
     """ returns value assigned to the text variable """
     return f"Python {escape(text).replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
