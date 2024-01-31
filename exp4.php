<?php
// Define a basic class 'Car'
class Car {
public $brand;
public $color;

// Constructor
public function __construct($brand, $color) {
$this->brand = $brand;
$this->color = $color;
echo "A new $this->color $this->brand car created.<br>";
}

// Method to display car information
public function displayInfo(){
echo "This is a $this->color $this->brand.<br>";
}

// Destructor
public function __destruct() {
echo "The $this->color $this->brand car is being destroyed.<br>";
}
}

// Inheriting class 'Car' into 'SportsCar'
class SportsCar extends Car {
public $speed;

// Constructor Overloading within inherited class
public function __construct($brand, $color, $speed) {
parent::__construct($brand, $color);
$this->speed = $speed;
}

// Method Overriding
public function displayInfo(){
echo "This is a $this->color $this->brand and can speed up to $this->speed mph.<br>";
}
}

// Creating objects from the classes
$car1 = new Car("Toyota", "red");
$car1->displayInfo();

$sportsCar1 = new SportsCar("Ferrari", "red", 200);
$sportsCar1->displayInfo();

?>