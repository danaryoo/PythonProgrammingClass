class Employee:
    def __init__(self, name,id,department,title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    def set_name(self,name):
        self.__name = name
    def set_id(self,id):
        self.__id = id
    def set_department(self,department):
        self.__department = department
    def set_title(self,title):
        self.__title = title