 # create a list of at least 5 states and capital
#  write a program that collect user option 1 - 4
#  1. Displays all states and capital
#  2. Add new state and capital to the list
#  3.Edit a particular state and its capital
#  4. Delete a paticular state and its capital

# CRUD - Operation
# C - Create
# R - Read
# U - Update
# D - Delete/Destroy
                                #solution
def Displays_states_and_capitals(States_Capitals):
    print('\nLists of States and Capitals:') 
    for state, capital in States_Capitals.items():
        print(f"{state} - {capital}")

def Add_states_capital(States_Capitals):
    state = input("Enter the name of the state: ")
    Capital = input("Enter the capital of the state: ")
    States_Capitals[state] = Capital  
    print(f"{state} and its capital {Capital} added.\n")

def Edit_state_capital(states_capitals):
    state = input("Enter the name of the state you want to Edit: ")
    if state in states_capitals:
        capital = input("Enter the new capital of the state: ")
        states_capitals[state] = capital
        print(f"{state} has been updated with the new capital {capital}. \n")
    else :
        print(f"{state} not found in the list. \n")

def delete_state_capital(state_capitals):
    state =input("Enter the name of the state you want to delete:")
    if state in state_capitals:
        del state_capitals[state]
        print(f"{state} and its capital have been deleted. \n")
    else:
        print(f"{state} not found on the list. \n")

def main():
    States_capitals ={
        "Lagos": "ikeja",
        "Oyo": "Ibadan", 
        "Ogun": "Abeokuta", 
        "osun": "Osungbo", 
        "Ekiti": "Ado-Etiki" , 
        "Ondo": "Akure"
        }
    while True:
        print("Options")
        print("1. Display all states and capitals")
        print("2. Add a new states and capital")
        print("3. Edit a particular states and its capital")
        print("4. Delete a particular states and its capital")
        print("5. Exit")

        option = input("Enter your option (1 - 5): ")

        if option == "1":
            Displays_states_and_capitals(States_capitals)
        elif option == "2":
            Add_states_capital(States_capitals)
        elif option == "3":
            Edit_state_capital(States_capitals)
        elif option == "4":
            delete_state_capital(States_capitals)
        elif option == "5":
            break
        else: 
            print("Invalid option. Please try again. \n")
    
main()