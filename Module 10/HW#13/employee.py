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
    
class ShiftSupervisor(Employee):
    def __init__(self,name,number,annual_salary,production_bonus):
          super().__init__(name,number)
          self._annual_salary = annual_salary
          self._production_bonus = production_bonus
    def set_annual_salary(self, annual_salary):
        self._annual_salary = annual_salary
    def set_production_bonus(self,production_bonus):
        self._production_bonus = production_bonus
    def get_annual_salary(self):
        return self._annual_salary
    def get_production_bonus(self):
        return self._production_bonus
    
    def printInformation(self):
         print('Name: '+self.get_name())
         print('Number: '+str(self.get_number()))
         print('Annual salary: '+str(self.get_annual_salary()))
         print('Production bonus goal met? : '+self.get_production_bonus())
