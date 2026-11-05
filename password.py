#Générateur de mot de passe.
import random
import tkinter as tk

#Définir les caractères possibles pour le mot de passe
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '_', '-', '=', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '~ ']

#Fonction pour générer le mot de passe
def generate_password():
    nr_letters = int(letter_entry.get())
    nr_symbols = int(symbol_entry.get())
    nr_numbers = int(number_entry.get())

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

    password_label.config(text=password)



#Créer l'interface graphique
root = tk.Tk()
root.title("Générateur de mot de passe")
root.config(bg="#4206CE")

#Créer les widgets
letter_label = tk.Label(root, text="Nombre de lettres :")
letter_entry = tk.Entry(root)
symbol_label = tk.Label(root, text="Nombre de symboles :")
symbol_entry = tk.Entry(root)
number_label = tk.Label(root, text="Nombre de chiffres :")
number_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Générer le mot de passe", command=generate_password)
password_label = tk.Label(root, text="")

#Placer les widgets
letter_label.grid(row=0, column=0)
letter_entry.grid(row=0, column=1)
symbol_label.grid(row=1, column=0)
symbol_entry.grid(row=1, column=1)
number_label.grid(row=2, column=0)
number_entry.grid(row=2, column=1)
generate_button.grid(row=3, columnspan=2)
password_label.grid(row=4, columnspan=2)

#styler les widgets
letter_label.config(font=("Arial", 12)) 
symbol_label.config(font=("Arial", 12))
number_label.config(font=("Arial", 12))
password_label.config(font=("Arial", 12))

#configurer la taille de la fenêtre
root.geometry("400x200")

#couleur de fond
root.config(bg="#f0f0f0")

#Lancer l'application
root.mainloop()

