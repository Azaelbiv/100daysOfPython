#Projet  de  Pièrre Papier et Ciseaux
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
