# Parent Class (Encapsulation Example)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable (__ balance) - Encapsulation

    # Method: Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposit ho gaye. Naya Balance: ₹{self.__balance}")
        else:
            print("Invalid amount!")

    # Method: Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} nikal gaye. Bacha hua Balance: ₹{self.__balance}")
        else:
            print("Insufficent balance ya invalid amount!")

    # Getter for private balance
    def get_balance(self):
        return self.__balance


# Child Class (Inheritance & Polymorphism Example)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        # Parent class ke constructor ko call karna
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # Extra Method for Savings Account
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"₹{interest} interest add ho gaya!")


# --- Execution (Objects Creation) ---

print("=== Normal Bank Account ===")
acc1 = BankAccount("Rahul", 1000)
acc1.deposit(500)
acc1.withdraw(300)
print(f"Total Balance: ₹{acc1.get_balance()}\n")

print("=== Savings Account (Inheritance) ===")
acc2 = SavingsAccount("Priya", 2000, 0.05)
acc2.add_interest()  # Interest calculate hoke deposit hoga