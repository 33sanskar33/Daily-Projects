#Day 2 Project: ATM Machine 

print("Welcome to the ATM Machine")
print("1.Check Balance")
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Exit")
balance = 10000

choice = int(input("Enter Your Choice: "))

if(choice == 1):
    print("Balance is: ", balance)
elif(choice == 2):
    deposit = int(input("Enter amount to deposit: "))
    if(deposit > 0):
        balance += deposit
        print("₹", deposit, "Deposit Sucessfully")
        print("Current Balance:", balance)
    else:
        print("Invalid Choiec")
elif(choice == 3):
    withdraw = int(input("Enter amount to withdraw: "))
    if(balance >= withdraw):
        balance -= withdraw
        print("Current balance is : ", balance)
    else:
        print("Insufficient Balance")
elif(choice == 4):
    print("Thanks for using ATM")
else:
    print("Invalid Choice")

