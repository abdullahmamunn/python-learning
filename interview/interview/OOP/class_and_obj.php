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
	
	$myCar = new Car("Toyota", "Red");
  echo $myCar->displayInfo();
  
  
  // 👉 A PHP class is a blueprint, and an object is an instance of a class.
  // __construct — Initializes object properties.
  // $this — Refers to the current object.
  // public — Accessible from outside the class.


?>