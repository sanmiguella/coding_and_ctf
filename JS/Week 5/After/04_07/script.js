// Global scope variables
var first_fraction = 7/16;
var second_fraction = 13/25;


function find_biggest_fraction(a, b) {
    console.log("Fraction a: ", first_fraction);
    console.log("Fraction b: ", second_fraction);

    var result; // Local scope

    // result are stored in arrays [x, y, z]
	a > b ? result = ["a", a] : result = ["b", b]; 
    return result;
}


function display_str(msg) {
    document.body.innerHTML = "<h2>Variable scope</h2>"; 
    document.body.innerHTML += msg; 

    console.log(msg); // Display output in console
}


var fraction_result = find_biggest_fraction(first_fraction, second_fraction);

// fraction_result[0] -> "a" or "b" 
// fraction_result[1] -> fraction_results
var output_msg = "Fraction " + fraction_result[0] + " with a value of " + fraction_result[1] + " is the biggest.";

display_str(output_msg); 
