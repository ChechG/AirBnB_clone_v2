#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


list_states = storage.all(State).values()
for i in list_states:
    print(i.id)
    print(i.name)



