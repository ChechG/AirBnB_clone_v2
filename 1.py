#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State, City


db_c = storage.all(City)
db_s = storage.all(State).values()
for i in db_s:
    print("{}: {}".format(i.id, i.name))
    for j in db_c:
        if db_c[j].state_id == i.id:
            print("\t{}: {}".format(db_c[j].id, db_c[j].name))
