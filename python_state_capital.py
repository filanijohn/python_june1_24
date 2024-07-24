state_capital = [
        {
            'state' : 'Oyo',
            'capital': 'Ibadan'
        },
        {
            'state' : 'Lagos',
            'capital': 'Ikeja'
        },
        {
            'state' : 'Ogun',
            'capital': 'Abeokuta'
        },
        {
            'state' : 'Edo',
            'capital': 'Benn'
        },
        {
            'state' : 'Akwa-ibm',
            'capital': 'Uyo'
        },
    ]   


def main(main_list):

    def display(st_list): #parameter / requirement

        for each_item in st_list:
            #print(each_item)
            pos = st_list.index(each_item)
            print(f'{pos+1}. {each_item["state"]} - {each_item["capital"]}')

    def add():
        new_state = input('Enter the name of the new State: ')
        mew_capital = input('Enter the name of the new capital: ')
        st_cp ={
            'state' : new_state,
            'capital' : mew_capital
        }
        main_list.append(st_cp)

        display(main_list)

    def edit():
        pos = input('Enter the number of the state: ')
        print('')
        st_cp = main_list[int(pos)-1]
        try:
            print(f'{pos}. {st_cp["state"]} - {st_cp["capital"]}')
            ask_State = input('Enter Y to edit the new State: ')
            new_State = False
            new_capital = False
            if ask_State.casefold() == 'y':
                new_State = input('Enter the name of the new State: ')
                main_list[int(pos)-1]['state'] = new_State

            if new_State or new_capital:
                print('Edit successful !!!')
            else:
                print('No changes were made')
        except:
            print('Invalid number')

    def delete():
        pos = input('Enter the number of the state to be delete: ')
        print('')
        try:
            main_list.pop(int(pos)-1)
            print('Delete successful')
        except:
            print('Invalid number')


    announement =   '''
                    Choose option 1 - 4
                    1. To displays all states and capital
                    2. To add new state and capital 
                    3. To edit a state and its capital
                    4. To delete a state and its capital
                    5. To close program\n
                    '''
    print(announement)
    option = input('Enter your option: ')
    if  option == '1':
        print('Displays all states and capital')
        display(main_list)
        main(main_list)
    elif option == '2':
        print('Add a state and its capital')
        add()
        main(main_list)
    elif option == '3':
        print('Edit a particular state and its capital')
        edit()
        main(main_list)
    elif option == '4':
        print('Delete a particular state and its capital')
        delete()
        main(main_list)

main(state_capital)
    