class Example:
    def __init__(self):
        self.public_var = "I am Public"         # Public attribute
        self._protected_var = "I am Protected"  # Protected attribute
        self.__private_var = "I am Private"     # Private attribute

    def public_method(self):
        return "Public method can be accessed anywhere"

    def _protected_method(self):
        return "Protected method can be accessed within subclass or instance (not enforced)"

    def __private_method(self):
        return "Private method, not directly accessible outside the class"

    def access_private(self):
        return self.__private_method()  # Private method accessed within class


# Creating object
obj = Example()

# Public attributes/methods can be accessed freely
print(obj.public_var)
print(obj.public_method())

# Protected attributes/methods can be accessed but should be used cautiously
print(obj._protected_var)
print(obj._protected_method())

# Private attributes/methods cannot be accessed directly
# print(obj.__private_var)  # Raises AttributeError
# print(obj.__private_method())  # Raises AttributeError

# Accessing private variables using name mangling
print(obj._Example__private_var)  # Works, but not recommended
print(obj.access_private())  # Accessing private method via a public method



class Parent:
    def __init__(self):
        self._protected_var = "Protected variable in Parent"

    def _protected_method(self):
        return "This is a protected method in Parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_var = "Child variable"

    def use_protected(self):
        # Accessing the protected method from Parent within the Child class
        parent_msg = self._protected_method()
        return f"Child accessing: {parent_msg}"


# Creating an instance of Child
child_instance = Child()

# Accessing the protected method via a public method in Child
print(child_instance.use_protected())

# Note: Although you can technically call the protected method directly,
# it is discouraged to do so outside the class hierarchy.
print(child_instance._protected_method())


# Single Inheritance:
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    pass

child = Child()
print(child.greet())  # Output: Hello from Parent!


#multiple Inheritance 
class Parent1:
    def greet(self):
        return "Hello from Parent1!"

class Parent2:
    def greet2(self):
        return "Hello from Parent2!"

class Child(Parent1, Parent2):
    pass

child = Child()
print(child.greet())   # Output: Hello from Parent1!
print(child.greet2())  # Output: Hello from Parent2!


# Multilevel Inheritance:

class Grandparent:
    def say(self):
        return "Hello from Grandparent!"

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

child = Child()
print(child.say())  # Output: Hello from Grandparent!



#Hierarchial Inheritance 
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child1(Parent):
    pass

class Child2(Parent):
    pass

child1 = Child1()
child2 = Child2()
print(child1.greet())  # Output: Hello from Parent!
print(child2.greet())  # Output: Hello from Parent!


#Hybrid Inheritance 
class Base:
    def greet(self):
        return "Hello from Base!"

class Parent1(Base):
    def greet(self):
        return "Hello from Parent1!"

class Parent2(Base):
    def greet(self):
        return "Hello from Parent2!"

# Multiple inheritance combined with hierarchical/multilevel inheritance
class Child(Parent1, Parent2):
    pass

child = Child()
# Python's MRO will decide which greet() method is used.
print(child.greet())  # Output: Hello from Parent1!


from abc import ABC, abstractmethod

# Base class (Abstract Class)
class BankAccount(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number  # Encapsulation (Protected Attribute)
        self._account_holder = account_holder
        self._balance = balance
        self._transactions = []  # Stores transaction history

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            self._balance += amount
            self._transactions.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully. New Balance: ${self._balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def get_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self._transactions

# Savings Account - Inherits from BankAccount
class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.03  # 3% Annual Interest

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if amount > self._balance:
                raise ValueError("Insufficient balance.")
            self._balance -= amount
            self._transactions.append(f"Withdrawn: ${amount}")
            print(f"${amount} withdrawn successfully. New Balance: ${self._balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def add_interest(self):
        interest = self._balance * self.INTEREST_RATE
        self._balance += interest
        self._transactions.append(f"Interest Added: ${interest:.2f}")
        print(f"Interest of ${interest:.2f} added. New Balance: ${self._balance}")

# Checking Account - Inherits from BankAccount
class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = 500  # Allows overdraft up to $500

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if self._balance - amount < -self.OVERDRAFT_LIMIT:
                raise ValueError("Withdrawal denied! Exceeds overdraft limit.")
            self._balance -= amount
            self._transactions.append(f"Withdrawn: ${amount}")
            print(f"${amount} withdrawn successfully. New Balance: ${self._balance}")
        except ValueError as e:
            print(f"Error: {e}")

# Business Account - Inherits from BankAccount
class BusinessAccount(BankAccount):
    TRANSACTION_FEE = 5  # Fee for every withdrawal

    def withdraw(self, amount):
        try:
            amount = float(amount)
            total_amount = amount + self.TRANSACTION_FEE
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if total_amount > self._balance:
                raise ValueError("Insufficient balance including transaction fee.")
            self._balance -= total_amount
            self._transactions.append(f"Withdrawn: ${amount}, Fee: ${self.TRANSACTION_FEE}")
            print(f"${amount} withdrawn with ${self.TRANSACTION_FEE} fee. New Balance: ${self._balance}")
        except ValueError as e:
            print(f"Error: {e}")

# Interactive Menu with User Input
def main():
    print("\n🏦 Welcome to the Bank Account Management System 🏦")

    # Get user details
    account_holder = input("Enter your full name: ").strip()
    
    while True:
        try:
            account_number = input("Enter a unique account number: ").strip()
            if not account_number.isdigit():
                raise ValueError("Account number must contain only digits.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            initial_balance = float(input("Enter initial deposit amount: $"))
            if initial_balance < 0:
                raise ValueError("Initial deposit cannot be negative.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Account Selection with Error Handling
    while True:
        print("\nChoose an account type:")
        print("1. Savings Account")
        print("2. Checking Account")
        print("3. Business Account")

        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                account = SavingsAccount(account_number, account_holder, initial_balance)
            elif choice == 2:
                account = CheckingAccount(account_number, account_holder, initial_balance)
            elif choice == 3:
                account = BusinessAccount(account_number, account_holder, initial_balance)
            else:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        print("\nChoose an operation:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        if isinstance(account, SavingsAccount):
            print("5. Add Interest")
        print("6. Exit")

        try:
            option = int(input("Enter your option (1/2/3/4/5/6): "))

            if option == 1:
                amount = input("Enter deposit amount: $")
                account.deposit(amount)
            elif option == 2:
                amount = input("Enter withdrawal amount: $")
                account.withdraw(amount)
            elif option == 3:
                print(f"Your current balance is: ${account.get_balance()}")
            elif option == 4:
                print("Transaction History:", account.get_transaction_history())
            elif option == 5 and isinstance(account, SavingsAccount):
                account.add_interest()
            elif option == 6:
                print("Thank you for using our system. Goodbye! 👋")
                break
            else:
                print("Invalid option. Please choose a valid operation.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

# Run the main menu
if __name__ == "__main__":
    main()


import numpy as np
x = np.percentile(ages, 75)
print(x)  # Output: 43
