#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
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

@app.route('/number/<n>')
def py_int(n):
    """ returns variable string """
    if n.isdigit() is True:
        return "%s is a number" % n

@app.route('/number_template/<n>')
def n_temp(n):
    """ returns html page """
    if n.isdigit() is True:
        return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
