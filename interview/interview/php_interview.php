<?php

// Regular Expressions in PHP 

// validate email
function isValidateEmail($email) {
    return (filter_var($email, FILTER_VALIDATE_EMAIL)) ? true : false;
}
echo isValidateEmail('almamuail') ? 'valid' : 'invalid';


// Task: Define a PHP class called Circle, with a private property radius. Add a constructor to set the radius and two public methods: getArea and getCircumference to calculate the area and the circumference of the circle, respectively.

class Circle{
    private $radius;
    public function __construct($radius){
        $this->radius = $radius;
    }

    public function getArea(){
        return pi() * pow($this->radius, 2);
    }

    public function getCircumference(){
        return 2 * pi() * $this->radius;
    }
}

$circle = new Circle(9);
echo $circle->getArea();
echo $circle->getCircumference();
	



