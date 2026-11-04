#Random Module, Day 4

import random

#On peut utiliser la fonction randint() pour générer un entier aléatoire entre deux bornes inclusives. Par exemple, pour générer un entier aléatoire entre 1 et 20, on peut utiliser le code suivant :
random_integer = random.randint(1, 20)
print(random_integer)

#On peut également utiliser la fonction random() pour générer un nombre flottant aléatoire entre 0 et 1. Par exemple, pour générer un nombre flottant aléatoire entre 0 et 1, on peut utiliser le code suivant :
random_float = random.random()
print(random_float)

#NB : La fonction random() ne prend pas d'arguments et renvoie un nombre flottant aléatoire compris entre 0 et 1. Pour générer un nombre flottant aléatoire dans une plage spécifique, on peut multiplier le résultat de random() par la plage souhaitée. Par exemple, pour générer un nombre flottant aléatoire entre 0 et 5, on peut utiliser le code suivant :
random_float_range = round(random.random() * 5, 2)
print(random_float_range)

#Remarque : La fonction round() est utilisée pour arrondir le nombre flottant à deux décimales.


#Exercice : Créez un programme qui génère un nombre aléatoire entre 1 et 100 et demande à l'utilisateur de deviner ce nombre. Le programme doit indiquer si le nombre deviné est trop bas, trop haut ou correct. Le programme doit continuer à demander à l'utilisateur de deviner jusqu'à ce qu'il trouve le bon nombre.
print("Bienvenue dans le jeu de devinette !")
nombre_secret = random.randint(1, 100)
nombre_devine = 0
while nombre_devine != nombre_secret :
    nombre_devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if nombre_devine < nombre_secret : 
        print("Trop bas ! Essayez encore. ")
    elif nombre_devine > nombre_secret : 
        print("Trop haut ! Essayez encore. ")
    else :
        print("Félicitations ! Vous avez deviné le nombre secret :", nombre_secret)
