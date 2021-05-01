#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models import State


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list')
def states_list():
    """ returns html page with states list """
    db = storage.all(State).values()
    return render_template('7-states_list.html', db=db)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
