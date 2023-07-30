from flask import Flask,  Blueprint
from controllers.auth import login
from controllers.addUsuario import addUsuario
from controllers.getFile import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello  Flask!'


api = Blueprint('api', __name__)

api.route("/login")(login)
api.route("/addUsuario")(addUsuario)
api.route("/getThumbnails")(getThumbnails)
api.route("/getVideos")(getVideos)


app.register_blueprint(api, url_prefix='/')

if __name__ == '__main__':
    app.run(port=81)
