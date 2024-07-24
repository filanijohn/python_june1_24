import math

def myProgram():
    print('Welcome to our sofware !!!!')
    print('''
        CHOOSE THE NUMBER OF YOUR OPTION BELOW:
          1. Perform an arithematic operation.
          2. Perform a Temperature convertion.
          3. Perform a Currency convertion.
          4. Close program.
        ''')
    option = input('Enter your option:')

    if option == "1":
        print('Perform an arithemetic operation.\n\n')
        print('''
            ENTER THE SYMBOL FOR YOUR OPERATION BELOW:
              1. ADDITION       +
              2. SUBTRATION     -
              3. MULIPLICATION  *
              4. DIVISION       /
              5. SQUARE ROOT
        ''')
        op_list =['+', '-', '*', '/']
        operation = input('Enter oparetion number:')
        num1 = input('Enter number:')

        if operation.strip() in op_list:
            num2 = input('Enter second number:')
            print('\n')
            try:
                print(eval(num1+operation+num2))
            
            except:
                print('you have entered an invalid value\n\n')
        elif operation == '5':
            print('Performing square root')
            try:
                #print(math,sqrt(int(num)))
                print(round(math.sqrt(int(num1))), 1)
                print('\n')
            except:
                print('you have entered an invalid value\n\n')


        # if opreation == '1':
        # result = int(num1) = int(num2)
        # result = eval(num1+'+'num2)
        # '7+8'
        # print(result)
        # recursive
        myProgram()
    elif option == '2':
        print('Perform a Temperature  convertion.\n\n')
        myProgram()
    elif option == '3':
        print('perform a Currency convertion\n\n')
        myProgram()
    else:
        print('Thank you for using our program.')
        pass

# myProgram()


# def destroy();
#   print('Destructive code !!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
#   try:
#      destroy()
#   except RecursionError:
#       print('Exception checked !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
#       destroy()

# destroy()
'''
write a program that a list or range of numbers.
1. checks if the number is an odd number or an even.
2. Below:
    checks if the number is divisible by 3 and print (Fizzy)
    checks if the nuber is divisible by 5 and print (Buzz)
    checks if it's divisible by both 3 and 5, print (FizzBuzz)
    if not divisible by any, print the number.

'''

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} - Even")
    else:
        print(f"{i} - Odd")

for i in range(1, 30):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

