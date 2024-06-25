import random
import sys
#convert the sting to unicode value
def encrypt(orgText):
    unicodeValueList =[]
    for char in orgText:
        unicodeValueList.extend(ord(num) for num in char)
    #print (" Unicode value of string",unicodeValueList)
    #generate a random value
    secretNum=random.randint(1,100)
    print("secret number:",secretNum)

    #ecrypt the unicode values with secret value
    encryptText=""
    #encryptUnicdList =[]
    for val in unicodeValueList:
        #print("Value:",val)
        newUnicdVal = int(val) + int(secretNum)
        #print("new Unicode Value:",newUnicdVal)
        #encryptUnicdList.extend(newUnicdVal)
        encryptText = encryptText + chr(newUnicdVal)

    #Print encypted text
    #print ("New unicode list:",encryptUnicdList) 
    return(encryptText, secretNum) 
    
def decrypt(encryptText, secretNum):
    #Decrypted Unicode List
    decrUnicodeValueList =[]
    for char in encryptText:
        decrUnicodeValueList.extend(((ord(num) - secretNum)for num in char))

    #Decrypted Unicode List
    decrText = "" 
    for val in decrUnicodeValueList: 
        decrText = decrText + chr(val)
    return(decrText) 
def main():
    # Accept input text
    orgText=input ("Enter text to encrypt:")
    #calling encrypt function
    encryptText , secretNo = encrypt(orgText)
    print ("encrypted text:",encryptText)
    decrText = decrypt(encryptText,secretNo)
    print ("Decrypted text: ",decrText)

if __name__ == '__main__':
    sys.exit(main()) 
