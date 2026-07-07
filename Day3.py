# Day 3 Project: Electricity Bill Calculator

name = input("Enter your name: ")
unit = int(input("Enter the number of unit consumed: "))

if(0< unit <= 100):
    print("Customer: ", name)
    print("Units: ", unit)
    print("Rate is ₹5 per unit")
    print("Total Bill: ", unit*5)
elif(100 < unit <= 200):
    print("Customer: ", name)
    print("Units: ", unit)
    print("Rate is ₹7 per unit")
    print("Total Bill: ", unit*7)
elif(unit > 200):
    print("Customer: ", name)
    print("Units: ", unit)
    print("Rate is ₹10 per unit")
    print("Total Bill: ", unit*10)
else:
    print("Invalid Units")

print("Thank you for using our Electricity Bill Calculator", name)