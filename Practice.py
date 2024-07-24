'''
write a program that takes a list of integers as input and returns the sum of all the integers in the list
write a program that takes a list of integers as input and returns the average of all the integers in the list
write a function that takes a string as input and returns the length of the string.
write a function that takes a list of integers as input and returns the maximum value in the list
write a program that takes a list of integers as input and returns a mew list that contains only the even integers from orginal list
write a program that takes two lists of integers as input and returns a new list that contains the intersection of the two lists(i.e, the elements that are pressent in both lists)
write a program that takes two lists of integers as input and returns a new list that contains the squres of all the integers in the original list
write a function that takes two lists of integers as input and returns a sum of the two integers
write a program that takes two lists of integers as input and returns the products of all the integers in the list
write a program that takes two lists of strings as input and returns a new list that contains only the strings that start with the letter 'a'.
'''

                              #solution
#1. write a program that takes a list of integers as input and returns the sum of all the integers in the list

from itertools import product
from pdb import main


def sum_of_integers(int_list):
    return sum(int_list)

# Main Program:
if __name__ == "_main_":
    # Get a list of integers from the user
    user_input = input("Enter a list of integers seperated by spaces: ")

   #Split the input string into a list of strings
    str_list = user_input.split() 

    #convert the list of the strings to a list of integers
    int_list = [int(num) for num in str_list]

    #calculate the average of the integers
    total_sum = sum_of_integers(int_list)

    #print the sum of the integers 
    print(f"The sum of the integers in the list is {total_sum}")


#2. write a program that takes a list of integers as input and returns the average of all the integers in the list
def average_of_integers(int_list):
    if len(int_list) == 0:
        return 0
    return sum(int_list) / len(int_list)

#main program
if __name__ == "_main_":
    # Get a list of integers from the user
    user_input = input("Enter a list of integers seperated by spaces: ")

    #Split the input string into a list of strings
    str_list = user_input.split()

    #convert the list of the strings to a list of integers
    int_list = [int(num) for num in str_list]

    #calculate the average of the integers
    average = average_of_integers(int_list)

    #print the average
    print(f"The average of the integers in the list is {average}")



#3. write a function that takes a string as input and returns the length of the string.
def get_string_length(input_string):
    return len(input_string)
#Main program:
if __name__ == "_main_":
    user_input = input("Enter a string")
    length_of_string = get_string_length(user_input)
    print(f"The length of the string is: {length_of_string} ")   

'''How it work:
1. The 'get_string_length' function takes a string as input and returns its length using the 'len()' function.
2. in the main program, the 'input()' function is used to get a string from the user.
3. The 'get_string_length' function is called with the user-provided string, and the length of the string is printed
'''

#4. write a function that takes a list of integers as input and returns the maximum value in the list
def find_max_value(numbers):
    if not numbers:
        raise ValueError("The list is Empty")
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
        return max_value

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(find_max_value(numbers))
# This function iterates through the list of the numbers, compares each number to the current maximum value, and updates the maximum values if a larger number is found. if the list is empty, it raise a 'valueError'.

#5. write a program that takes a list of integers as input and returns a mew list that contains only the even integers from orginal list.

def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)
# This function uses a list comprehension to iterate through the input list, checks if each number is even using the modulo operator '%', and includes it in the new list if it is.

#6. write a program that takes two lists of integers as input and returns a new list that contains the intersection of the two lists(i.e, the elements that are pressent in both lists)

def intersect_lists(list1, list2):
    # using set intersection to find common elements
    intersection = list(set(list1) & set(list2))
    return intersection

 # Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = intersect_lists(list1, list2)
print(intersection)
# the function converts the input lists to sets and then uses the '&' operator to find the intersection of the two sets. The result is converted back to a list before being returned.

#7. write a program that takes two lists of integers as input and returns a new list that contains the squares of all the integers in the original list 

def square_numbers(number):
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers

# Example usage:
numbers =[1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(squared_numbers) 
# This function uses a list comprehension to iterate through the input list and computes the square of each number, returning a new list with the squared values.

#8. write a function that takes two lists of integers as input and returns a sum of the two integers.
def sum_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both list must have the same length")
    summed_list =[a + b for a, b in zip(list1,list2)]
    return summed_list

# Example usage:
list1 = [1, 2, 3]                
list2 = [4, 5, 6]
summed_list = sum_lists(list1, list2)
print(summed_list)
# This function first checks, if both lists have the same lenght. if they don't, it raises a 'ValueError'. Then it uses a list comprehension along with the 'Zip' function to iterate over pairs of elements from both lists, summing each pair and returning the result as a new list.

#9. write a program that takes two lists of integers as input and returns the products of all the integers in the list

def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def products_of_lists(list1, list2):
    product1 = product_of_list(list1)
    product2 = product_of_list(list2)
    return product1, product2

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

product1, product2 = products_of_lists(list1, list2)
print(f"Product of list1: {product1}")
print(f"Product of list2 : {product2}")

'''
In the program:
* The 'product_of_list' fuction calculates the product of all integers
* The 'products_of_lists' function calculates the products of all integers in both input lists by calling 'products_of_list' for each list.
* The programs then prints the products of the two lists.
'''
#10. write a program that takes two lists of strings as input and returns a new list that contains only the strings that start with the letter 'a'.

def filter_strings_starting_with_a(list1, list2):
    combined_list = list1 + list2
    filter_list = [s for s in combined_list if s.startswith('a')]
    return filter_list

# Example usage:
list1 = ["apple", "banana", "angel", "cherry"]
list2 = ["avovado", "blueberry", "arrow", "date"]

filter_list = filter_strings_starting_with_a(list1, list2)
print(filter_list)

'''
in the program:

1. 'filter_strings_starting_with_a' function takes two lists of string as input.
2. The function combines the two lists into one.
3. It then uses a list comprehension to filter out the strings that start with the letter 'a' using the 'startswith' method.
4. The filter list is returned and printed.
'''