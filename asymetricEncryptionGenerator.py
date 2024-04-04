from math import factorial
import random

def keysGenerator() :
    primeList= [229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349]
    firstPrime = primeList[random.randint(0,len(primeList)-1)]
    secondPrime=firstPrime
    while secondPrime == firstPrime :
        secondPrime = primeList[random.randint(0,len(primeList)-1)]
    n = firstPrime * secondPrime
    phiN = (firstPrime -1) * (secondPrime-1)
    coprimeN = []
    factorsN =[]
    coprimePhiN=[]
    factorsPhiN =[]
    #find comprimes(n)
    for i in range(2,n+1):
        if n % i == 0 :
            factorsN.append(i)
    for i in range(1,n+1):
        coprimeyes=False
        for factor in factorsN:
            if i % factor == 0:
                coprimeyes= True
        if coprimeyes == False:
            coprimeN.append(i)
    #find coprimes(phiN)
    for i in range(2,phiN+1):
        if phiN % i == 0 :
            factorsPhiN.append(i)
    for i in range(2,phiN):
        coprimeyes=False
        for factor in factorsPhiN:
            if i % factor == 0:
                coprimeyes= True
        if coprimeyes == False:
            coprimePhiN.append(i)
    possiblePublicKeys = []
    for prime in coprimeN :
        if prime in coprimePhiN:
            possiblePublicKeys.append(prime)
    publicKey = possiblePublicKeys[random.randint(0, len(possiblePublicKeys)-1)]
    privateKeyPossiblities =[]
    for i in range(78,4*phiN):
        if (publicKey*i) % phiN == 1:
            privateKeyPossiblities.append(i) 
    privateKey = privateKeyPossiblities[random.randint(0, len(privateKeyPossiblities)-1)]
    print('Public Keys: '+str(publicKey)+", "+str(n))
    print('Private Keys: '+str(privateKey)+", "+str(n))
    #testing
    randNum = random.randint(11,99)
    encryption = (randNum**publicKey) % n
    decryption = (encryption**privateKey) % n
    if randNum == decryption :
        print('keys are functional ' +str(randNum)+', '+str(decryption))
    else :
        print('Do not use keys!!!'+str(randNum)+', '+str(decryption))

