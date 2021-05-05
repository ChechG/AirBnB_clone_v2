#!/usr/bin/python3
""" Script that starts Flask web application """
from flask import Flask, render_template
from models import storage
from models import State, Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters')
def filters():
    states = storage.all(State).values()
    ame = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, ame=ame)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
