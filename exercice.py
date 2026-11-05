#Projet  de  Pièrre Papier et Ciseaux
import random

user_choice = int(input("Faites votre  choix, tapez 0 pour  pierre, 1 pour papier ou 2 pour ciseaux : "))
computer_choice = random.randint(0, 2)

if user_choice == computer_choice : 
    print("Égalité ! Vous avez choisi", user_choice, "et l'ordinateur a choisi", computer_choice)
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("Vous avez gagné ! Vous avez choisi", user_choice, "et l'ordinateur a choisi", computer_choice)
else:
    print("Vous avez perdu ! Vous avez choisi", user_choice, "et l'ordinateur a choisi", computer_choice)   
