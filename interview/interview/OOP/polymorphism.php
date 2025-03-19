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
	
   class SportCar extends Car{
     public function displayInfo() { // override the method from parent class
       return "This is sports car $this->brand $this->color and it's too fast";
     }
   }
   
   $obj = new SportCar("Ferreri", "black");
   
   echo $obj->displayInfo();


?>