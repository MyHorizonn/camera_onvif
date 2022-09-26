from flask import Flask
from onvif import ONVIFCamera, exceptions

mycam = None
try:
    mycam = ONVIFCamera('192.168.2.42', 80, 'python', 'Qwert1234')
    print("camera connected")
except (exceptions.ONVIFError) as e:
    print("connect error")
def create_app():
    app = Flask(__name__)

    from .camera_ptz import camera_ptz as camera_ptz_blueprint
    app.register_blueprint(camera_ptz_blueprint)

    return app