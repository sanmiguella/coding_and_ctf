function find_biggest_fraction() {
    // declaration of variables
    var numerator_a, denominator_a; 
    var numerator_b, denominator_b; 

    // assign the value from textboxes to variable
    numerator_a = parseInt(document.getElementById('numerator_a').value); 
    denominator_a = parseInt(document.getElementById('denominator_a').value); 

    numerator_b = parseInt(document.getElementById('numerator_b').value); 
    denominator_b = parseInt(document.getElementById('denominator_b').value);

    // turns input into fraction
    // passing arguments to functions
    a = convert_to_fraction(numerator_a, denominator_a); 
    b = convert_to_fraction(numerator_b, denominator_b);

    // condition testing
    if (a > b) { 
        msg = '<i>Fraction A</i> with the value of ' + a + ' is the biggest!<br><br>';
        msg += 'Value of <b>Fraction A</b> is <u>' + a + '</u><br>'; 
        msg += 'Value of <b>Fraction B</b> is <u>' + b + '</u><br>'; 

        display_result(msg);
    } else if (a == b) {
        msg = 'Both fraction are equal!<br><br>';
        msg += 'Value of <b>Fraction A</b> is <u>' + a + '</u><br>'; 
        msg += 'Value of <b>Fraction B</b> is <u>' + b + '</u><br>'; 

        display_result(msg);
    } else {
        msg = '<i>Fraction B</i> with the value of ' + b + ' is the biggest!<br><br>';
        msg += 'Value of <b>Fraction A</b> is <u>' + a + '</u><br>'; 
        msg += 'Value of <b>Fraction B</b> is <u>' + b + '</u><br>'; 

        display_result(msg);
    }
}

var output = window.frames[0];

// for easier display, use iframe
function display_result(display_string) {
    output.document.body.innerHTML = display_string;
}

// clears the value of every input
function clear_input() {
    document.getElementById('numerator_a').value = ''; 
    document.getElementById('denominator_a').value = ''; 

    document.getElementById('numerator_b').value = ''; 
    document.getElementById('denominator_b').value = '';
}

function convert_to_fraction(numerator, denominator) {
    fraction = numerator / denominator; 
    return fraction; // return the result of the division
}
