#Utilisation des fonction en python

def greetings(name, location) :
    print(f"Hello {name}")
    print(f"How do you do {name} ?")
    print(f"How is it going in {location}")

name = input("Enter your name : ")
location = input("Enter your location : ")
greetings(location=location, name=name)

#fonction to calculate the number of cans of paint.
#First we import the maths module:
import math

def paint_calc(height, width, cover):
    area = height*width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

height = float(input("Enter the height value :"))
width = float(input("Enter the width value : "))
cover = float(input("Enter the cover value : "))

paint_calc(height=height, width=width, cover=cover)