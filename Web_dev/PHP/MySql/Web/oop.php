<?php

// Defining a class.
class Car {

    function MoveWheels() {
        echo "<p>Wheels moved!</p>";
    }
}

// Checking if method exists.
if ( method_exists("Car", "MoveWheels") ) {
    echo "<p>Method Exists!</p>"; 
} else {
    echo "<p>Method doesn't exist!</p>";
}

// Defining new instances of Car class.
$bmw = new Car(); 
$mercedes = new Car(); 

// Accessing methods of the Car class.
echo "<hr><h3>Starting engine for BMW:</h3>"; 
$bmw->MoveWheels();

echo "<hr><h3><h3>Starting engines for Mercedes:</h3>";
$mercedes->MoveWheels();

?>