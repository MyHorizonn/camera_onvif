from flask import (
    Flask,
    request,
    jsonify,
    render_template
)
from . import camera_ptz
from .. import mycam

XMAX = 1
XMIN = -1
YMAX = 1
YMIN = -1

ptz = None
media = None
media_profile = None
request = None
ptz_configuration_options = None
moverequest = None

if mycam != None:
    ptz = mycam.create_ptz_service()
    media = mycam.create_media_service()
    active = False
    media_profile = media.GetProfiles()[0]
    request = ptz.create_type('GetConfigurationOptions')
    request.ConfigurationToken = media_profile.PTZConfiguration.token
    ptz_configuration_options = ptz.GetConfigurationOptions(request)

@camera_ptz.route('/')
def main():
    return render_template('index.html')


@camera_ptz.route('/up', methods=['POST'])
def move_up():
    print('up')
    if mycam != None:
        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        global XMAX, XMIN, YMAX, YMIN
        XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

        print ('move up...')
        moverequest.Velocity.PanTilt.x = 0
        moverequest.Velocity.PanTilt.y = YMAX

        global active
        if active:
            ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = True
        ptz.ContinuousMove(moverequest)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/stop', methods=['POST'])
def stop():
    if mycam != None:
        global active
        media_profile = media.GetProfiles()[0]
        request = ptz.create_type('GetConfigurationOptions')
        request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz.Stop({'ProfileToken': request.ProfileToken})
        active = False
        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404