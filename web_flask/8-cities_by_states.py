#!/usr/bin/python3
""" Script that starts Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ returns html page with states list """
    dbs = storage.all(State).values()
    return render_template('8-cities_by_states.html', dbs=dbs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
