import random
import string

all_characters = list(string.ascii_letters + string.digits + string.punctuation)

limit = 99

def passwordGen():
    while True:
        try:
            print("\n" + "="*40)  # Ligne de séparation
            Value = int(input("Enter a number of characters (limit 99) "))  

            if Value > limit:
                print("LIMIT 99 !!!!!!!!!!!! ")
                continue

            if Value <= 0:
                print("Merci d'entrer un nombre positif.")
                continue

            password = "".join(random.choice(all_characters) for _ in range(Value))
            print("Generated Password: " + password)

            print("="*40)  # Autre séparation
            again = input("Do you want to generate another one? (yes/no): ").lower()

            if again == "no":
                print("Exiting password generator...")
                break
            elif again != "yes":
                print("Invalid input, exiting...")
                break

        except ValueError:
            print("Merci d'entrer une valeur valide.")

passwordGen()
