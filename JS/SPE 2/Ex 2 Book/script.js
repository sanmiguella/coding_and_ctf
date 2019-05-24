/**
 * Title: PES-EX2
 * AUTHOR: SUHAIRY BIN SUBORI
 * ID: P7358646
 * CLASS: DICS1/CE/1910/1
 * **/

// Method 2: Book
function reverse_anything(x) {
    // If an empty string ("") is used as the separator, the string is split between each character
    uInput_split = user_input.split(""); 
    uInput_reverse = uInput_split.reverse(); // Reverse the order of elements in an array
    // Seperator used: whitespace, to prevent the joined string from forming into a string separated with commas(,)
    uInput_join = uInput_reverse.join(""); 

    return uInput_join; // Returns result to the calling function
}

var user_input = prompt("Input a string"); // Prompts user to enter a string
alert(reverse_anything(user_input)); // Since reverse_anyting returns a value, we will be using it as an input for alert