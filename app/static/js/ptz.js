const ptz_dict = {'up': 'up', 'down': 'down', 'left': 'left', 'right': 'right', 'stop': 'stop', 'set_preset': 'set_preset', 'select_preset': 'select_preset', 'get_presets': 'get_presets'}

function make_act(act){
    console.log(ptz_dict[act])
    data = {
        cam_ip: document.getElementById('cam_ip').value,
        port: document.getElementById('port').value,
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
    }
        fetch(`/${ptz_dict[act]}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        body: JSON.stringify({
            data: data,
        }),
    })
    .then((response) => {
        console.log(response.status)
    })
}