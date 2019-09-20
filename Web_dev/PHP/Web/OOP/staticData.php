<?php

// Defining a class.
class Car {
    static $wheels = 4; // Static properties.
    static $door = 4; 
    var $hood = 0; 

    function ModifyCar() { // Method for modifying properties of the Car class.
        Car::$wheels = 6; 
        Car::$door = 2;
        $this->hood = 1;

        echo "<h4>Modification completed!</h4>"; 
    }

    function ShowProperties() {
        echo "<p>Wheels(static) : " . Car::$wheels . "</p>"; // Modifying static properties.
        echo "<p>Door(static) : " . Car::$door . "</p>"; 
        echo "<p>Hood : $this->hood</p>";
    }
}


$bmw = new Car(); 

$bmw->ShowProperties();
echo "<hr>"; 

$bmw->ModifyCar(); 
$bmw->ShowProperties();




?>