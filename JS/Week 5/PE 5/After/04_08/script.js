const MYCONSTANT = 5; // can't be changed after declaration

function log_scope() {
    var local_var = 2; 
    
    if (local_var) {
        // Allows variable to be changed inside this block 
        // If let isn't declared, changing value of variable
        // inside this block would change the value of the variable
        // outside the block.
        let local_var = "I'm different!"; 
        
        display_string("<b>Nested</b> local_var : " + local_var); 
    }

    display_string("<b>log_scope</b> local_var : " + local_var);
}

function display_string(msg) {
    document.body.innerHTML += msg + "<br>";
    console.log(msg); 
}

log_scope();