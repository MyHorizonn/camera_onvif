from flask import Flask


def create_app():
    app = Flask(__name__)

    from .camera_ptz import camera_ptz as camera_ptz_blueprint
    app.register_blueprint(camera_ptz_blueprint)

    return app