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


@app.route('/number/<int:n>')
def py_int(n):
    """ returns variable string """
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def n_temp(n):
    """ returns html page if int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def n_odd_even(n):
    """ returns html page if int odd/even"""
    if n % 2 == 0:
        o = "even"
    else:
        o = "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd=o)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
