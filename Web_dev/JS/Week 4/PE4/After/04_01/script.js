// Regular function, called explicitly by name:
function multiply() {
    var result = 3 * 4;
    msg = "(multiply function) 3 multiplied by 4 is " + result + '<br>';

    display_result(msg);
    console.log(msg);
}
multiply();

// Anonymous function stored in variable.
// Invoked by calling the variable as a function:
var divided = function() {
    var result = 3 / 4;
    msg = "(divided function) 3 divided by 4 is " + result + '<br>';
    
    display_result(msg);
    console.log(msg);
}
divided();

// Immediately Invoked Function Expression.
// Runs as soon as the browser finds it:
(function() {
    var result = 12 / 0.75;
    msg = "(Immediately invoked function) 12 divided by 0.75 is " + result + '<br>';

    display_result(msg);
    console.log(msg);
}())

function display_result(display_string) {
    var output = window.frames[0];
    output.document.body.innerHTML += display_string;
}

function clear_iframe() {
    var output = window.frames[0];
    output.document.body.innerHTML = ''; 
}