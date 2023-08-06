class Account:
 def __init__(self,title=None,balance=0):
          self.title=title
          self.balance=balance
class SavingsAccount():
     def __init__(self,title,balance,interestrate):
            self.title=title
            self.balance=balance
            self.interestrate=interestrate
     def Savings_Account_Details(self):
          return (f'The title is: {self.title}\nThe balance amount is: {self.balance}\nThe interest rate is: {self.interestrate}')
Account1=SavingsAccount("Ashish",5000,5)
Account2=SavingsAccount("Karthik",10000,4)
print(Account1.Savings_Account_Details())
print(Account2.Savings_Account_Details())