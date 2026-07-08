#Day 4 Project: Movie Ticket Booking System 🎬

print("========== Welcome to SanScar cinema ==========")
print("1.Movie's Casting")
print("2.Upcoming Movies")
print("3.Ticket Booking")
print("4.Exit")

choice = int(input("Enter your choice: "))
movie1 = "Dhoom"
movie2 = "Cars 2"
movie3 = "F1"
movie4 = "Spider-Man No way home"
movie5 = "Tokyo Drift"
invalid = "Invalid Choice"


if(choice == 3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    ticket = int(input("Ticket: "))
    colddrink = int(input("Would you like Cold Drink? (Yes = 1/No = 2): "))
    popcorn1 = int(input("Would you like Popcorn? (Yes = 1/No = 2): "))

    if age < 0 or ticket <= 0:
        print("Invalid Input")
    elif(age < 12):
        print("Customer: ", name)
        print("Age: ", age)

        print("Ticket price: ₹100 ")
        print("Ticket: ", ticket)

        if(colddrink == 1):
            print("Rate is: ₹80")
            print("1.Continue")
            print("2.Cancel")
            cold = int(input("Enter your choice: "))
            if(cold == 1):
                print("Thank you for purchase")
                coldrate = 80
            else:
                coldrate = 0
                print("Payment is canceled")
        elif(colddrink == 2):
             coldrate = 0
             print("Cold Drink not selected")
        else:
            coldrate = 0
            print("Invalid choice for Cold Drink")

        if(popcorn1 == 1):
            print("Rate is: ₹150")
            print("1.Continue")
            print("2.Cancel")
            pop2 = int(input("Enter your choice: "))
            if(pop2 == 1):
                print("Thank you for purchase")
                poprate = 150
            else:
                poprate = 0
                print("Payment is canceled")
        elif(popcorn1 == 2):
             poprate = 0
             print("Popcorn not selected")
        else:
            poprate = 0
            print("Invalid choice for popcorn")

        if(ticket > 3):
            print("Congratulations!")
            print("You got ₹100 OFF")
            totalbill = ticket*100 + poprate + coldrate
            print("Total Bill: ", totalbill - 100)
        else:
            print("Total Bill: ", ticket*100 + poprate + coldrate)


        print("Enjoy the Movie! 🍿")
    elif(12 <= age < 60):
        print("Customer: ", name)
        print("Age: ", age)

        print("Ticket price: ₹200 ")
        print("Ticket: ", ticket)

        if(colddrink == 1):
            print("Rate for Cold Drink is: ₹80")
            print("1.Continue")
            print("2.Cancel")
            cold = int(input("Enter your choice: "))
            if(cold == 1):
                print("Thank you for purchase")
                coldrate = 80
            else:
                coldrate = 0
                print("Payment is canceled")
        elif(colddrink == 2):
             coldrate = 0
             print("Cold Drink not selected")
        else:
            coldrate = 0
            print("Invalid choice for Cold Drink")

        if(popcorn1 == 1):
            print("Rate for Popcorn is: ₹150")
            print("1.Continue")
            print("2.Cancel")
            pop2 = int(input("Enter your choice: "))
            if(pop2 == 1):
                print("Thank you for purchase")
                poprate = 150
            else:
                poprate = 0
                print("Payment is canceled")
        elif(popcorn1 == 2):
             poprate = 0
             print("Popcorn not selected")
        else:
            poprate = 0
            print("Invalid choice for popcorn")

        if(ticket > 3):
            print("Congratulations!")
            print("You got ₹100 OFF")
            totalbill = ticket*200 + poprate + coldrate
            print("Total Bill: ", totalbill - 100)
        else:
            print("Total Bill: ", ticket*200 + poprate + coldrate)

        print("Enjoy the Movie! 🍿")
    elif(age >= 60):
        print("Customer: ", name)
        print("Age: ", age)

        print("Ticket price: ₹150 ")
        print("Ticket: ", ticket)

        if(colddrink == 1):
            print("Rate for Cold Drink is: ₹80")
            print("1.Continue")
            print("2.Cancel")
            cold = int(input("Enter your choice: "))
            if(cold == 1):
                print("Thank you for purchase")
                coldrate = 80
            else:
                coldrate = 0
                print("Payment is canceled")
        elif(colddrink == 2):
             coldrate = 0
             print("Cold Drink not selected")
        else:
            coldrate = 0
            print("Invalid choice for Cold Drink")

        if(popcorn1 == 1):
            print("Rate for Popcorn is: ₹150")
            print("1.Continue")
            print("2.Cancel")
            pop2 = int(input("Enter your choice: "))
            if(pop2 == 1):
                print("Thank you for purchase")
                poprate = 150
            else:
                poprate = 0
                print("Payment is canceled")
        elif(popcorn1 == 2):
             poprate = 0
             print("Popcorn not selected")
        else:
            poprate = 0
            print("Invalid choice for popcorn")

        if(ticket > 3):
            print("Congratulations!")
            print("You got ₹100 OFF")
            totalbill = ticket*150 + poprate + coldrate
            print("Total Bill: ", totalbill - 100)
        else:
            print("Total Bill: ", ticket*150 + poprate + coldrate)

        print("Enjoy the Movie! 🍿")


elif(choice == 1):
    print(movie1)
    print(movie2)
    print(movie3)
    print(movie4)
    print(movie5)
    print("Thank You")

elif(choice == 2):
    print("Krish 4")
    print("Top gun maverick 3")
    print("Bhool Bhulaya")
    print("Jolly L.L.B 4")
    print("The universe")

elif(choice == 4):
    print("Thank You")
    