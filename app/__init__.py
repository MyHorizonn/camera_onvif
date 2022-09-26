from flask import Flask
from onvif import ONVIFCamera, exceptions

mycam = None
try:
    mycam = ONVIFCamera('127.0.0.1', 80, 'admin', 'admin')
    print("camera connected")
except (exceptions.ONVIFError) as e:
    print("connect error")
def create_app():
    app = Flask(__name__)

    from .camera_ptz import camera_ptz as camera_ptz_blueprint
    app.register_blueprint(camera_ptz_blueprint)

    return app