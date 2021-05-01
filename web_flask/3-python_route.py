#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ returns string Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns string HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ returns variable string """
    if "_" in text:
        text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/<text>')
@app.route('/python/')
def py_text(text="is_cool"):
    """ returns variable string """
    if "_" in text:
        text = text.replace("_", " ")
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
