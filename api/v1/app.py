#!/usr/bin/python3


import sys

from flask import Flask, Blueprint
from os import getenv
from models import storage
from api.v1.views import app_views
# sys.path.append('../..')

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = 5000
    app.run(debug=True, host=host, port=port, threaded=True)
