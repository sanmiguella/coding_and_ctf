<?php

// Defining a class.
class Car {

    // Default properties of the Car class.
    var $windowColor = "blue"; 
    var $wheels = "normal"; 
    var $fuel = "empty";

   function ModifyCar() { // Method to modify car properties.
        $this->windowColor = "red"; 
        $this->wheels = "turbo"; 
        $this->fuel = "full";
        echo "<hr><h4>Car Modified!</h4><hr>";
   }

   function DisplayProperties() { // Method to display car properties.
        echo "<p>Window color: $this->windowColor</p>";
        echo "<p>Wheel: $this->wheels</p>"; 
        echo "<p>Fuel: $this->fuel</p>";
   }
}

// Instantiating classes.
$bmw = new Car(); 

echo "<h4>Before mod:</h4>"; 
$bmw->DisplayProperties();  // Display properties before mod.

$bmw->ModifyCar();

echo "<h4>After mod:</h4>"; 
$bmw->DisplayProperties(); // Display properties after mod.


?>