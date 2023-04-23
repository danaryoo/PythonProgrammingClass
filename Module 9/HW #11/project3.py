import project3_RetailItem

def main():
    number = (input('enter the Item #: '))
    description = (input('enter the Description: '))
    units = (input('enter the Units in inventory: '))
    price = (input('enter the Price: '))

    v1 = project3_RetailItem.RetailItem.set_number = number
    v2 = project3_RetailItem.RetailItem.set_description = description
    v3 = project3_RetailItem.RetailItem.set_units = units
    v4 = project3_RetailItem.RetailItem.set_price = price

    print(f'Item #:{v1}      Description:{v2}      Units in Inventory:{v3}      Price:{v4}')

main()