<?php

// Defining a class.
class Car {
     // Available to the whole program.
     public $wheels = 4;  
     public $doors = 4; 

     // Available to this class or subclasses. 
     protected $metal_frame = 1; 
     protected $window_material = "glass"; 
     
     private $turbo_engine = 1; // Available only to this class
     
     function __construct() {
          $this->showProperties();
     }

     protected function showProperties() { // Protected function
          echo "<h3>Cars Assembled!</h3>"; 
          echo "<table border=1>";
          echo "
               <tr>
                    <td colspan=2><b>Properties</b></td>
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
                    <td>Turbo engine</td><td>$this->turbo_engine</td>
               </tr>
               ";
          echo "</table>";
     }
}

$bmw = new Car();

?>