const ptz_dict = {'up': 'up', 'down': 'down', 'left': 'left', 'right': 'right', 'stop': 'stop'}

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