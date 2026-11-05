"""
#Utilisation de Loops en python
for i in range(5):
    print("Ceci est la boucle numéro", i + 1)


#Liste des fruits
fruits = ["pomme", "banane", "cerise", "orange", "kiwi"]
for fruit in fruits : 
    print(fruit)



#Exemple d'utilisation de la boucle while
student_heights = input("Entrez les hauteurs des étudiants séparées par des espaces : ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights :
    total_height += height
print("la hauteur totale est de :", total_height)

number_of_students = 0
for student in student_heights :
    number_of_students += 1
print("nombre d'étudiants :", number_of_students)

average_height = round(total_height /number_of_students, 2)
print("La hauteur moyenne des étudiants est de :", average_height)
"""
user_score = int(input("Entrez votre score : "))
total = 0 
for number in range(1, (user_score + 1)) :
    total += number
print(total)

for total in range(1, (user_score + 1)) :
    total *=int(user_score + 1) / 2
print(int(total))