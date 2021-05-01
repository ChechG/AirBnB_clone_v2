#!/usr/bin/python3
""" Script that starts Flask web application """
from flask import Flask, render_template
from models import storage
from models import State
from uuid import UUID

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def st_ci_list(id=None):
    """ returns html page of state with cities list """
    cit = storage.all(State)
    states = cit.values()
    if id == None:
        return render_template('9-states.html', states=states, id=id)
    else:
        ej = 'State.' + str(id)
        if ej in cit:
            return render_template('9-states.html', cit=cit, ej=ej, id=id)
        else:
            return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
