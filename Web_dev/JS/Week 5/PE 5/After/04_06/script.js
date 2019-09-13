var first_fraction = 7/9; 
var second_fraction = 13/25; 

var the_biggest = (function(a, b) {
    var result; 
    a > b ? result = ["Value of a: <u>" + round_to_two(a) + "</u>"] : result = ["Value of b: <u>" + round_to_two(b) + "</u>"];

    return result;
}) (first_fraction, second_fraction)

function round_to_two(num) {
    return ( Math.round(num * 100) / 100 )  ;
}

function display_str(msg) {
    document.body.innerHTML = "<h2>Immediately invoked function expressions</h2>"; 
    document.body.innerHTML += msg; 

    console.log(msg); // Display output in console
}

display_str(the_biggest)