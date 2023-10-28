#!/usr/bin/python3
"""import libraries"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.all_models import our_models


@app_views.route("/status")
def status():
    """returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """return json fromat of number of each objects by type
    """

    # json_format = jsonify({
    #     "amenities": storage.count(Amenity),
    #     "cities": storage.count(City),
    #     "places": storage.count(Place),
    #     "reviews": storage.count(Review),
    #     "states": storage.count(State),
    #     "users": storage.count(User)
    # })

    # return json_format

    json_format = jsonify({
        "amenities": storage.count(our_models['Amenity']),
        "cities": storage.count(our_models['City']),
        "places": storage.count(our_models['Place']),
        "reviews": storage.count(our_models['Review']),
        "states": storage.count(our_models['State']),
        "users": storage.count(our_models['User'])
    })

    return json_format
