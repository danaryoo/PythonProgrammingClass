#Insect class = main/super class
#sub-classes = bumblebee + grasshopper ; use mutator + accessor methods for each class
#bumblebee stings grasshopper jumps

class Insect:
    def __init__(self, name, body_part,legs):
        self.__name = name
        self.__body_part = body_part
        self.__legs = legs

    def set_name(self,name):
        self.__name = name
    def set_body_part(self,body_part):
        self.__body_part = body_part
    def sef_legs(self,legs):
        self.__legs = legs
    
    def get_name(self):
        return self.__name
    def get_body_part(self):
        return self.__body_part
    def get_legs(self):
        return self.__legs

class Bumblebee(Insect):
    def __init__(self,name,body_part,legs,sting):
        super().__init__(name,body_part, legs)
        self._sting = sting
    def set_sting(self,sting):
        self._sting = sting
    def get_sting(self):
        return self._sting
        
    def print_Bumblebee(self):
        print('Name: ' + self.get_name())
        print('Number of Body Parts? : '+ str(self.get_body_part()))
        print('Number of Legs?: '+ str(self.get_legs()))
        print('Does it sting?: '+ str(self.get_sting()))

class Grasshopper(Insect):
    def __init__(self,name,body_part,legs,jump):
        super().__init__(name,body_part,legs)
        self._jump = jump
    def set_jump(self,jump):
        self._jump = jump
    def get_jump(self):
        return self._jump
    
    def print_Grasshopper(self):
        print('Name: ' + self.get_name())
        print('Number of Body Parts? : '+ str(self.get_body_part()))
        print('Number of Legs?: '+ str(self.get_legs()))
        print('Does it jump?: '+ str(self.get_jump()))

def main():
    bumblebee = Bumblebee('Bebe',3,6,'yes')
    grasshopper = Grasshopper('Derek',3,6,'yes')
    bumblebee.print_Bumblebee()
    grasshopper.print_Grasshopper()

main()