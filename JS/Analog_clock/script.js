const HOURHAND = document.querySelector("#hour");
const MINUTEHAND = document.querySelector("#minute");
const SECONDHAND = document.querySelector("#second");

var date = new Date();
let hr = date.getHours();
let min = date.getMinutes();
let sec = date.getSeconds();
let msg = '';

msg = ''
msg += date + '\n\n';
msg += hr + '(hrs) ';
msg += min + '(mins) ';
msg += sec + '(secs)';

console.log(msg);

let hrPosition = (hr * 360 / 12) + (min * (360 / 60) / 12);
let minPosition = (min * 360 / 60) + (sec * (360 / 60) / 60);
let secPosition = sec * 360 / 60;

HOURHAND.style.transform = "rotate(" + hrPosition + "deg)";
MINUTEHAND.style.transform = "rotate(" + minPosition + "deg)";
SECONDHAND.style.transform = "rotate(" + secPosition + "deg)";

function timedRefresh(timeoutPeriod) 
{
    setTimeout("location.reload(true)", timeoutPeriod);
}

window.onload = timedRefresh(1000);

