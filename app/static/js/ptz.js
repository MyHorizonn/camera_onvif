const ptz_dict = {'up': 'up', 'down': 'down', 'left': 'left', 'right': 'right', 'stop': 'stop', 'set_preset': 'set_preset'}

function make_act(act){
    console.log(ptz_dict[act])
    fetch(`/${ptz_dict[act]}`, {
        method: 'POST',
        headers: {
            'Content0Type': 'application/json'
        }
    })
    .then((response) => {
        console.log(response.status)
    })
}