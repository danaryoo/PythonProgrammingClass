class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address = address
    def set_phone(self,phone):
        self.__phone = phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self,name,address,phone,customer_number,mailing):
        super().__init__(name,address,phone)
        self._customer_number = customer_number
        self._mailing = mailing
    def set_customer_number(self,customer_number):
        self._customer_number = customer_number
    def set_mailing(self,mailing):
        self._mailing = mailing
    def get_customer_number(self):
        return self._customer_number
    def get_mailing(self):
        return self._mailing
    
    def PrintInformation(self):
        print('Name: '+ self.get_name())
        print('Address: '+ self.get_address())
        print('Phone Number: '+ str(self.get_phone()))
        print('Customer Number: '+str(self.get_customer_number()))
        print('Joining the mailing list? (0 = no, 1 = yes): '+ str(self.get_mailing()))
