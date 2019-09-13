//var a = 5/7; 
//var b = 18/25; 

// Results from the ternary operation will return value to the variable:
// the_biggest
var the_biggest = function(a, b) {
    var result; 
    a > b ? result = ["Value of a: <u>" + round_to_two(a) + "</u>"] : result = ["Value of b: <u>" + round_to_two(b) + "</u>"];

    return result;
}

function round_to_two(num) {
    return ( Math.round(num * 100) / 100 )  ;
}

function display_str(msg) {
    document.body.innerHTML = "<h2>Anonymous functions</h2>";
    document.body.innerHTML += msg;

    console.log(msg); // Display output in console
}

// The value from the_biggest variable will be passed as an argument to
// the function display_str()
display_str( the_biggest(7/9, 13/25) ); // Passing of argument to the_biggest()