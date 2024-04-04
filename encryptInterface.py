from tkinter.tix import InputOnly
import decrypt
import Encrypt
import asymetricEncryptionGenerator

print("Hello welcome to Troy Daniels encryption interface")
print("This uses asymmetric cryptography and will pop out pubic and private keys to use")
inputType = "nope"
needKeys = "nope"
crypt= "nope"
while needKeys!="n" and needKeys!="y":
    needKeys = input("Do you need a new set of keys (enter 'y' or 'n'): ")
if needKeys == "y":
    print("this may take a few minutes")
    asymetricEncryptionGenerator.keysGenerator()
    print("write these down!!!")
while inputType!="file" and inputType!="message":
    inputType= input("Would you like to use a file or message (enter 'file' or 'message'):")
while crypt!="encrypt" and crypt!="decrypt":
    crypt= input("Would you like to encrypt or decrypt a message (enter 'encrypt' or 'decrypt'):")

if inputType == "file" :
    if crypt == "encrypt":
        Encrypt.encryptTextFile()
    else:
        decrypt.decryptTextFile()
else:
    if crypt == "encrypt":
        Encrypt.encryptMessage()
    else:
        decrypt.decryptMessage()