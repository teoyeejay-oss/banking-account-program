class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance= balance

    def __str__(self):
        return f"Account Owner : {self.owner} | Balance : {self.balance:.2f}"

    def __add__(self,other):
         return BankAccount(f"{self.owner} and {other.owner}", self.balance + other.balance)

    @classmethod
    def from_dict(cls,data):
        return cls(data["owner"],data["balance"])

    @staticmethod
    def valid_amount(amount):
        return amount >0

    def deposit(self,amount):
        if BankAccount.valid_amount(amount):
            self.balance += amount
            print(f"Deposited : RM{amount:.2f}")
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if not BankAccount.valid_amount(amount):
            print("Invali amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else :
            self.balance -= amount
            print(f"Withdraw :RM{amount:.2f}")


acc1 = BankAccount("Ali",1000)
acc2 = BankAccount.from_dict({"owner":"Kuma","balance":3000})
acc1.deposit(500)
acc2.withdraw(4000)
combined =acc1 + acc2
print(combined)
print(acc1)
print(acc2)