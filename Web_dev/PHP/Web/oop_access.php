<?php

// Defining a class.
class Car {
     // Available to the whole program.
     public $make = "Skytech Normal";

     // Available to this class or subclasses. 
     protected $wheels = "default";  
     protected $doors = 4; 
     protected $metal_frame = "default"; 
     protected $window_material = "glass"; 
     protected $engine = "default"; 
     protected $carType = "Normal Car";
     
     public function showHeader() {
          echo "<h3><u>$this->carType</u></h3>";
     }

     public function showMake() {
          echo "<p><b>Car make</b> : $this->make</p>";
     }

     public function showProperties() { 
          $this->showHeader();
          echo "<table border=1>";

          // Displays the car properties in a table.
          echo "
               <tr>
                    <td colspan=2><b>Default Properties</b></td>
               <tr>
               <tr>
                    <td>Wheels</td><td>$this->wheels</td>
               </tr>
               <tr>
                    <td>Doors</td><td>$this->doors</td>
               </tr>
               <tr>
                    <td>Metal Frame</td><td>$this->metal_frame</td>
               </tr>
               <tr>
                    <td>Window material</td><td>$this->window_material</td>
               </tr>
               <tr>
                    <td>Engine</td><td>$this->engine</td>
               </tr>
               ";

          echo "</table>";

          $this->showMake();
     }
}

class RacingCar extends Car {
     var $make = "Skytech Turbo";
     var $wheels = "racing";
     var $doors = 2; 
     var $window_material = "reinforced glass";
     var $metal_frame = "sleek";
     var $engine = "turbo";
     var $carType = "Racing Car";   
}

$myCar = new Car();
$myCar->showProperties();

echo "<hr>";   

$myRacingCar = new RacingCar();
$myRacingCar->showProperties();

?>