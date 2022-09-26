from flask import Blueprint

camera_ptz = Blueprint('camera_ptz', __name__)

from . import routes