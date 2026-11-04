"""
print("Welcome to your life in weeks")
age = int(input("What is your current age? "))
day_left = (90 - age) * 365
week_left = (90 - age) * 52
month_left = (90 - age) * 12
print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left.")



print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")



print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm ?"))
if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")



print("Welcome to the even/odd number checker")
number = int(input("Which number do you wanna check?"))
if number %2 ==0 : 
    print("this is an even number")
else :
    print("this is an odd number")


print("Welcome to the leap year checker")
year = int(input("which year do you want to check?"))
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")


print("Welcome to the bmi calculator")
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))
bmi = round(weight / height**2, 2)
if bmi<18.5 :
    print(f"Your BMI is {bmi}, your are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi}, your are normal weight")
elif bmi<30:
    print(f"Your BMI is {bmi}, your are overweight")
elif bmi<35:
    print(f"Your BMI is {bmi}, your are obese")
else:
    print(f"Your BMI is {bmi}, your are clinically obese")

print("Welcome to the pizza order program")

size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni ? Y or N : ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")
if size == "S" or size == "s" :
    bill = 15
    if add_pepperoni == "Y" or add_pepperoni == "y" :
        bill += 2
    if extra_cheese == "Y" or extra_cheese == "y" :
        bill += 1
elif size == "M" or size == "m" :
    bill = 20
    if add_pepperoni == "Y" or add_pepperoni == "y"  :
        bill += 3
    if extra_cheese == "Y" or extra_cheese == "y" :
        bill += 1
elif size == "L" or size == "l" :
    bill = 25
    if add_pepperoni == "Y" or add_pepperoni == "y" :
        bill += 3
    if extra_cheese == "Y" or extra_cheese == "y" :
        bill += 1

print(f"Your final bill is ${bill}.")

print("Welcome to the love calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1 + name2
lower_case_names = combined_names.lower()
t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
true = t + r + u + e
love = l + o + v + e
love_score = int(str(true) + str(love))
print(f"Your love score is: {love_score}")
"""

print("Welcome to the treasure island")
print("Your mission is to find the treasure.")
input1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
if input1 == "left":
    input2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if input2 == "wait":
        input3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if input3 == "red":
            print("It's a room full of fire. Game Over.")
        elif input3 == "yellow":
            print("You found the treasure! You Win!")
        elif input3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
