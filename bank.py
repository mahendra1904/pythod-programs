#BANK APPLICATION
import sys
print('WELCOME TO KANPUR NATIONAL BANK ')
customer_name=input('Enter your name : ')
print('Welcome ', customer_name,' Please select the folloing option for banking :  ')
balance=0
while True:
    print(' d- deposit \n w- withdraw \n e- exit: ')
    option=input('Choose your option :  ')
    if option=='d' or option=='D':
        amt=float(input('Enter the amout to deposit :' ))
        balance=balance+amt
        print(' After deposit the balance is : ',balance)
    elif option=='w' or option =='W':
        amt=float(input('Enter the amout to withdraw : '))
        if amt>balance:
            print(' Insufficeant fund : can not perform this operation :  ')
        else:
            
            balance=balance-amt
            print(' After withdrw the balance is : ',balance)
    elif option.lower()=='e':
        print('Thanks for banking : ')
        sys.exit()
    else:
        print('Chose the valid options:   ')
