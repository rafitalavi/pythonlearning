# Simple Calculator Genarate Program 
# MD.BODRUL ISLAM
# Reg: 813

def add(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y!=0:
        return x/y

print("\nWelcome to Simple Calculator : ")
print("1-> Addition: ")
print("2-> Subtraction: ")
print("3-> Multiplication: ")
print("4-> Division:")

choice = int(input("\nEnter Your Choice : "))

num1 = float(input("\nEnter the first Value : "))
num2 = float(input("Enter the second Value : "))
print('\nCalculator Output is : ')
if choice == 1:
    print(num1,"+",num2," = ",add(num1,num2))
elif choice == 2:
    print(num1,"-",num2," = ",substraction(num1,num2))
elif choice == 3:
    print(num1,"*",num2," = ",multiplication(num1,num2))
elif choice == 4:
    print(num1,"/",num2," = ",division(num1,num2))
    
else:
    print("\nInvalid input...!")

print('\n\tThank You Sir! \nSimple Calculator Program is Succesfully Done.''\n')    