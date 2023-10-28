#!/usr/bin/python3
"""module for states routes
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
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


@app_views.route("/states/<state_id>", methods=['GET'])
def get_states_id(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_states_id(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({})


@app_views.route("/states/", methods=['POST'])
def post_states():
    if not request.get_json():
        abort(400, description="Not a JSON")
    if not 'name' in request.json:
        abort(400, description="Missing name")
    state = State(name=request.json['name'])
    storage.new(state)
    storage.save()
    return(jsonify(state.to_dict())), 201

@app_views.route("/states/<state_id>", methods=['PUT'])
def update_states(state_id):
    if not request.get_json():
        abort(400, description="Not a JSON")
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state_dict = state.to_dict()
    state_dict['name'] = request.json['name']
    storage.save()
    return jsonify(state_dict)

