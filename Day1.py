#Question: Student Grade Calculator

#marks
maths = int(input("Enter your maths marks: "))
chemistry = int(input("Enter your chemistry marks: "))
physics = int(input("Enter your physics marks: "))
english = int(input("Enter your english marks: "))
geography = int(input("Enter your geography marks: "))

sum = (maths + chemistry + physics + english + geography)/500 * 100
print(sum)

if(sum >= 90):
    print("Grade A")
elif(80 <= sum <89.99 ):
    print("Grade B")
elif(70 <= sum <79):
    print("Grade C")
elif(60 <= sum <69):
    print("Grade D")
elif(sum < 60):
    print("Grade F")