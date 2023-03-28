#Project #2
#This program uses a dictionary to keep friends' names an  birthdays
#global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    birthdays = {} #create an empty dictionary
    choice = 0 #initialize a variable for the user's choice
    if choice == LOOK_UP:
        look_up(birthdays)
    elif choice == ADD:
        add(birthdays)
    elif choice == CHANGE:
        change(birthdays)
    elif choice == DELETE:
        delete(birthdays)

def get_menu_choice(): #diplays the menu + gets a validated choice from the user
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a new birthday')
    print('4. Delete a new birthday')
    print('5. Quit the program')
    print()
    choice = int(input('Enter your choice: ')) #gets the user's choice
    while choice < LOOK_UP or choice > QUIT: #validates the choice
        choice = int(input('Enter a valid choice: '))
    return choice #return the user's choice 

def delete(birthdays): #deletes an entry from the birthdays dictionary
    name = input('Enter a name ') #get a name to look up
    if name in birthdays: #if the name is found, delete the entry
        del birthdays[name]
    else:
        print('That name is not found.')

if __name__=='__main__':
    main()