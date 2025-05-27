import random
import string
import sys

all_characters = list(string.ascii_letters + string.digits + string.punctuation)

def passwordGen():
    while True:
        try:
            print("\n" + "="*40)  # Ligne de séparation
            Value = int(input("\nEnter a limit of characters: "))  

            if Value <= 0:
                print("\nMerci d'entrer un nombre positif.")
                continue

            password = "".join(random.choice(all_characters) for _ in range(Value))
            print("\nGenerated Password: " + password + "\n")

            print("="*40)  # Autre séparation
            again = input("\nDo you want to generate another one? (yes/no): ").lower()

            if again == "no":
                print("\nExiting password generator...\n")
                sys.exit()
            elif again != "yes":
                print("\nInvalid input, exiting...\n")
                sys.exit()

        except ValueError:
            print("\nMerci d'entrer une valeur valide.\n")

passwordGen()
