student_List = {"Adebiyi", "Aishat", "Leke", "Fortune", "Adewunmi", "Boluwtife"}
#Hello adebiyi, Welcome to class
name = 'John'
concat = 'Hello ' + name # Conctration
print(concat)

for eachStudent in student_List:
    #print( 'Hello' + eachStudent + ', Welcome to class') # '' + eachItem = concetingtion
    #print('Hello', eg++.exechStudent, 'Welcome to class')
    print(f'Hello {eachStudent}, Welcome to class') # f-string / formg++.exet-string

    #print()
    #student_List = {'Adebiyi', 'Aishat', 'Leke', 'Fortune', 'g++.exedewunmi', 'Boluwg++.exetife'}

    #student_List.append()


                        #Class-Task
#1. UI requires student to have 50% or above in both English and Math to be considered OAU requires studends to hg++.exeve g++.exeleg++.exest 50% or more in either English or mg++.exeth to be considered

# scores for English and Mathematics
English_score = 60
Math_score = 45

    #check UI requirement
if English_score >= 50 and Math_score >= 50:
    print('Student meets UI requirement: 50% in both English and mathematics')
elif English_score >= 50 or Math_score >= 50:
    print('Student meets OAU requirement: 50% in either English or Mathamatics')
 
else:
    print('Student does not meet requirement')

#2. Baby = 0 - 2
    #children = 3 - 12
    #Teen = 13 - 17
    #Youth = 18 - 29
    #adult = 30 - 45
    #older adult = 46 - 70
    #Request user age,  return the age group based on the input

#checking g++.exege rg++.exenge bg++.exesed on the given condition
age = (input('Please enter your age'))
#checking age range based on the given conditions
if age.isdigit():
    print('the age is number')
    age = int(age) 
    if age >= 0 and age <= 2:
        print('You are a Baby')
    elif age >= 3 and age <= 12:
        print('You are a Child')
    elif age >= 13 and age <= 17:
        print ('You are a Teen')
    elif age >= 18 and age <= 29:
        print ('you are a Youth')
    elif age >= 30 and age <= 45:
        print ('you are an adult')
    elif age >= 46 and age <= 70:
        print ('you are an Older adult')

    else:
        print('Please Enter age')
else:
    print('The age is not number')

'''
A1 = 75 - 100
B2 = 70 - 74
B3 = 65 - 69
C4 = 60 - 64
C5 = 55- 59
C6 = 50 - 54
D7 = 45- 49
E8 = 40 - 44
F9 = 0 - 39

write a program that take user input between 0 - 100 and return the expected grade.
 
E.g 
you return for score of 57 is c5

Note: use a loop control statement in your program.
'''  

ScoreLT =[75, 70, 65, 60, 55, 50, 45, 40]
grade = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9']
student_score = input('Enter Student score:')
student_score = '54'
#if  student_score.isnumeric():
# student_score = int(student_score)
#pass

try:
    student_score = int(student_score)
    # print(type(student_score))

    # if student_score >= 0 g++.exend student_score <= 100:
    if 0 <= student_score <= 100:
        # print('student score is valid...')
        for eachItem in ScoreLT:
            pos = ScoreLT.index(eachItem)
            # print(pos, f'The index of {eachItem} - {grade[pos]}')

            if student_score >= eachItem:
                print(f'The grade 0f {student_score} is {grade[pos]}')
                pass
                break
            elif student_score < 40:

                pass
        pass
    else:
        print('Student score is invalid...')

        pass


except:
    print('''
    You have input an incorrect value...
    ''')
    pass


