#Q1. Banking System (Finance Domain)

class BankAccount:
    bid = 1203
    loc = "Kothaguda"
    minbal = 5000
    def __init__(self, baid, phno, email, bal, name):
        self.baid = baid
        self.phno = phno
        self.email = email
        self.bal = bal
        self.name = name
    
    def display(self):
        print(self.name, self.bal, self.baid, self.phno)
    
    def withdraw(self, mon):
        if(self.bal<0):
            print("bank bal is 0")
        if(self.bal>mon):
            self.bal = self.bal-mon
        else: print("bank balance is low")
        
    def deposit(self, mon):
        if(mon>1_00_000):
            print("deposits only 1 lakh and below.")
        else:
            self.bal = self.bal+mon
    
    @classmethod
    def update_min_balance(cls, newminbal):
        cls.minbal = newminbal
        print(f"New minimum balance is {newminbal}")

ba1 = BankAccount(1221, 1234567890, "anukdf@gmail.com", 1_20_000, "anusha")
ba2 = BankAccount(1222, 1234567891, "gunakdf@gmail.com", 1_20_000, "guna")

ba1.display()
ba1.withdraw(120000)
ba1.display()
ba1.withdraw(50000)
ba1.display()
ba1.deposit(70000)
ba1.display()


BankAccount.update_min_balance(100)