const ptz_dict = {'up': 'up'}

function up(act){
    console.log('up')
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