<?php

// Defining a class.
class Car {
    // Default properties of the Car class.
    var $windowColor = "blue"; 
    var $wheels = "normal"; 

   function ModifyCar() { // Method to modify car properties.
        $this->windowColor = "red"; 
        $this->wheels = "turbo"; 
        echo "<hr><h4>Car Modified!</h4><hr>";
   }

   function DisplayProperties() { // Method to display car properties.
        echo "<p>Window color: $this->windowColor</p>";
        echo "<p>Wheel: $this->wheels</p>"; 
   }
}

// Instantiating classes.
$bmw = new Car(); 

class ArmoredCar extends Car {
     // Extending the functionality of Car by providing it with armor. 
     var $hullFront = "heavy armor"; 
     var $hullSides = "light armor"; 
     var $hullRear = "light armor"; 

     // Modifying the base class properties.
     var $windowColor = "tinted green";
     var $wheels = "off road";

     function DisplayBattleProperties() { // Method to display armored vehicle properties.
          echo "<h4>Normal car properties</h4>";
          $this->DisplayProperties(); 
          echo "<hr>";

          echo "<h4>Armored vehicle properties</h4>";
          echo "<p>Front hull: $this->hullFront</p>"; 
          echo "<p>Side hull: $this->hullSides</p>"; 
          echo "<p>Rear hull: $this->hullRear</p>"; 
          echo "<hr>";
     }
}

$battleVehicle = new ArmoredCar(); 
$battleVehicle->DisplayBattleProperties();

?>