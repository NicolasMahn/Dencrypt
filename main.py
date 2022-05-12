import json

from cryptography.fernet import Fernet

import Random

RANDOM_INT = Random.numb


def encrypt():
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
                with open(f"Tickets.json", 'w') as f:
                    json.dump(result, f, indent=3)
                f.close()
                with open(f"Key.txt", 'w') as f:
                    if diyKey:
                        f.write(key)
                    else:
                        f.write(str(key)[2:len(str(key)) - 1])
                f.close()
                print("The Result and Key has been saved to Tickets.json and Key.txt")
        else:
            print("Dude, you had one Job. I think you should go back to primary school!")
    else:
        print("Dude, WTF do you know what numbers are?")

    print("\n\n")
    main()


def decrypt():
    sameKey = True
    print("Please enter the Key")
    key = input()
    fernet = Fernet(key)
    while sameKey:
        print("Please enter encrypted Number")
        encNumb = input()
        numb = int(int(fernet.decrypt(bytes(encNumb, encoding="UTF-8")))/RANDOM_INT)
        print(f"The decrypted Number is {numb}")
        print("Would you like to continue with the same Key (Y/n)?")
        answer = input()
        if answer.lower()[:1] == 'n':
            sameKey = False
    main()


def main():
    print("This System encrypts and decrypts Tickets.")
    answer = input("Do you want to encrypt, decrypt or exit (e/D/x)?\n")
    if answer.lower()[:1] == 'e':
        encrypt()
    elif answer.lower()[:1] == 'x':
        pass
    else:
        decrypt()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
