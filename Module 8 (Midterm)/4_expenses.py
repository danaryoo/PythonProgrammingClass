#user enters rent, gas, food, clothing, car payment
#program takes the inputs and write them to the text file
#program reads the file's content
expense_file = open('expenses.txt','w')

def expenses():
    print('This program creates and reads monthly expenses based on your input')
    anotherInput = 'Y'
    while anotherInput =='Y' or anotherInput == 'y':
        user_rent = int(input('What was last month\'s rent?: ' ))
        user_gas = int(input('What was last month\'s gas?: ' ))
        user_food = int(input('What was last month\'s food?: ' ))
        user_clothing = int(input('What was last month\'s clothing?: ' ))
        user_car = int(input('What was last month\'s car payment?: ' ))
        sum = user_rent + user_gas + user_food + user_clothing + user_car

        expenses_file = open('expenses.txt','a')
        expenses_file.write('Last month rent: $'+ str(user_rent) + '\n')
        expenses_file.write('Last month gas: $'+ str(user_gas) + '\n')
        expenses_file.write('Last month food: $'+ str(user_food) + '\n')
        expenses_file.write('Last month clothing: $'+ str(user_clothing) + '\n')
        expenses_file.write('Last month car payment: $'+ str(user_car) + '\n')
        expenses_file.write('Last month total: $'+ str(sum) + '\n')
        print(f'Last month\'s information recorded')

        anotherInput = input('Do you want to enter another? Type Y or y')

def read_expenses():
    openExpenses = open('expenses.txt','r')
    readExpenses = openExpenses.read()
    openExpenses.close()
    print(readExpenses)

expenses()
read_expenses()

