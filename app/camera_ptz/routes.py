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
cam_request = None
ptz_configuration_options = None
moverequest = None

if mycam != None:
    ptz = mycam.create_ptz_service()
    media = mycam.create_media_service()
    active = False
    media_profile = media.GetProfiles()[0]
    cam_request = ptz.create_type('GetConfigurationOptions')
    cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
    ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)

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

        print(XMAX, XMIN, YMAX, YMIN)

        print ('move up...')
        moverequest.Velocity.PanTilt.x = 0
        moverequest.Velocity.PanTilt.y = YMAX / 2
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        global active
        if active:
            ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = True
        ptz.ContinuousMove(moverequest)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404


@camera_ptz.route('/down', methods=['POST'])
def move_down():
    print('down')
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

        print(XMAX, XMIN, YMAX, YMIN)

        print ('move down...')
        moverequest.Velocity.PanTilt.x = 0
        moverequest.Velocity.PanTilt.y = YMIN / 2
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        global active
        if active:
            ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = True
        ptz.ContinuousMove(moverequest)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404


@camera_ptz.route('/left', methods=['POST'])
def move_left():
    print('left')
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

        print(XMAX, XMIN, YMAX, YMIN)

        print ('move left...')
        moverequest.Velocity.PanTilt.y = 0
        moverequest.Velocity.PanTilt.x = XMIN / 2
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        global active
        if active:
            ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = True
        ptz.ContinuousMove(moverequest)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404


@camera_ptz.route('/right', methods=['POST'])
def move_right():
    print('right')
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

        print ('move right...')
        moverequest.Velocity.PanTilt.y = 0
        moverequest.Velocity.PanTilt.x = XMAX / 2
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

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
        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = False
        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/set_preset', methods=['POST'])
def set_preset():
    if mycam != None:
        token = ptz.SetPreset({'ProfileToken': media_profile.token})
        print(token)
        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/select_preset', methods=['POST'])
def select_preset():
    if mycam != None:
        ptz.GotoPreset({'ProfileToken': media_profile.token, 'PresetToken': 1})
        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/get_presets', methods=['POST'])
def get_presets():
    if mycam != None:
        presets = ptz.GetPresets({'ProfileToken': media_profile.token})
        print(presets)
        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404