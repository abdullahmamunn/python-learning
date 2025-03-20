Factory design pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.

The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

The Factory Method Pattern is used when a class can't anticipate the class of objects it must create. The Factory Method Pattern is used when a class wants its subclasses to specify the objects it creates.

Example of Factory Method Pattern in PHP:

<?php
// Interface for creating objects
interface ShapeFactory {
    public function createShape();
}

// Concrete implementation of ShapeFactory for creating Circle objects
class CircleFactory implements ShapeFactory {
    public function createShape() {
        return new Circle();
    }
}

// Concrete implementation of ShapeFactory for creating Square objects
class SquareFactory implements ShapeFactory {
    public function createShape() {
        return new Square();
    }
}

// Interface for shapes
interface Shape {
    public function draw();
}

// Concrete implementation of Shape for Circle
class Circle implements Shape {
    public function draw() {
        echo "Drawing a circle\n";
    }
}

// Concrete implementation of Shape for Square

class Square implements Shape {
    public function draw() {
        echo "Drawing a square\n";
    }
}

// Client code
$circleFactory = new CircleFactory();
$circle = $circleFactory->createShape();
$circle->draw();

$squareFactory = new SquareFactory();
$square = $squareFactory->createShape();
$square->draw();

// in this example, we have an interface ShapeFactory that defines a method createShape() for creating objects. We have two concrete implementations of ShapeFactory: CircleFactory and SquareFactory, each of which creates a specific type of shape (Circle or Square).


?>