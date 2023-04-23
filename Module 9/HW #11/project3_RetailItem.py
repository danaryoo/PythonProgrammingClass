class RetailItem:
    def __init__(self, number,description,units,price):
        self.__number = number
        self.__description = description
        self.__units = units
        self.__price = price

    def set_number(self,number):
        self.__number = number
    def set_description(self,description):
        self.__description = description
    def set_units(self,units):
        self.__units = units
    def set_price(self,price):
        self.__price = price