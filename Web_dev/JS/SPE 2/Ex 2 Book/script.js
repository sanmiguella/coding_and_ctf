// Method 2: Book
function reverse_anything(x) {
    // If an empty string ("") is used as the separator, the string is split between each character
    uInput_split = x.split(""); 
    uInput_reverse = uInput_split.reverse(); // Reverse the order of elements in an array
    // Seperator used: whitespace, to prevent the joined string from forming into a string separated with commas(,)
    uInput_join = uInput_reverse.join(""); 

    return uInput_join; // Returns result to the calling function
}

var user_input = prompt("Input a string"); // Prompts user to enter a string
alert(reverse_anything(user_input)); // Since reverse_anyting returns a value, we will be using it as an input for alert