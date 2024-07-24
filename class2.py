y = 10
y2 = 10.3
y3 = 7e46

# print(type(y))
# print(type(y2))
# print(type(y3))

b1 = True
b2 =False

#collection/Array : List, Turple, Set, Dict
student_List =['Adebiyi', 'Adewunmi', 'Aishat', 'Leke', 'Fortune', 'Boluwatife']
# print(student_List[0:3])
# print(student_List[1][3:8])

# print(student_List)
student_List.pop() #removes the last element 
# print(student_List)
#List 
hL = ['Parach', 343, 'Adewunmi', True, 34.1, ['Boy', 'Girl']]
student_List.sort()
# print(student_List)

student_List.reverse()
# print(student_List)
                        #Assignment
greeting = ['Good morning', 'Good Evening', 'Good Afternoon']
greeting.append('Good Night')
print(greeting) # it add  an element to end of the list

fruits = ['orange', 'Apple', 'Banana', 'pinapple']
fruits.clear()
print(fruits) #This method use to delete or clear all the element from the list

fruits = ['orange', 'Apple', 'Banana', 'pinapple']
fruits.copy()
print(fruits) #It return the copy of the list

number = [1, 4, 8, 5, 4, 0, 4, 3]
y = number.count(4)
print(y) #it returns number of the element in the specified value 

point = [1, 2, 3, 4, 5]
topic =['Mathematics', 'English', 'physic', 'Biology']
point.extend(topic)
print(point) #it add the specified list elements to the end of the current lists

text = [ 7, 10, 4, 12, 5, 12]
z = text.index(12)
print(z) #this method only returns the first occurence of the value

Names =['olamide', 'folurunsho', 'damilola']
Names.insert(2, "olusola")
print(Names) #This method inserts the specified value at the specified poistion

number =[10, 5, 7,  6]
number.remove(7)
print(number) #This method remove the elements with the specified value

#Tuple
student_Turple = ['Adebiyi', 'Adewunmi', 'Aishat', 'Leke', 'Fortune', 'Boluwatife']
# print(student_Turple[3])
# print(student_Turple[:3])

               


#Bracket / Braces
# () - curve
# [] - square
# {} - curly
# <> - Angle

# Set
student_Set ={'Adebiyi', 'Adewunmi', 'Aishat', 'Leke', 'Fortune', 'Boluwatife'}
print(student_Set)

print(student_List)

for eachItem in student_List:

    print(eachItem)
    print(eachItem[0:3])

    #print the first three letter of each items

