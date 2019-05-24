// My method
function reverse_anything(x) {
    // String is an array and as such, the upper bound of the array is the length of the array subtracted
    // by 1 since array usually begins with 0
    var upper_bound = x.length - 1; 
    var reversed_str = "";  // Initialize a variable because we do not want any random values in it, good coding practice

    i = upper_bound; 
    while (i >= 0 ) { // Loop continues as long as we haven't execeed the lower bound of user_input
        // If string is Hello, this loop will start with 'o', then, 'l', etc...
        reversed_str += x[i]; 
        i--;   // Remember to decrement, else this while loop will go on forever
    }

    return reversed_str; // Returns the reverse string to the calling function
}

var user_input = prompt("Input a string"); // Prompts user to enter a string
// Since reverse_anything returns a strings, we can use it as an input for alert
alert( reverse_anything(user_input) ); 