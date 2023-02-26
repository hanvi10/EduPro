// Global variables
const time_el = document.querySelector(".watch .time");
const startStop_btn = document.getElementById("startStop");
const reset_btn = document.getElementById("reset");
let stopTime = 0;
let running = false;
let input_seconds;
let seconds;
let interval = null;

const changeBackground_btn = document.getElementById("changeBackground");
const body_el = document.querySelector("body");

const backgrounds = [
"https://images.pexels.com/photos/2559941/pexels-photo-2559941.jpeg",
"https://images.pexels.com/photos/2775196/pexels-photo-2775196.jpeg",
"https://images.pexels.com/photos/3747499/pexels-photo-3747499.jpeg"
];

let currentBackgroundIndex = 0;

// Event listeners
startStop_btn.addEventListener("click", startStop);
reset_btn.addEventListener("click", reset);
changeBackground_btn.addEventListener("click", changeBackground);

// Changes backround
function changeBackground() {
    currentBackgroundIndex++;
    if (currentBackgroundIndex >= backgrounds.length) {
      currentBackgroundIndex = 0;
    }
    body_el.style.backgroundImage = `url('${backgrounds[currentBackgroundIndex]}')`;
  }


// Gets input from user and stores it in variable seconds
function getInput () {
    let input_minutes = Number(document.getElementById("minutes").value);
    input_seconds = input_minutes * 60;
    seconds = input_seconds;
}

function timer () {
    running = true;
    seconds--;

    // Check if seconds is less than or equal to 0
    if (seconds <= 0) {
        clearInterval(interval);
        interval = null;
        running = false;
        startStop_btn.innerText = "Start";
    }

    // Format time
    updateDisplay();
}


function startStop () {
    if (running) {
        // Timer is currently running, so stop it
        clearInterval(interval);
        interval = null;
        running = false;
        startStop_btn.innerText = "Start";
        stopTime = seconds;
    } else {
        // Timer is currently stopped, so start it
        if (stopTime) {
            seconds = stopTime;
            stopTime = 0;
        } else {
            getInput();
        }
        if (seconds > 0) {
        interval = setInterval(timer, 1000);
        running = true;
        startStop_btn.innerText = "Stop";
        }
    }
}

function reset () {
    if (running) {
        clearInterval(interval);
        interval = null;
        running = false;
        startStop_btn.innerText = "Start";
    }
    seconds = input_seconds;
    updateDisplay();
}

function updateDisplay() {
    let hrs = Math.floor(seconds / 3600);
    let mins = Math.floor((seconds - (hrs * 3600)) / 60);
    let secs = seconds % 60;
    if (secs < 10) secs = "0" + secs;
    if (mins < 10) mins = "0" + mins;
    if (hrs < 10) hrs = "0" + hrs;
    if (hrs < 1) {
        time_el.innerText = `${mins}:${secs}`;
    } else {
        time_el.innerText = `${hrs}:${mins}:${secs}`;
    }
}
