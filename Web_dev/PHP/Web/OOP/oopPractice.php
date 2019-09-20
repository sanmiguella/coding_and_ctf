<?php 

class Dog {
    // Properties for the dog class.
    protected $eyeColor = "black";
    protected $nose = "snout"; 
    protected $furColor = "brown"; 

    public function ShowAll() { // Method to show the properties of the Dog class.
        echo "<p>Eye color : $this->eyeColor</p>"; 
        echo "<p>Nose : $this->nose</p>"; 
        echo "<p>Fur color : $this->furColor</p>"; 
    }
}

class PitBull extends Dog {
    // Changing the base properties of the Dog class since this is a new PitBull class extends the functionality of the Dog class.
    var $eyeColor = "brown"; 
    var $nose = "flat"; 
    var $furColor = "black"; 
}

$myDog = new Dog(); 

echo "<h2>My Dog</h2>";
$myDog->ShowAll(); 
echo "<hr>"; 

$myPitBull = new PitBull(); 

echo "<h2>My Pitbull</h2>"; 
$myPitBull->ShowAll(); 


?>