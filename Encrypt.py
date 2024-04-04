from itertools import count
import random

def encryptMessage():
    mess = input("Enter the Message: ")
    publicKey = input("Enter the public key(first number): ")
    n = input("Enter the public key(second number): ")
    newMessage=''
    for i in mess:
        asyncOutput= ord(i) ** int(publicKey) % int(n)
        charRemainder = (asyncOutput % 94) + 33
        charMax = asyncOutput // 94
        for j in range(charMax):
            total= 94
            randomChar=random.randint(33,61)
            newMessage+= chr(randomChar)
            total-=randomChar
            newMessage+=chr(total)
        newMessage+= chr(charRemainder) +' '
    print(newMessage)
    return newMessage


def encryptTextFile():
    fName = input("Enter the file name (Make sure file is in same folder as this): ")
    publicKey = input("Enter the public key(first number): ")
    n = input("Enter the public key(second number): ")
    filePath="./" +fName
    try:
        ofile= open(filePath)
        newMessage=""
        for line in ofile:
            for i in line:
                asyncOutput= ord(i) ** int(publicKey) % int(n)
                charRemainder = (asyncOutput % 94) + 33
                charMax = asyncOutput // 94
                for j in range(charMax):
                    total= 94
                    randomChar=random.randint(33,61)
                    newMessage+= chr(randomChar)
                    total-=randomChar
                    newMessage+=chr(total)
                newMessage+= chr(charRemainder) +' '
        newf = open("./encrypted_"+fName,'w')
        newf.write(newMessage)
    except:
        print("sorry could not encrypt file")
