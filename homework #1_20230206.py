#Project #1
name = input ('Type your name ') 
address = input ('What is your address?'+ "\n")
city= input ('In what city do you live?'+ "\n")
state = input ('In what state?'+ "\n")
zipcode = input ('In what zip code?'+ "\n")
phone = input ('What is your phone number?'+ "\n")
major = input ('What is your major?'+ "\n")
print ('My name is' + name + "\n" +
        'I live in' + address + state + zipcode + "\n" +
        'And my number is' + phone + "\n" +
        'My major is/was' + major)

#Project #2
price = input ("What is the item's price? ")
sales_tax = int(price) * 1.07
print ('The final amount is ' + str(sales_tax))

#Project #3
food = input ('How much did the food cost? ')
subtotal = (int(food) *0.07) + (int(food)* 0.18) + int(food)
print ('The final amount is '+ str(subtotal))

#Project #4
sugar = 1.5 / 48
butter = 1 / 48
flour = 2.75 / 48
cookies = int (input ('How many cookies do you want to make? '))
print("To make" + str(cookies) + "number of cookies," + "\n" + 
        "You need " + str(sugar * cookies) + "cups of sugar" + "\n" +
        str(butter * cookies) + " cups of butter" + "\n" +
        str(flour * cookies) + " cups of flour.")