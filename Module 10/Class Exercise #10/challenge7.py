#Employee + ProductionWorker classe
class Employee:
    def __init__(self,name,number):
        self.__name = name
        self.__number = number
    def set_name(self,name):
        self.__name = name
    def set_number(self,number):
        self.__number = number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    
    def GetInformation(self):
        print('Name: ' + self.__name)
        print('Number: ' + str(self.__number))
        print('Shift: ' + str(self._shift))
        print('Pay Rate: ' + str(self._pay_rate))

class ProductionWorker(Employee):
    def __init__(self,name,number,shift, pay_rate):
        super().__init__(name,number)       
        self._shift = shift
        self._pay_rate = pay_rate
    def set_shift(self,shift):
        self._shift = shift
    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate
    def get_shift(self):
        return self._shift
    def get_pay_rate(self):
        return self._pay_rate
    
name = input('Enter the name: ')
number = input('Enter the number: ')
shift = input('Enter the shift number: ')
pay_rate = input('Enter the hourly pay rate: ')

worker = ProductionWorker(name,number, shift,pay_rate)
worker.GetInformation()