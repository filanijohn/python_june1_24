 #function

from pdb import main


def greet():
    print('Hello Adex')


greet()
greet()
greet()
greet()

def greetStudent(name):
    #parameter is the requiremnt
    print('Hello {name}, welocime to class')

greetStudent('Bolu')
greetStudent('Leke')
greetStudent('Adeniyi')
greetStudent('Adex')

def addNum(num1, num2):
    result = num1 + num2
    print(result)

addNum(43, 64)
addNum(43, 34)

def subNum(num1, num2):
    result = num1 - num2
    print(result)

subNum(43, 34)

def mulNum(num1, num2):
    result = num1 * num2
    print(result)

mulNum(43, 34)

def divNum(num1, num2):
    result = num1 / num2
    print(result)

divNum(43, 34)

'''
write a program that an arthmetic function on two numbers based on user option

write a temperature converter program, fehenreit  to celcius and vica versa

write a program that converts dollar to naira and visa versa, using 1640 naira to a dollar as exchange rate
'''
                # solution
#1 
def add(x, y):
    return x + y
 
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 
    if y == 0:
        return "Error! Division by Zero is not allowed."
    else:  
        return x / y
    
print('select operation:')
print('1. Add')
print('2. subtract')
print('3, multiply')
print('4, divide')

choice = input('Enter choice (1/2/3/4): ')

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print('invalid input')


#2
def fehrenheit_to_celsius(fehrenheit):
    celsius = (fehrenheit - 32 ) * 5.0/9.0
    return celsius
def celsius_to_fehrenheit(celsius):
    fehrenheit = (celsius * 9.0/5.0 ) + 32
    return fehrenheit


while True:
    print('Temperature converter')
    print('---------------------')
    print('1. fehrenheit to celsius')
    print('2. celcius to fehrenheit')
    print('3. Exit')
    choice =int(input('Enter your choice (1/2/3):'))

    if choice == 1:
        fehrenheit = float(input('Enter Temperature in fehrenheit:'))
        celsius = fehrenheit_to_celsius(fehrenheit)
        print(f'{fehrenheit} °F is equal to {celsius:.2f}°C')
    elif choice == 2:
        celsius = float(input('2Enter Temperature in celsius:'))
        fehrenheit = celsius_to_fehrenheit(celsius)
        print(f'{celsius} °F is equal to {fehrenheit:.2f}°F') 
    elif choice == '3':
        print('Exit')
        break
    else:
        print('Invalid choice. please enter 1, 2 or 3.')

#3

def dollar_to_naira(dollar, exchange_rate = 1640):
    naira = dollar * exchange_rate
    return naira
def naira_to_dollar(naira, exchange_rate = 1640):
    dollar = naira / exchange_rate
    return dollar

while True:
    print("Currency Converter")
    print("-------------------")
    print("Dollar to Naira")
    print("Naira to Dollar")

choice = int(input("Enter your choice(1/2):"))
if choice == 1:
    dollar = float(input("Enter amount in Dollars:"))
    naira = dollar_to_naira(dollar)
    print(f"${dollar} is equal to ₦{naira:.2f}")
elif choice == 2:
    naira = float(input("Enter amount in Naira"))
    dollar = naira_to_dollar(naira)
    print(f"₦{naira} is equal to ${dollar:.2f}")
else:
    print("Invalid choice. Please enter 1 or 2")

main()