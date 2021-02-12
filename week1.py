class bankaccount():
    def __init__(self,bankname,name,age,accountnumber,balance):
        self.bankname=bankname
        self.name=name
        self.age=age
        self.accountnumber=accountnumber
        self.balance=balance

    def show_details(self):
        print("enter valid information")
        print("")
        print('bankname:', self.bankname)
        print('name:', self.name)
        print('age:', self.age)
        print('accountnumber:', self.accountnumber)
        print('balance:', self.balance)

class mobilebank(bankaccount):
    def __init__(self,bankname,name,age,accountnumber,balance):
        super().__init__(bankname,name,age,accountnumber,balance)
        self.balance=0
    def deposit(self,amount):
        print('you have despoisted sucessfully')
        self.balance=self.balance+amount
        print('account has been updated',self.balance)
    def withdraw(self,amount):
        if self.balance>=amount:
            print("you withdrawal amount has been sucessfully completed")
            self.balance=self.balance-amount
            print('your balance',self.balance)
        else:
            print('insufficent balance')
    def viewbalance(self):
        self.show_details()
        print('your balance',self.balance)

s1=bankaccount('icic', 'vamshi', 20, 1903302142, 5000)
s1.show_details()
p1=mobilebank('sbi', 'ravi', 22, 1912421222212, 500000)
p1.show_details()
p1.deposit(2500000)
p1.withdraw(200)
print()
p1.viewbalance()