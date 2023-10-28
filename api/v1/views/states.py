#!/usr/bin/python3
"""module for states routes
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort
from models.all_models import our_models
from models.state import State


@app_views.route('/states/', methods=['GET'])
def get_states():
    """return json format for states object
    """
    states_list = []
    for item in storage.all(State).values():
        states_list.append(item.to_dict())
    return jsonify(states_list)

@app_views.route("/api/v1/states/<state_id>", methods=['GET'])
def get_states_id(state_id):
    state = storage.get(State, state_id)
    return jsonify(state.to_dict())
