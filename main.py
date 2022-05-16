"""
This system decrypts and encrypts tickets or other int arrays.
For example 1 can be encrypted to a byte code like this:
gAAAAABigrWsV-vesiIvrgI0CiY-X0uDE-Ot-SkpXla8DQ9D0q2SqEhEotXi-BDe-fW1R2ZwP3cvVVWpocchg2m-Ku3PcuGlrYQC2TjX8rTvIGSNOCDufuI=
which can be decrypted with a key like this one:
msV-x2CarhEaAM5EaDPZpwupUNm6kO8Wu2SY_rpWZKQ=
"""

import json
import subprocess
from cryptography.fernet import Fernet
import random

# This int is not uploaded to GitHub, for obvious reasons.
# If you need it please contact me.
RANDOM_INT = random.numb


def encrypt():
    """
    This methode encrypts int arrays
    """
    save = False
    print("Would you like to save the encoded Numbers and the Key (Y/n)?")
    print("This is highly recommended!")
    answer = input()
    if answer.lower()[:1] != 'n':
        save = True

    print("From what natural Number to what natural Number would you like to encrypt?")
    first = input("Starting Number (include): ")
    last = input("Last Number (include): ")
    print(f"Ok, creating encrypted Integers from [{first},{last}]")

    if first.isnumeric() and last.isnumeric():
        first = int(first)
        last = int(last)
        if last >= first > 0:
            result = dict()
            numbs = [*range(first, last + 1, 1)]

            print("Would you like to use a pre defined key (not recommended) (y/N)")
            answer = input()
            if answer.lower()[:1] == 'y':
                key = input("Key: ")
                diyKey = True
            else:
                key = Fernet.generate_key()
                diyKey = False
            fernet = Fernet(key)
            for numb in numbs:
                encNumb = fernet.encrypt(str(RANDOM_INT * numb).encode())
                if diyKey:
                    print(f"{numb} has been encrypted to {str(encNumb)[2:len(str(encNumb)) - 1]} with the Key: "
                          f"{key}")
                else:
                    print(f"{numb} has been encrypted to {str(encNumb)[2:len(str(encNumb)) - 1]} with the Key: "
                          f"{str(key)[2:len(str(key)) - 1]}")
                result[numb] = str(encNumb)[2:len(str(encNumb)) - 1]

            if save:
                with open("output/Tickets.json", 'w') as f:
                    json.dump(result, f, indent=3)
                f.close()
                with open("output/Key.txt", 'w') as f:
                    if diyKey:
                        f.write(key)
                    else:
                        f.write(str(key)[2:len(str(key)) - 1])
                f.close()
                print("\nThe Result and Key has been saved to Tickets.json and Key.txt")
                # print("You'll find them in: %ProgramData%/Dencrypt/output")
                subprocess.Popen(f'explorer "output"')
        else:
            print("Dude, you had one Job. I think you should go back to primary school!")
    else:
        print("Dude, WTF do you know what numbers are?")
    menu()


def decrypt():
    """
    This methode decrypts encNumbers with the help of a key
    """
    sameKey = True
    print("Please enter the Key")
    key = input()
    try:
        fernet = Fernet(key)
    except Exception:
        print("Dude, this key isn't valid")
        menu()
    while sameKey:
        print("Please enter the encrypted Number")
        encNumb = input()
        try:
            numb = int(int(fernet.decrypt(bytes(encNumb, encoding="UTF-8"))) / RANDOM_INT)
            print(f"The decrypted Number is {numb}")
            print("Would you like to continue with the same Key (Y/n)?")
        except Exception:
            print("Dude, You did something wrong, maybe the encrypted Number isn't valid?")
            print("Don't blame this on me!")
            print("Do you want to try again (Y/n)?")
        answer = input()
        if answer.lower()[:1] == 'n':
            sameKey = False
    menu()


def menu():
    """
    This methode handles the menu
    """
    print("\n")
    answer = input("Do you want to decrypt, encrypt or exit (D/e/x)?\n")
    if answer.lower()[:1] == 'e':
        encrypt()
    elif answer.lower()[:1] == 'x':
        pass
    else:
        decrypt()


def main():
    """
    this method initialises the program, and then opens the menu
    """
    print("This System encrypts and decrypts Tickets.")
    menu()


if __name__ == '__main__':
    main()
