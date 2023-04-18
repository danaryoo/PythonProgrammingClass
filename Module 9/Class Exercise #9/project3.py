class PI: 
    def GetInformation(self,LN,FN,Age,Addy,City,State,ZipCode):
        return LN + ' , ',FN+' , '+str(Age) + Addy+ ' , '+City+' , '+State+' , '+str(ZipCode)

PersonalInformation = PI()
PersonalInformation.LN = input('Enter the last name: ')
PersonalInformation.FN = input('Enter the first name: ')
PersonalInformation.Age = input('Enter the age: ')
PersonalInformation.Addy = input('Enter the address: ')
PersonalInformation.City = input('Enter the city: ')
PersonalInformation.State = input('Enter the state: ')
PersonalInformation.ZipCode = input('Enter the zipcode: ')

print(PersonalInformation.GetInformation(PersonalInformation.LN,PersonalInformation.FN,PersonalInformation.Age,PersonalInformation.Addy
                                         , PersonalInformation.City,PersonalInformation.State,PersonalInformation.ZipCode))