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
          echo "<h4>Normal car properties</h4>";
          echo "<p>Window color: $this->windowColor</p>";
          echo "<p>Wheel: $this->wheels</p>"; 
          echo "<hr>";     
     }

     // Constructor: Autostart for classes.
     function __construct() { // Once a new instance of the Car class has been created, display its properties.
          $this->DisplayProperties();
     }
}

class ArmoredCar extends Car {
     // Extending the functionality of Car by providing it with armor. 
     var $hullFront = "heavy armor"; 
     var $hullSides = "light armor"; 
     var $hullRear = "light armor"; 

     // Modifying the base class properties.
     var $windowColor = "tinted green";
     var $wheels = "off road";

     function DisplayBattleProperties() { // Method to display armored vehicle properties.
          echo "<h4>Armored vehicle properties</h4>";
          echo "<p>Front hull: $this->hullFront</p>"; 
          echo "<p>Side hull: $this->hullSides</p>"; 
          echo "<p>Rear hull: $this->hullRear</p>"; 
          echo "<hr>";
     }

     // Constructor: Autostart for classes.
     function __construct() { // Once a new instance of the ArmoredCar class has been created, display its base class properties and its battle properties.
          $this->DisplayProperties();
          $this->DisplayBattleProperties();
     }
}

// Instantiating classes.
$battleVehicle = new ArmoredCar(); 

?>