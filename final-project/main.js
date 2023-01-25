alert('hello');
// Global variables
const time_el = document.querySelector('.watch .time')
const start_btn = document.getElementById('start')
const stop_btn = document.getElementById('stop')
const reset_btn = document.getElementById('reset')

let seconds = 48456;
let interval = null;

// Event listeners


// Update the timer
function timer () {
    seconds--;

    // Format time
    let mins = Math.floor(seconds / 60);
    let secs = seconds % 60;

    if (secs < 10) secs = '0' + secs;
    if (mins < 10) mins = '0' + mins;
    
    time_el.innerText = `${mins}:${secs}`;
}

function start () {
    if (interval) {
        return
    }

    interval = setInterval(timer, 1000);
}