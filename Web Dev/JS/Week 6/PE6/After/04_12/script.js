function do_some_math() {
	// Variable scope: Local
	var a = 5; 
	var b = 4;
	var x = multiply(); // Another way to do it

	// Nested function
	// Closure: A function inside a function
	function multiply() {
		var result = a * b; 
		return result; 
	}

	//return multiply;
	return x; // Another way to do it
}

// Declares variable and assign the output of a function to be its value
var the_result = do_some_math();

//console.log("The result: ", the_result());
console.log("The result: ", the_result); // Another way to do it
