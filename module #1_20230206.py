#Dana Ryoo
print ('Dana Ryoo')

#Challenge Exercise #1
firstname = input ('Enter the first name ')
lastname = input ('Enter the last name ')
print ('hello ' + firstname + "," + lastname)

#Challenge Exercise #2
name = input ('Type your name ') 
age = int (input ('Type your age '))
income = float (input ('type your income '))
salary = input ('Type your salary ')
bonus = input ('Type your bonus ') 
pay = salary + bonus

print ('Hello ' + name +
       "your age is " + str (age) + 
       "your income is $ " + str (income))
print ('your pay is $', pay)

#Challenge Exercise #3
p1_first = input ('What is your first name?' + "\n")
p1_last = input ('What is your last name?' + "\n")
address = input ('What is your address?'+ "\n")
city= input ('In what city do you live?'+ "\n")
state = input ('In what state?'+ "\n")
zipcode = input ('In what zip code?'+ "\n")
print ('Hello, we want to ask you some quick questions' + 
        first_name + ',' + last_name +
        city + ',' + state + ',' + zipcode)

#Challenge Exercise #4
p1_hours = int(input('Enter # of hours worked'))
p1_pay = int(input('Enter your hourly pay'))
p1_total = p1_hours * p1_pay
p2_first = input ('What is your first name?' + "\n")
p2_last = input ('What is your last name?' + "\n")
p2_hours = int(input('Enter # of hours worked '))
p2_pay = int(input('Enter your hourly pay '))
p2_total = p2_hours *p2_pay
average = (p1_total + p2_total)/2
print ('The average pay between two people are ' + str(average))