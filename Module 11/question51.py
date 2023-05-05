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
    
Worker1 = ProductionWorker("John Doe", 12345, 1, 10.0)
Worker2 = ProductionWorker("Dorothy Smith", 67890, 2, 13.0)
Worker3 = ProductionWorker("Cynthia Kim", 24680, 1, 12.0)

Worker1.GetInformation()
Worker2.GetInformation()
Worker3.GetInformation()