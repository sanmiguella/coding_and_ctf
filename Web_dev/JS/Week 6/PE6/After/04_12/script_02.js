function give_me_Ems(pixels) {
    var base_value = 16; // Normal browser font sizze

    function do_the_math() { 
        return pixels / base_value; 
    }

    return do_the_math; 
}

// Declares several variable and pass different values to each according
// to browser font size ranging from small to extra large
var small_size = give_me_Ems(12); 
var medium_size = give_me_Ems(18); 
var large_size = give_me_Ems(24); 
var extra_large_size = give_me_Ems(32); 

// Only by calling example_var() with this syntax will there be a value
console.log("Small size: ", small_size()); 
console.log("medium size: ", medium_size()); 
console.log("large size: ", large_size()); 
console.log("extra large size: ", extra_large_size()); 