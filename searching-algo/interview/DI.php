<?php
class PaymentGateway {
    public function charge($amount) {
        return "Total charge: ".$$amount;
    }
}

class OrderService {
    public $PaymentGateway;
    public function __construct(PaymentGateway $PaymentGateway) {
       $this->PaymentGateway = $PaymentGateway;
    }

    public function PlaceOrder($amount) {
        $this->PaymentGateway->charge($amount);
    }
}

class MyServiceProvider {
    
    public function register() {
        $this->app->bind(PaymentGateway::class, Orderservice::class);
        $this->app->singleton(PaymentGateway::class, Orderservice::class);
    }
}


?>