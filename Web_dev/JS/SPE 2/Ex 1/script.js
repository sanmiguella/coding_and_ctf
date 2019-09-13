function find_biggest_fraction(a, b) {
    var result = "";  // Declared variable scope : Local

    if (a > b) {    // If a is greater than b
        result = "a: " + a; // String will be "a: { value }"
    }
    
    else {  // If a is lesser than b
        result = "b: " + b; // String will be "b: { value }"
    }

    return result; // Returns result to the calling function
}

var first_fraction = 3 / 4;     // 0.75
var second_fraction = 5 / 7;    // 0.71

// Since find_biggest_fraction() returns a value, we will just use
// the return value as an input for console.log()
console.log( find_biggest_fraction(first_fraction, second_fraction) );