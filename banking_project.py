#Kanpur National Bank Project
import sys
print("Welcome to Kanpur National Bank ")
balance=0
customer_name=input("Please Enter your Name: ")
print("Welcome",customer_name,',')
print("*"*20)
while True:
    option=input("Choose D for Deposit:\nChoose W for Withdrawl:\nChoose E for Exit:\n")
    if option=="D" or option=="d":
        amount=int(input("Enter the amount to deposit: "))
        balance+=amount
        print("After Deposit your updated balance is ",balance)
    elif option=="W" or option=="w":
        withdrawl=int(input("Enter the amount to withdraw: "))
        if withdrawl>balance:
            print("You Don't have sufficient balance,Check Again")
        else:
            balance-=withdrawl
            print("Your updated balance is",balance)
    elif option=="E" or option=="e":
        print("Thankyou for banking,Visit Again Soon")
        sys.exit()
    else:
        print("Enter the options mentioned below")
