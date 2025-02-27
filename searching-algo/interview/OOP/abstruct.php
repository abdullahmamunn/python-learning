<?php
 abstract class Animal {
   protected $name;
   
   public function __construct($name) {
     $this->name = $name;
   }
   
   abstract public function makeSound(); // Abstract method — must be implemented by child classes
   
   public function eat() {     // Concrete method — shared across all child classes
     echo "$this->name eats\n";
   }
 }
 
 class Dog extends Animal {
   public function makeSound() {
     echo "$this->name Says Woof!\n";
   }
 }
 
class Cat extends Animal {
   public function makeSound() {
     echo "$this->name Says Mew!\n";
   }
 }
 
 
$dog = new Dog('Tom');
$cat = new Cat('Tommi');

$dog->makeSound();
$dog->eat();

$cat->makeSound();
$cat->eat();




 abstract class Vehicle {
   protected $name;
   
   public function __construct($name) {
     $this->name = $name;
   }
   
   abstract public function startEngine(); // Abstract method — must be implemented by child classes
   abstract public function stopEngine();
   
   public function describe() {     // Concrete method — shared across all child classes
     echo "$this->name looking good\n";
   }
 }
 
 class Car extends Vehicle {
  public function startEngine() {
     echo "$this->name when started, it is using four wheels.\n";
   }
   
  public function stopEngine() {
     echo "$this->name when stopped, its four wheels stop\n";
   }
 }
 
class Bike extends Vehicle {
  public function startEngine() {
     echo "$this->name when started, it uses two wheels\n";
   }
   
  public function stopEngine() {
     echo "$this->name when stopped, its two wheels also stop\n";
   }
 }
 
 
$car = new Car('Toyota');
$bike = new Bike('Royal Anfield');

$car->startEngine();
$car->stopEngine();
$car->describe();

$bike->startEngine();
$bike->stopEngine();
$bike->describe();




?>