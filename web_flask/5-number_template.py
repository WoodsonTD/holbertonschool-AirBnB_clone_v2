#!/usr/bin/python3
"""add a route"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def displayC(text):
    return "C " + text.replace("_", " ")


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def displayPython(text='is cool'):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def nisnumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def displaytemplate(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
