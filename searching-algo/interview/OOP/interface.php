<?php

// ✅ Exercise:
// 1️⃣ Create an interface Shape with methods getArea() and getPerimeter().
// 2️⃣ Create two classes — Rectangle and Circle — that implement Shape.
// 3️⃣ Instantiate both classes and print their areas and perimeters.
 interface Shape {
   public function getArea();
   public function getPerimeter();
   
 }
 
 class Rectangle implements Shape {
   public $height;
   public $width;
   
   public function __construct($height, $width) {
     $this->height = $height;
     $this->width = $width;
   }
   public function getArea() {
     return $this->height*$this->width;
   }

   public function getPerimeter() {
    return 2 * ($this->height + $this->width);
   }
   
 }
 
 class Circle implements Shape {
   
   public $radius;
   
   public function __construct($radius) {
     $this->radius = $radius;
   }

   public function getArea() {
    $pi = 3.1416;
     
    return $pi * ($this->radius * $this->radius);
   }
   
   public function getPerimeter() {
     $pi = 3.1416;
     
     return 2 * $pi * $this->radius;
   }
   
 }
 
 
 $rectengle = new Rectangle(7,8);
 $circle    = new Circle(7);
 
 echo $rectengle->getArea();
 echo $circle->getPerimeter();

?>