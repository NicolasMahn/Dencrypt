"""
:author NicolasMahn
This system decrypts and encrypts tickets or other int arrays.
For example 1 can be encrypted to a byte code like this:
gAAAAABigrWsV-vesiIvrgI0CiY-X0uDE-Ot-SkpXla8DQ9D0q2SqEhEotXi-BDe-fW1R2ZwP3cvVVWpocchg2m-Ku3PcuGlrYQC2TjX8rTvIGSNOCDufuI=
which can be decrypted with a key like this one:
msV-x2CarhEaAM5EaDPZpwupUNm6kO8Wu2SY_rpWZKQ=
"""

import json
import os
import subprocess
from cryptography.fernet import Fernet
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm

import privat
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
import qrcode
from os.path import exists

# This int is not uploaded to GitHub, for obvious reasons.
# If you need it please contact me.
RANDOM_INT = privat.numb
decryptedNumbs = set()

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def makeTickets(result):
    """
    This methode creates a pdf of tickets
    """
    makeFront(result)
    makeBack(result)


def makeBack(result):
    """
    This method makes the back of the pdf tickets
    """
    buffer = BytesIO()
    pdfWriter = canvas.Canvas(buffer)
    pdfWriter.setTitle("Ententickets Rückseite")
    pdfWriter.setPageSize(landscape(A4))

    i = 1000000
    max = 0
    keys = result.keys()
    for key in keys:
        if i > key:
            i = key
        if max < key:
            max = key
    p = 0
    while i <= max:
        if i <= max:
            pdfWriter.drawCentredString(255 * mm, 140 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 230 * mm, 144 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(165 * mm, 140 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 140 * mm, 144 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(75 * mm, 140 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 50 * mm, 144 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(255 * mm, 80 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 230 * mm, 84 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(165 * mm, 80 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 140 * mm, 84 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(75 * mm, 80 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 50 * mm, 84 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(255 * mm, 20 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 230 * mm, 24 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(165 * mm, 20 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 140 * mm, 24 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        i += 1
        if i <= max:
            pdfWriter.drawCentredString(75 * mm, 20 * mm, f"{i:04d}")
            qrCode = qrcode.make(result.get(i))
            qrCode.save(f'QR_Code{i}.png')
            pdfWriter.drawImage(f'QR_Code{i}.png', 50 * mm, 24 * mm, 50 * mm, 50 * mm)
            os.remove(f"QR_Code{i}.png")
        pdfWriter.showPage()
        p += 1
        i += 1

    pdfWriter.save()

    buffer.seek(0)
    pdfNew = PdfFileReader(buffer)
    tmp = buffer.getvalue()
    open('tmp.pdf', 'wb').write(tmp)
    background = PdfFileReader(open("Ententickets_Rueckseite_Vorlage.pdf", "rb"))
    pdf = PdfFileWriter()

    i = 0
    while p > i:
        page = pdfNew.getPage(i)
        page.mergePage(background.getPage(0))
        pdf.addPage(page)
        i += 1

    outputStream = open("output/Ententickets_Rueckseite.pdf", "wb")
    pdf.write(outputStream)
    outputStream.close()
    os.remove("tmp.pdf")


def makeFront(result):
    """
    This method makes the front of the pdf tickets
    """
    buffer = BytesIO()
    pdfWriter = canvas.Canvas(buffer)
    pdfWriter.setTitle("Ententickets Vorderseite")
    pdfWriter.setPageSize(landscape(A4))

    i = 1000000
    max = 0
    keys = result.keys()
    for key in keys:
        if i > key:
            i = key
        if max < key:
            max = key
    p = 0
    while i <= max:
        pdfmetrics.registerFont(TTFont('an', 'Arial Narrow.ttf'))
        pdfWriter.setFont("an", 11)
        pdfWriter.setFillColorRGB(0.4375, 0.4414, 0.4492)

        pdfWriter.drawCentredString(50 * mm, 165.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(140 * mm, 165.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(230 * mm, 165.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(50 * mm, 105.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(140 * mm, 105.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(230 * mm, 105.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(50 * mm, 45.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(140 * mm, 45.2 * mm, f"{i:04d}")
        i += 1
        pdfWriter.drawCentredString(230 * mm, 45.2 * mm, f"{i:04d}")
        pdfWriter.showPage()
        p += 1
        i += 1

    pdfWriter.save()

    buffer.seek(0)
    pdfNew = PdfFileReader(buffer)
    tmp = buffer.getvalue()
    open('tmp.pdf', 'wb').write(tmp)
    background = PdfFileReader(open("Ententickets_Vorderseite_Vorlage.pdf", "rb"))
    pdf = PdfFileWriter()

    i = 0
    while p > i:
        page = pdfNew.getPage(i)
        page.mergePage(background.getPage(0))
        pdf.addPage(page)
        i += 1

    outputStream = open("output/Ententickets_Vorderseite.pdf", "wb")
    pdf.write(outputStream)
    outputStream.close()
    os.remove("tmp.pdf")


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
                try:
                    key = input("Key: ")
                    if key.lower()[:1] == 'p':
                        key = privat.key
                except Exception:
                    print("Dude, Like an accepted key, not this bs")
            else:
                key = Fernet.generate_key()
                print(key)
            fernet = Fernet(key)
            key = str(key)
            for numb in numbs:
                encNumb = fernet.encrypt(str(RANDOM_INT * numb).encode())
                encNumb = str(encNumb)
                print(f"{numb} has been encrypted to {encNumb} with the Key: {key}")
                result[numb] = encNumb

            if save:
                with open("output/Tickets.json", 'w') as f:
                    json.dump(result, f, indent=3)
                f.close()
                with open("output/Key.txt", 'w') as f:
                    f.write(key)
                f.close()
                print("\nThe Result and Key has been saved to Tickets.json and Key.txt")
                # print("You'll find them in: %ProgramData%/Dencrypt/output")
                print("\nShould I directly create tickets with corresponding numbers and QR codes (Y/n)?")
                answer = input()
                if answer.lower()[:1] != 'n':
                    makeTickets(result)
                subprocess.Popen(f'explorer "output"')
        else:
            print("Dude, you had one Job. I think you should go back to primary school!")
    else:
        print("Dude, WTF do you know what numbers are?")
    menu()


def saveNumb(numb):
    """
    This method saves the decrypted numbs to a result json so when they are scanned again, the system knows it
    """
    global decryptedNumbs

    decryptedNumbs.add(numb)

    if exists(f"results.json"):
        file = open(f"results.json")
        results = json.load(file)
        file.close()
    else:
        results = list()

    results.append(numb)

    if len(results) > 0:
        with open(f"results.json", "w") as outfile:
            outfile.write(json.dumps(results))


def decrypt():
    """
    This methode decrypts encNumbers with the help of a key
    """
    global decryptedNumbs

    if exists(f"results.json"):
        file = open(f"results.json")
        results = json.load(file)
        file.close()
        for r in results:
            decryptedNumbs.add(r)

    sameKey = True
    print("Please enter the Key")
    key = input()
    if key.lower()[:1] == 'p':
        key = privat.key
    try:
        fernet = Fernet(key)
    except Exception:
        print("Dude, this key isn't valid")
        sameKey = False
    while sameKey:
        print("Please enter the encrypted Number or type stop to stop")
        encNumb = input()
        if encNumb.lower()[:4] == 'stop':
            break
        if len(encNumb) == 123:
            encNumb = encNumb[2:122]
        try:
            numb = int(int(fernet.decrypt(bytes(encNumb, encoding="UTF-8"))) / RANDOM_INT)
            # print("Would you like to continue with the same Key (Y/n)?")
            if numb in decryptedNumbs:
                print(f"{O}{numb} is a Duplicate, this Ticket was already scanned{W}")
            else:
                print(f"{G}The decrypted Number is {numb}{W}")
                saveNumb(numb)
        except Exception:
            print(f"{R}The encrypted Number isn't valid!{W}")
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
