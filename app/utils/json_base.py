#url_server_device = 'http://192.168.212.97:8000'
url_server_device = 'http://192.168.0.18:8000'
json_ptz = {
    'up': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_move",
                            "type_data": "UP"}]
},
    'right': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_move",
                            "type_data": "RIGHT"}]
},
    'left': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_move",
                            "type_data": "LEFT"}]
},
    'down': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_move",
                            "type_data": "DOWN"}]
},
    'stop': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_move",
                            "type_data": "STOP"}]
},
    'poll_device': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_Device",
                            "type_data": "POLL"}]
},
    'install_preset': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_PRESET",
                            "type_data": "PRESET"}]
},
    'call_preset': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_PRESET",
                            "type_data": "CALL_PRESET"}]
},
    'delete_preset': {
    "deviceId": "key64",
    "codeId": "PTZ",
    "data_request_write": [{"type_event": "PTZ_PRESET",
                            "type_data": "DELET_PRESET"}]
},
}
