import project4_class7

def main():
    name = (input('enter the name '))
    address = (input('enter the address '))
    phone = (input('enter the phone '))
    city = (input('enter the city '))
    zipcode = (input('enter the zip code '))
    age = (input('enter the age '))

    v1 = project4_class7.Customer.set_name = name
    v2 = project4_class7.Customer.set_address = address
    v3 = project4_class7.Customer.set_phone = phone
    v4 = project4_class7.Customer.set_city = city
    v5 = project4_class7.Customer.set_zipcode = zipcode
    v6 = project4_class7.Customer.set_age = age

    print(f'Hello {v1}! Your age is {v6} and your # is {v3}.\nYour address is {v2},{v4} and the zip code is {v5}.')

main()