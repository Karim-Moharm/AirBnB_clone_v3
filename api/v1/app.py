#!/usr/bin/python3
"""import libraries"""
from flask import Flask, Blueprint
from os import getenv
from models import storage
from api.v1.views import app_views
# sys.path.append('../..')

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    """close session"""
    storage.close()


# if __name__ == "__main__":
#     host = getenv("HBNB_API_HOST")
#     port = getenv("HBNB_API_PORT")
#     if not host:
#         host = "0.0.0.0"
#     if not port:
#         port = 5000
#     app.run(debug=True, host=host, port=port, threaded=True)

if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
