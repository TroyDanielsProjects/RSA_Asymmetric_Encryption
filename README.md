# asymmetric-encryption
Asymmetric Encryption Program. Generate public and private keys. Encrypt and decrypt files using keys.
If you would like to find out more about Asymmetric Encryption watch https://youtu.be/AQDCe585Lnc .
Make sure that all files are in the same folder.
The UI of the program is encryptInterface.py
## To see how it works
# Encryption
1.) There is already a test file you can use with a set message (inspect message in file = "crypt_test.text". If you would like to set your own message follow step 1.a) below. Otherwise skip <br>
1.a) First create a new text file in the same folder (Name the file anything) and then write a message in the file (FYI- the longer the message the more compute necessary) <br>
2.) To run program - open terminal at folder. type command "python3 encryptInterface.py" <br>
2.) follow the prompts, generate a new set of keys and make sure to save them <br>
3.) for the next prompt type "file" (getting the encrypted message in the console is messy)<br>
4.) then "encrypt" <br>
5.) Next, type in the name of the file you are encrypting (if you did not create a new file "crypt_test.txt")
6.) enter your generated public key (If you notice there are two numbers for the public key. for the first prompt just enter the first number. Second prompt => second number) <br>
7.) You will see a new file created ("encrypted_{file name}). Feel free to inspect the enctypted file! <br>

# Decryption <br>
1.)  run program again - open terminal at folder. type command "python3 encryptInterface.py" <br>
2.) type "n" as you already have a set of keys (need to use those!) <br>
3.) for the next prompt type "file" <br>
4.) then "decrypt" <br>
5.) Next, type in the name of the file you are decrypting (if you did not create a new file "encrypted_crypt_test.txt") <br>
6.) enter your saved private key (If you notice there are two numbers for the private key. for the first prompt just enter the first number. Second prompt => second number) <br>
7.) Inspect the new txt file (message inside should be the same as the original message. If not, check that you entered the keys correctly- 1 wrongly entered number will cause  jiberish!) <br>

Created by Troy Daniels
