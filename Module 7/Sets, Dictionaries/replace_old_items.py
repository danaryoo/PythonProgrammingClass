def main():
    food = ['Pizza','Burgers','Chips']
    print('here are the food items in the list')
    print(food)
    item = input('which items in the list do you want to change?')
    try: #will try the batch of code below
        itemIndex = food.index(item) #gets the items index in the list
        newItem = input('enter the new value ')
        food[itemIndex] = newItem #replace the old item with the new item
        print(' here is the revisted list ')
        print(food)
    except ValueError: #if an error is found it will print the error
        print('the item was not found in the list')

if __name__ == '__main__':
    main()