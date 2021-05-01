#!/usr/bin/python3
""" Script that starts Flask web application """
from flask import Flask, render_template
from models import storage
from models import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states')
def st_list():
    """ returns html page with states list """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<uuid:id>')
def st_ci_list(id):
    """ returns html page of state with cities list """
    ej = 'State.' + str(id)
    cities = storage.all(State)
    return render_template('9-states.html', cities=cities, ej=ej)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
