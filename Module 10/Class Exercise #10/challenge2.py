#uses super keyword to inherit attributes + arguments
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#student class is inheriting from the person class
class Student(person):
    def __init__(self,name,age,studentID, GPA,address,city,state,zipcode):
        name = input('enter the studnet name: ')
        age = input('enter the astudnetge: ')
        studentID = input('enter the Student ID: ')
        GPA = input('enter the GPA: ')
        address = input('enter the address: ')
        city = input('enter the city: ')
        state = input('enter the state: ')
        zipcode = input('enter the zip code: ')
        super().__init__(name,age) 
        #super keyword is calling the super class which is the person class passing name + sage
        self.name = name
        self.age = age
        self.studentID = studentID
        self.GPA = GPA
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Teacher(person):
    def __init__(self,name,age,TeacherID,ClassTeaching,address,city,state,zipcode):
        super().__init__(name,age)
        name = input('enter the teacher name: ')
        age = input('enter the teacher age: ')
        TeacherID = input('enter the Teacher ID: ')
        ClassTeaching = input('enter the name of the course teaching: ')
        address = input('enter the address: ')
        city = input('enter the city: ')
        state = input('enter the state: ')
        zipcode = input('enter the zip code: ')
        self.name = name
        self.age = age
        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

student = Student('Jane Doe',25,777,3.8,'1234 Any St','Los Angeles','CA',90034)
print(f'Student Name: {student.name}')
print(f'Student Age: {student.age}')
print(f'Student ID: {student.studentID}')
print(f'Student GPA: {student.GPA}')
print(f'Student Address: {student.address}')
print(f'Student city: {student.city}')
print(f'Student State: {student.state}')
print(f'Student Zip Code: {student.zipcode}')
print('\n')
teacher = Teacher('Ms. Cantor',45,7,'Python','5678 Street St','Los Angeles','CA',91214)
print(f'Teacher Name: {teacher.name}')
print(f'Teacher Age: {teacher.age}')
print(f'Teacher ID: {teacher.TeacherID}')
print(f'Teacher Course: {teacher.ClassTeaching}')
print(f'Teacher Address: {teacher.address}')
print(f'Teacher city: {student.city}')
print(f'Teacher State: {student.state}')
print(f'Teacher Zip Code: {student.zipcode}')