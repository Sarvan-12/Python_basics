#create Account class with 2 attributes - balance and account no.
#create methods for debit,credit and printing the balance

class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no
    def debit(self,amt):
        self.bal-=amt
        print(amt,"Rs was debited")
        print("total balance =",self.bal)
    def credit(self,amt):
        self.bal+=amt
        print(amt,"Rs was credited")
        print("total balance =",self.bal)
   
    def print_bal(self):
        print(self.bal)

a1=Account(10000,12345)
print(a1.bal)
print(a1.acc_no)
a1.debit(1500)
a1.credit(2350)
a1.print_bal()

