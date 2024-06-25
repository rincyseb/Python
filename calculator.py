<<<<<<< HEAD
import sys
#Addition function
def addNumbers(num1, num2):
    return(num1 + num2)
#Subtraction Function
def DiffNumbers(num1, num2):
    return(num1 - num2)
#Multiplication Function
def MultiplyNumbers(num1, num2):
    return(num1 * num2)
#Division Function
def DivideNumbers(num1, num2):
    if (num1 == 0):
        return 0
    elif (num2 == 0):
        print("cannot divide by 0")
    else:
        return(num1 / num2)
#Function to find remainder
def RemainderNumbers(num1, num2):
    return(num1 % num2)
#Main Function to accept numbers    
def main():
    while True:
        num1 = input("Enter first number ")
        num2 = input("Enter second number ")
        operation = input("Enter the type of operation ")
        if num1.isdigit() and num2.isdigit():
            if operation in ['+','-','*','/','%']:
                match(operation):
                    case '+':
                        print(addNumbers(int(num1), int(num2)))
                        break
                    case '-':
                        print(DiffNumbers(int(num1), int(num2)))
                        break
                    case '*':
                        print(MultiplyNumbers(int(num1), int(num2)))
                        break
                    case '/':
                        print(DivideNumbers(int(num1), int(num2)))
                        break
                    case '%':
                        print(RemainderNumbers(int(num1), int(num2)))
                        break
                    case deafult:
                        print("Not a valid Operation") 
                        break   
            else:
                print("Not a Valid operator")       
        else:
            print("Enter Valid Integer")                    
            
if __name__ == '__main__':
    sys.exit(main()) 
=======
import sys
#Addition function
def addNumbers(num1, num2):
    return(num1 + num2)
#Subtraction Function
def DiffNumbers(num1, num2):
    return(num1 - num2)
#Multiplication Function
def MultiplyNumbers(num1, num2):
    return(num1 * num2)
#Division Function
def DivideNumbers(num1, num2):
    if (num1 == 0):
        return 0
    elif (num2 == 0):
        print("cannot divide by 0")
    else:
        return(num1 / num2)
#Function to find remainder
def RemainderNumbers(num1, num2):
    return(num1 % num2)
#Main Function to accept numbers    
def main():
    while True:
        num1 = input("Enter first number ")
        num2 = input("Enter second number ")
        operation = input("Enter the type of operation ")
        if num1.isdigit() and num2.isdigit():
            if operation in ['+','-','*','/','%']:
                match(operation):
                    case '+':
                        print(addNumbers(int(num1), int(num2)))
                        break
                    case '-':
                        print(DiffNumbers(int(num1), int(num2)))
                        break
                    case '*':
                        print(MultiplyNumbers(int(num1), int(num2)))
                        break
                    case '/':
                        print(DivideNumbers(int(num1), int(num2)))
                        break
                    case '%':
                        print(RemainderNumbers(int(num1), int(num2)))
                        break
                    case deafult:
                        print("Not a valid Operation") 
                        break   
            else:
                print("Not a Valid operator")       
        else:
            print("Enter Valid Integer")                    
            
if __name__ == '__main__':
    sys.exit(main()) 
>>>>>>> 8c3f0e114f1d048c9019849cbb8fe973d2f389e2
    