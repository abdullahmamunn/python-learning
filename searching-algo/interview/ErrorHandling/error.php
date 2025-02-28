<?php
// ✅ PHP Try-Catch Exercise
// 1️⃣ Create a BankAccount class with withdraw() and deposit() methods.
// 2️⃣ Throw an exception if withdrawal exceeds the balance.
// 3️⃣ Use try-catch to handle the exception. -->


class InsufficientFundsException extends Exception {}


class BankAccount {

    public $balace;

    public function __construct($initialBalance) {
        if($initialBalance <0) {
            throw new Exception("Initial balance can't be negative");
        }
        $this->balance = $initialBalance; 
    } 

    public function withdraw($amount) {
        if($amount <=0) {
            throw new Exception("Withdrawal amount must be positive.");
        }
        if($amount > $this->balance) {
            throw new Exception("insufficient funds! Balance: \$$this->balance. Tried to withdraw \$$amount");
        }
        $this->balance -= $amount;
        echo "Withdrew: \$$amount. New balance: \$$this->balance\n";
    }

    public function deposite($amount) {
       if ($amount <=0) {
        throw new Exeption("Deposite amount must greater then zero");
       }

       $this->balance +=$amount;
       
       echo "Deposited: \$$amount. New balance: \$$this->balance\n";
    }

}

// Test the BankAccount class
try {
    $account = new BankAccount(500);
    $account->deposit(0);
    $account->withdraw(700); // This will throw InsufficientFundsException
} catch (InsufficientFundsException $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    echo "General Error: " . $e->getMessage() . "\n";
}


?>