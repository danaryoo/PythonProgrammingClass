class Pet:
    def __init__(self, name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self,name):
        self.__name = name
    def set_animal_type(self,animal_type):
        self.__anima_type = animal_type
    def set_age(self,age):
        self.__age = age

    def GetPet(self):
        print('Pet\'s name is '+ self.name)
        print('The type is ' + self.animal_type)
        print('The age is ' + self.age)
