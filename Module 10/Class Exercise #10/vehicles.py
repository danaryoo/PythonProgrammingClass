class Automobiles:
    def __init__(self,make,model,mileage,price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    #these are the mutator methods
    def set_make(self,make):
        self.__make = make 
    def set_model(self,model):
        self.__model = model
    def set_mileage(self,mileage):
        self.__mileage = mileage
    def set_price(self,price):
        self.__price = price

    #these are accessor methods
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price

class Car_demo(Automobiles):
    def __init__(self,make,model,mileage,price,door,electronic):
        super().__init__(make,model,mileage,price)
        self._door = door
        self._electronic = electronic
    
    def print_description(self):
        print('Make: ' + self.get_make())
        print('Model: '+ str(self.get_model()))
        print('Mileage: '+ str(self.get_mileage()))
        print('Price: '+ str(self.get_price()))
        print('Number of Doors:'+ str(self.get_door()))
        print('Electronic vehicle?: '+ self.get_electronic())
    
    def set_door(self,door):
        self._door = door
    def set_electronic(self,electronic):
        self._electronic = electronic
    def get_door(self):
        return self._door
    def get_electronic(self):
        return self._electronic
    