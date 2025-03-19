<?php
	class Car {
	  
	  public $brand;
	  public $color;
	  
	  public function __construct($brand, $color) {
	    $this->brand = $brand;
	    $this->color = $color;
	  }
	  
	  public function displayInfo() {
	    return "This car is a $this->color $this->brand";
	  }
	  
	}
	
	class ElectricCar extends Car{
	  
	  public $battery_capacity;
	  
	  public function __construct($brand, $color, $battery_capacity) {
	    parent::__construct($brand, $color);
	    $this->battery_capacity = $battery_capacity;
	  }
	  
	  public function displayBatteryInfo() {
	    return " And car has battery capacity $this->battery_capacity KWH"; 
	  }
	  
	}
	
	$myCar = new ElectricCar("Toyota", "Black", 75);
  echo $myCar->displayInfo();
  echo $myCar->displayBatteryInfo();
  
// 👉 A child class inherits properties and methods from a parent class.
// extends — Creates a subclass.
// parent::__construct — Calls the parent class constructor.


?>