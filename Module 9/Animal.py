from wsgiref import validate

class Animal:
    def __init__(self,l , a, n):
        self.leg = l
        self.name = n
        self.age = a
    def __str__ (self):
        return self.__name + ' ' + self.age + ' ' + str(self.age)

    def SetLeg(self, l):
        self.leg = l 
    def GetLeg(self):
        return self.leg 
    
    def SetAge(self, a):
        self.age = a 
    def GetAge(self):
        return self.age 
    
    def SetName(self, n):
        self.name = n 
    def GetName(self):
        return self.name 
