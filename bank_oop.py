# BANK APPLICATION  VIA OOPS
import sys
class customer:
    ''' customer class with bank related operations'''
    bank_name='PMC CORPORATION'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print(' After deposit the balance is :   ', self.balance)
    def withdrw(self,amt):
        if amt>self.balance:
            print('insufficient funds: can not perform operations:  ')
            sys.exit()
        else:
            self.balance=self.balance-amt
            print('After withdraw the balance is :  ', self.balance)

print('welcome to ',customer.bank_name)
name=input('Enter your name: ')
c=customer(name)
while True:
    print('d-deposit \n w-withdraw \n e- exit')
    option=input('choose your option : ')
    if option.lower()=='d':
        amt=float(input(' Enter the amout to deposit  '))
        c.deposit(amt)
    elif option.lower()=='w':
        amt=float(input('Enter the amount to withdraw  '))
        c.withdrw(amt)
    elif option.lower()=='e':
        print('Thanks for Banking   ')
        sys.exit()
    else:
        print('Choose the correct option  ')



    
