import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']


def cipher(choice,plain_text,shift_amount):
    if choice == "encode" or choice == "en":
        enText = ""
        for letter in plain_text:
            letterIndex = alphabet.index(letter)

            if letterIndex + shift <= 27:
                enText += alphabet[letterIndex + shift_amount]
            else:
                shiftedIndex = letterIndex + shift_amount
                shiftedIndex = shiftedIndex - len(alphabet)
                enText += alphabet[shiftedIndex]
        os.system("cls")
        print(f"\033[31m{art.logo}\033[00m")
        print(f"The encoded Text is '{enText}'")
    elif choice == "decode" or choice == "de":
        deText = ""
        for letter in plain_text:
            letterIndex = alphabet.index(letter)

            if letterIndex - shift >= 0:
                deText += alphabet[letterIndex - shift_amount]
            else:
                shiftedIndex = letterIndex - shift_amount
                shiftedIndex = shiftedIndex + len(alphabet)
                deText += alphabet[shiftedIndex]
        os.system("cls")
        print(f"\033[31m{art.logo}\033[00m")
        print(f"The decoded Text is '{deText}'")
    else:
        return "Error!"

run = True
while run:
    print(f"\033[31m{art.logo}\033[00m")
    direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    cipher(direction,text,shift)
    
    rerun = input("\nDo you want to rerun (Y/N)\n>>>")
    
    if rerun == "N" or rerun == "n" or rerun == "no":
        run = False
    os.system("cls")
