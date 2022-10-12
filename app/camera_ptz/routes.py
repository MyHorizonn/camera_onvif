from flask import (
    Flask,
    request,
    jsonify,
    render_template
)
from . import camera_ptz
from onvif import ONVIFCamera, exceptions

active = False
moverequest = None

@camera_ptz.route('/')
def main():
    return render_template('index.html')

@camera_ptz.route('/zoom_down', methods=['POST'])
def zoom_down():
    print('zoom down')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        cam_request = ptz.create_type('GetConfigurationOptions')
        cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)

        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        print ('zooming. down..')
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI
        moverequest.Velocity.PanTilt.x = 0
        moverequest.Velocity.PanTilt.y = 0
        moverequest.Velocity.Zoom.x = -1.0

        print(moverequest)
        
        print(moverequest.Velocity.Zoom)

        global active
        if active:
            ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = True
        ptz.ContinuousMove(moverequest)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/zoom_up', methods=['POST'])
def zoom_up():
    print('zoom up')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        cam_request = ptz.create_type('GetConfigurationOptions')
        cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)

        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        print ('zooming up...')
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI
        moverequest.Velocity.PanTilt.x = 0
        moverequest.Velocity.PanTilt.y = 0
        moverequest.Velocity.Zoom.x = 1.0
        
        print(moverequest.Velocity.Zoom)

        global active
        if active:
            ptz.Stop({'ProfileToken': moverequest.ProfileToken})
        active = True
        ptz.ContinuousMove(moverequest)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404


@camera_ptz.route('/up', methods=['POST'])
def move_up():
    print('up')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        cam_request = ptz.create_type('GetConfigurationOptions')
        cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)

        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max

        print ('move up...')
        moverequest.Velocity.PanTilt.x = 0
        moverequest.Velocity.PanTilt.y = YMAX / 2
        moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
        moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI

        print(moverequest.Velocity.Zoom)

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
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        cam_request = ptz.create_type('GetConfigurationOptions')
        cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)
        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

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
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        cam_request = ptz.create_type('GetConfigurationOptions')
        cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)
        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min

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
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        cam_request = ptz.create_type('GetConfigurationOptions')
        cam_request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = ptz.GetConfigurationOptions(cam_request)
        global moverequest
        moverequest = ptz.create_type('ContinuousMove')
        moverequest.ProfileToken = media_profile.token
        if moverequest.Velocity is None:
            moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max

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
    print('stop')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
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
    print('set_presets')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        token = ptz.SetPreset({'ProfileToken': media_profile.token})
        print(token)
        return jsonify({'token': token}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/select_preset', methods=['POST'])
def select_preset():
    print('select_presets')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        ptz.GotoPreset({'ProfileToken': media_profile.token, 'PresetToken': int(cam_info['preset'])})
        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/get_presets', methods=['POST'])
def get_presets():
    print('get_presets')
    data = request.json
    if data is None:
        data = request.form.to_dict()
    cam_info = data['data']
    print(cam_info)
    mycam = None
    try:
        mycam = ONVIFCamera(cam_info['cam_ip'], int(cam_info['port']), cam_info['username'], cam_info['password'])
        print("camera connected")
    except (exceptions.ONVIFError) as e:
        print("connect error")
    if mycam != None:
        ptz = mycam.create_ptz_service()
        media = mycam.create_media_service()
        media_profile = media.GetProfiles()[0]
        presets = ptz.GetPresets({'ProfileToken': media_profile.token})
        return jsonify(presets), 200
    return jsonify({'msg': 'err'}), 404