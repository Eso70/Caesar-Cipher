from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("CaesarCipher")
root.geometry("363x373")
root.iconbitmap("C:\\Esma3il\\Programming\\Python\\CaesarCipher\\shield.ico")


SYMBOLS = "A !#@bcdEFGhIGK l$&^mnOPQrSTUvWXY z%*:;',.\\a BCDefgHigkL MNopqRstuVwxy Z"
key = StringVar()

def reset():
    key.set("")
    txt_1.delete("1.0", END)

def encrypt():
    translated = ""
    input_text = txt_1.get("1.0", END).strip()
    key_value = int(key.get())  # Convert key to integer
    for char in input_text:
        if char in SYMBOLS:
            symbolIndex = SYMBOLS.find(char)
            translatedIndex = (symbolIndex + key_value) % len(SYMBOLS)  # Encryption
            translated += SYMBOLS[translatedIndex]
        else:
            translated += char
    txt_1.delete("1.0", END)
    txt_1.insert("1.0", translated)

def decrypt():
    translated = ""
    input_text = txt_1.get("1.0", END).strip()
    key_value = int(key.get())  # Convert key to integer
    for char in input_text:
        if char in SYMBOLS:
            symbolIndex = SYMBOLS.find(char)
            translatedIndex = (symbolIndex - key_value) % len(SYMBOLS)  # Decryption
            translated += SYMBOLS[translatedIndex]
        else:
            translated += char
    txt_1.delete("1.0", END)
    txt_1.insert("1.0", translated)


#Creating
lbl_1 = Label(root, text="Enter your text for encryption or decryption", font=("calbri", 13, "bold"), anchor="nw")
txt_1 = Text(root, font=("Poppins", 23), bg="white", width=21, height=4)
lbl_2 = Label(root, text="Enter your key for encryption or decryption", font=("calbri", 13, "bold"), anchor="nw")
ety_1 = Entry(root, width=21, textvariable=key, font=("Poppins", 23), show="*")
btn_1 = Button(root, text="Decryption", font=("Poppins", 15, "bold"), bg="black", fg="white", width=14, command=decrypt)
btn_2 = Button(root, text="Encryption", font=("Poppins", 15, "bold"), bg="green", fg="white", width=14, command=encrypt)
btn_3 = Button(root, text="Reset", font=("Poppins", 15, "bold"), bg="blue", fg="white", width=29, command=reset)
btn_4 = Button(root, text="Quit", font=("Poppins", 15, "bold"), bg="red", fg="white", width=29, command=root.quit)

#Showing
lbl_1.grid(row=0, column=0)  # Label 1
txt_1.grid(row=1, column=0)  # Text Box
lbl_2.grid(row=2, column=0)  # Label 2
ety_1.grid(row=3, column=0)  # Entry Box (Input)
btn_1.place(x=2, y=235)  # Button 1
btn_2.place(x=183, y=235)  # Button 2
btn_3.place(x=3, y=280)  # Button 3
btn_4.place(x=3, y=325)  # Button 4

root.mainloop()
