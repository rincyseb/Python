# Program to encrypt user enterd text
import rsa

#generate public and private key with rsa.newkeys method
publicKey, privateKey = rsa.newkeys(512)

#Accept the message to encrypt
orginalText = input("Enter the text to Encrypt:")

print ("Original text: ", orginalText)
print ("********************************")
#Encrypt the text using rsa.encrypt
encryptText = rsa.encrypt(orginalText.encode(), publicKey)


print ("Encrypted text:", encryptText)
print ("********************************")

#Decrypt the cipher text to using rsa.decrypt method
decryptText = rsa.decrypt(encryptText, privateKey).decode()

#Print Decrypted Text
print ("Decrypted text: ", decryptText)