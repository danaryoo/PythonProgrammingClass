#user enters favorite coffee brand, prod number, and price
#program writes to the coffee file + reads the file content
def write_coffee():
    print('Please enter your favorite coffee brand, production number, and price')
    brand = input('Favorite Brand: ')
    productNum = input('Production number: ')
    price = input('Price : $ ')

    append_coffee = open('coffee.txt','a')
    append_coffee.write ('\n'+ brand + ',')
    append_coffee.write (productNum + ',')
    append_coffee.write (price)
    append_coffee.close()
    print('Your information has been added')

def read_coffee():
    infile = open('coffee.txt','r')
    fileContents = infile.read()
    infile.close()
    print(fileContents)

write_coffee()
read_coffee()