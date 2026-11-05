#Projet  de  Pièrre Papier et Ciseaux
"""
import random

games_choices = ["pierre", "papier", "ciseaux"]
user_choice = int(input("Faites votre  choix, tapez 0 pour  pierre, 1 pour papier ou 2 pour ciseaux : "))
computer_choice = random.randint(0, 2)

while user_choice < 0 or user_choice >=3 : 
    print("Choix invalide ! Veuillez choisir 0, 1 ou 2.")
    user_choice = int(input("Faites votre  choix, tapez 0 pour  pierre, 1 pour papier ou 2 pour ciseaux : "))

if user_choice == computer_choice : 
    print("Égalité ! Vous avez choisi", games_choices[user_choice], "et l'ordinateur a choisi", games_choices[computer_choice])
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("Vous avez gagné ! Vous avez choisi", games_choices[user_choice], "et l'ordinateur a choisi", games_choices[computer_choice])
else:
        print("Vous avez perdu ! Vous avez choisi", games_choices[user_choice], "et l'ordinateur a choisi", games_choices[computer_choice])   


#Exercice 2 : The FizzBuzz Problem
frizzbuzz = 0
frizz = 0
buzz = 0
for number in range(1, 101):
    if number %3 == 0 and number % 5 == 0 :
        frizzbuzz += 1
        print("FrizzBuzz :", frizzbuzz)
    elif number % 3 ==0 :
        frizz += 1
        print("Frizz :", frizz)
    elif number % 5 == 0:
        buzz += 1
        print("Buzz :", buzz)
    else : 
        number += 1
print("Total FrizzBuzz :", frizzbuzz)
print("Total Frizz :", frizz)
print("Total Buzz :", buzz)
print("nombre de nombres qui ne sont ni Frizz ni Buzz :", number - (frizzbuzz + frizz + buzz))
"""

#Exercice 3 : Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '_', '-', '=', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '~ ']

print("Bienvenue dans le générateur de mot de passe !")
nr_letters = int(input("Combien de lettres voulez-vous dans votre mots de passe ?\n"))
nr_symbols = int(input(f"Combien de symboles voulez-vous ?\n"))
nr_numbers = int(input(f"Combien de chiffres voulez-vous ?\n"))

password_list = []
for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("\nVoici votre mot de passe généré aléatoirement !")
print(password)