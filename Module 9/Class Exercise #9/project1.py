class Students:
    def GetInformation(self):
        print('student Lastname name is ' + self.Lastname)
        print('student Firstname name is ' + self.Firstname)
        print('student Address name is ' + self.Address)
        print('student City name is ' + self.City)
        print('student State name is ' + self.State)
        print('student Zipcode name is ' + self.Zipcode)

#creates the Student1 object
Student1 = Students()
Student1.Lastname = 'Doe'
Student1.Firstname = 'Jane'
Student1.Address = '111 St'
Student1.City = 'Santa Ana'
Student1.State = 'CA'
Student1.Zipcode = '12345\n'

#creates the Student2 object
Student2 = Students()
Student2.Lastname = 'Cantor'
Student2.Firstname = 'Mike'
Student2.Address = '222 St'
Student2.City = 'Garden Grove'
Student2.State = 'CA'
Student2.Zipcode = '67890'

#user inputs the Student3 object
Student3 = Students()
Student3.Lastname = input('Please enter your last name: ')
Student3.Firstname = input('Please enter your first name: ')
Student3.Address = input('Please enter your address: ')
Student3.City = input('Please enter your city: ')
Student3.State = input('Please enter your state: ')
Student3.Zipcode = input('Please enter your zip code: ')


#Calling the function
Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()
