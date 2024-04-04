def decryptMessage():
    mess = input("Copy and paste the encrypted message here: ")
    privateKey = input("Enter the private key(first number): ")
    n = input("Enter the public key(second number): ")
    print("This may take a few minutes")
    newMessage=""
    eachChar= mess.split(' ')
    eachChar=eachChar[:len(eachChar)-1]
    for letterSum in eachChar:
        count=0
        lastChar= letterSum[len(letterSum)-1:]
        letterSum = letterSum[:len(letterSum)-1]
        for letter in letterSum:
            count+= ord(letter)
        count+= ord(lastChar) - 33
        charToAdd = count ** int(privateKey) % int(n)
        newMessage+=chr (charToAdd)
    print(newMessage)
    return newMessage


def decryptTextFile():
    fName = input("Enter the file name (make sure file is in same folder as this): ")
    privateKey = input("Enter the private key(first number): ")
    n = input("Enter the public key(second number): ")
    filePath="./" +fName
    newMessage=""
    print("This may take a few minutes")

    ofile= open(filePath)
    mess= ofile.read()
    eachChar= mess.split(' ')
    eachChar=eachChar[:len(eachChar)-1]
    for letterSum in eachChar:
        count=0
        lastChar= letterSum[len(letterSum)-1:]
        letterSum = letterSum[:len(letterSum)-1]
        for letter in letterSum:
            count+= ord(letter)
        count+= ord(lastChar) - 33
        charToAdd = count ** int(privateKey) % int(n)
        newMessage+=chr (charToAdd)
    newf = open("./Decrypted_"+fName,'w')
    newf.write(newMessage)
    print("Done!")
