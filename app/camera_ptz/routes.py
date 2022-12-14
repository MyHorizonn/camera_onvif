from flask import (
    Flask,
    request,
    jsonify,
    render_template
)
from . import camera_ptz
from onvif import ONVIFCamera, exceptions
import json

active = False
moverequest = None


@camera_ptz.route('/')
def main():
    return render_template('index.html')

@camera_ptz.route('/get_status', methods=['POST'])
def get_status():
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
        req = ptz.create_type("GetStatus")
        req.ProfileToken = media_profile.token
        resp = ptz.GetStatus(req)

        print(resp)
        return jsonify({"msg": "ok"}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/focus_auto', methods=['POST'])
def focus_auto():
    print('focus auto')
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

        imaging = mycam.create_imaging_service()
        media = mycam.create_media_service()
        video_sources = media.GetVideoSources()[0]

        focus_request = imaging.create_type('SetImagingSettings')
        focus_request.VideoSourceToken = video_sources.token
        focus_request.ImagingSettings = {
            'Focus':{
                'AutoFocusMode': 'AUTO'
            }
        }
        imaging.SetImagingSettings(focus_request)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404

@camera_ptz.route('/focus_stop', methods=['POST'])
def focus_stop():
    print('focus stop')
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
        imaging = mycam.create_imaging_service()
        media = mycam.create_media_service()
        video_sources = media.GetVideoSources()[0]

        # stop focus
        imaging.Stop(video_sources.token)

        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404


@camera_ptz.route('/focus_plus', methods=['POST'])
def focus_plus():
    print('focus +')
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
        
        imaging = mycam.create_imaging_service()
        media = mycam.create_media_service()
        video_sources = media.GetVideoSources()[0]

        # ???????????? ??????????
        focus_request = imaging.create_type('SetImagingSettings')
        focus_request.VideoSourceToken = video_sources.token
        focus_request.ImagingSettings = {
            'Focus':{
                'AutoFocusMode': 'MANUAL'
            }
        }
        imaging.SetImagingSettings(focus_request)

        # stop focus
        imaging.Stop(video_sources.token)

        # ??????????
        move_request = imaging.create_type('Move')
        move_request.VideoSourceToken = video_sources.token
        move_request.Focus = {
                'Continuous':{
                    'Speed': 7.0
                }
            }
        #print(move_request)
        imaging.Move(move_request)


        return jsonify({'msg': 'ok'}), 200
    return jsonify({'msg': 'err'}), 404


@camera_ptz.route('/focus_minus', methods=['POST'])
def focus_minus():
    print('focus -')
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
        
        imaging = mycam.create_imaging_service()
        media = mycam.create_media_service()
        video_sources = media.GetVideoSources()[0]

        # ???????????? ??????????
        focus_request = imaging.create_type('SetImagingSettings')
        focus_request.VideoSourceToken = video_sources.token
        focus_request.ImagingSettings = {
            'Focus':{
                'AutoFocusMode': 'MANUAL'
            }
        }
        imaging.SetImagingSettings(focus_request)

        # stop focus
        imaging.Stop(video_sources.token)

        # ??????????
        move_request = imaging.create_type('Move')
        move_request.VideoSourceToken = video_sources.token
        move_request.Focus = {
                'Continuous':{
                    'Speed': -7.0
                }
            }
        #print(move_request)
        imaging.Move(move_request)

        '''
        'Focus': {
            'AutoFocusMode': 'MANUAL',
            'DefaultSpeed': 1.0,
            'NearLimit': 100.0,
            'FarLimit': 0.0,
            '_value_1': None,
            '_attr_1': None
        }

        '''

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
        moverequest.Velocity.Zoom.x = 0.0

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
        moverequest.Velocity.Zoom.x = 0.0

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
        moverequest.Velocity.Zoom.x = 0.0

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
        moverequest.Velocity.Zoom.x = 0.0

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