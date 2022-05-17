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
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm

import privat
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
import qrcode

# This int is not uploaded to GitHub, for obvious reasons.
# If you need it please contact me.
RANDOM_INT = privat.numb


def makeTickets(result):
    """
    This methode creates a pdf of tickets
    :param result: TODO
    :return:
    """
    makeFront(result)
    makeBack(result)

def makeBack(result):
    """
    TODO
    :param result:
    :return:
    """
    buffer = BytesIO()
    pdfWriter = canvas.Canvas(buffer)
    pdfWriter.setTitle("Ententickets Rückseite")
    pdfWriter.setPageSize(landscape(A4))

    i = 0
    p = 0
    while i < len(result):
        # pdf.drawImage('Ententickets_Vorderseite_Vorlage.jpg', 0, 0, 297 * mm, 210 * mm)
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 50 * mm, 140 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 140 * mm, 140 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 230 * mm, 140 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 50 * mm, 80 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 140 * mm, 80 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 230 * mm, 80 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 50 * mm, 20 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 140 * mm, 20 * mm, 50 * mm, 50 * mm)
        i += 1
        if i < len(result):
            qrCode = qrcode.make(result.get(i))
            qrCode.save('QR_Code.png')
            pdfWriter.drawImage('QR_Code.png', 230 * mm, 20 * mm, 50 * mm, 50 * mm)
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


def makeFront(result):
    """
    TODO
    :param result:
    :return:
    """
    buffer = BytesIO()
    pdfWriter = canvas.Canvas(buffer)
    pdfWriter.setTitle("Ententickets Vorderseite")
    pdfWriter.setPageSize(landscape(A4))

    i = 0
    p = 0
    while i < len(result):
        pdfmetrics.registerFont(TTFont('an', 'Arial Narrow.ttf'))
        pdfWriter.setFont("an", 11)
        pdfWriter.setFillColorRGB(0.4375, 0.4414, 0.4492)
        # pdf.drawImage('Ententickets_Vorderseite_Vorlage.jpg', 0, 0, 297 * mm, 210 * mm)
        i += 1
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
                except Exception:
                    print("Dude, Like an accepted key, not this bs")
                diyKey = True
            else:
                key = Fernet.generate_key()
                diyKey = False
            fernet = Fernet(key)
            if not diyKey:
                key = str(key)[2:len(str(key)) - 1]
            for numb in numbs:
                encNumb = fernet.encrypt(str(RANDOM_INT * numb).encode())
                encNumb = str(encNumb)[2:len(str(encNumb)) - 1]
                print(f"{numb} has been encrypted to {encNumb} with the Key: {key}")
                result[numb] = encNumb

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
                print("\nShould I directly create tickets with corresponding numbers and qr codes (Y/n)?")
                answer = input()
                if answer.lower()[:1] != 'n':
                    makeTickets(result)
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
