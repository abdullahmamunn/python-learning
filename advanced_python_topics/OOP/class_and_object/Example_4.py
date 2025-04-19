# Update version of Example_3
#  Added: 
# Transaction History
# Password Protection
# Interest Calculation (Simple Interest)
# Cleaner & More Modular Code

# Create a BankAccount class with: owner and balance, and password attributes

# Methods:
# deposit(amount)
# withdraw(amount)
# show_balance()
# show_transaction()
# calculate_interest()
# Make sure the withdraw() method checks if the balance is sufficient.



function LetterChanges(str) {
  let result = "";

  for (let i = 0; i < str.length; i++) {
    let char = str[i];

    // If it's a letter
    if (char >= 'a' && char <= 'z') {
      let code = char.charCodeAt(0);
      let nextCode = code + 1;

      // Wrap around z -> a and Z -> A
      if (char === 'z') nextCode = 'a'.charCodeAt(0);
     
      let nextChar = String.fromCharCode(nextCode);

      // Capitalize if vowel
      if ('aeiou'.includes(nextChar.toLowerCase())) {
        nextChar = nextChar.toUpperCase();
      }

      result += nextChar;
    } else {
      result += char;
    }
  }

  return result;
}

console.log(LetterChanges("hello*3"));
