#Python list methods
#Pour créer une liste, on utilise des crochets [] et on sépare les éléments par des virgules.
#Exemple :  
ma_liste_de_nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Pour accéder à un élément de la liste, on utilise son index (position) en commençant par 0.    
print(ma_liste_de_nombres[0])  # Affiche 1
print(ma_liste_de_nombres[5])  # Affiche 6  

#Liste de chaînes de caractères
ma_liste_de_noms = ["Alice", "Bob", "Charlie", "David"]

#Accéder à un élément de la liste
print(ma_liste_de_noms[2])  # Affiche "Charlie"
print(ma_liste_de_noms[-1])  # Affiche "David" (dernier élément de la liste)

#Ajouter un élément à la fin de la liste avec append()
ma_liste_de_noms.append("Eve")
print(ma_liste_de_noms)  # Affiche ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

#Insérer un élément à une position spécifique avec insert()
ma_liste_de_noms.insert(1, "Frank")
print(ma_liste_de_noms)  # Affiche ['Alice', 'Frank', 'Bob', 'Charlie', 'David', 'Eve']

#Supprimer un élément de la liste avec remove()
ma_liste_de_noms.remove("Charlie")
print(ma_liste_de_noms)  # Affiche ['Alice', 'Frank', 'Bob', 'David', 'Eve']

#Supprimer un élément à une position spécifique avec pop()
ma_liste_de_noms.pop(2)  # Supprime l'élément à l'index 2 (Bob)
print(ma_liste_de_noms)  # Affiche ['Alice', 'Frank', 'David', 'Eve']

#Trier la liste avec sort()
ma_liste_de_noms.sort()
print(ma_liste_de_noms)  # Affiche ['Alice', 'David', 'Eve', 'Frank']   

#Inverser l'ordre des éléments de la liste avec reverse()
ma_liste_de_noms.reverse() 
print(ma_liste_de_noms)  # Affiche ['Frank', 'Eve', 'David', 'Alice']

#Ajouter plusieurs éléments à la liste avec extend()
ma_liste_de_noms.extend(["Grace", "Heidi"])
print(ma_liste_de_noms)  # Affiche ['Frank', 'Eve', 'David', 'Alice', 'Grace', 'Heidi']

#Methode split() pour diviser une chaîne de caractères en une liste
noms = input("Entrez des noms séparés par des virgules : ")
maliste_de_noms = noms.split(",")
print(maliste_de_noms)  # Affiche la liste des noms entrés par l'utilisateur