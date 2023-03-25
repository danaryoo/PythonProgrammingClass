# %%
#Exercise #1
def WriteInput(): 
    print("Please enter your first, last name and age")
    anotherInput ='Y'
    
    while anotherInput =='Y' or anotherInput =='y': 
        firstName = input('First name: ')
        lastName = input('Last name: ')
        age = input('Age: ')

        challenge1 = open('challenge1.txt','a') #the a letter means to append

        challenge1.write (firstName + '\n')
        challenge1.write (lastName + '\n')
        challenge1.write (age + '\n')

        challenge1.close()

        print('Demographic information recorded')

        anotherInput = input('do you want to write another? type Y or y')

def read():
    infile = open('challenge1.txt','r')
    fileContents = infile.read()
    infile.close()
    print(fileContents)

WriteInput()
read()

# %%
#Challenge #2
def WriteNumbers():
    outfile = open('numbers.txt','a')

    num1 = int(input('Enter #1 '))
    num2 = int(input('Enter #2 '))
    num3 = int(input('Enter #3 '))
    sum = num1 + num2 + num3
    avg = sum/3

    outfile.write('The 1st number is '+ str(num1) + '\n')
    outfile.write('The 2nd number is '+ str(num2) + '\n')
    outfile.write('The 3rd number is '+ str(num3) + '\n')
    outfile.write('The average number is '+ str(avg) + '\n')
    outfile.write('The total number is '+ str(sum) + '\n')

    print('data recorded')

def readWriteNumbers():
    ReadWriteNumbers = open('numbers.txt','r')
    ReadWriteNum = ReadWriteNumbers.read()
    ReadWriteNumbers.close()
    print(ReadWriteNum)

WriteNumbers()
readWriteNumbers()

# %%
#Exercise #3
def sales():
    num_days = int(input('Enter the days of sales: '))
    salary = int(input('Enter your salary: '))
    sales_file = open('sales.txt','a')
    total_sales = 0

    for count in range(1, num_days+1):
        sales = float(input('enter the sales for day # ' + str(count) + " : $"))
        total_sales += sales
        sales_file.write(str(sales) + '\n')
    print('sales recorded')

    if total_sales > 1000:
        salary = salary * 1.1
    salary_output = f'Total salary (with commission if applicable) is ${salary}'
    sales_file.write(salary_output)
    sales_file.close()
sales()

def ReadSales():
    sales_file = open('sales.txt','r')
    line = sales_file.readline()

    while line !='': #as long an empty string is NOT returned
        try:
            amount = float(line)
            print(format(amount, '.2f'))
        except:
            print(line)
        line = sales_file.readline()
    sales_file.close()
ReadSales()

# %%
#Exercise #4
def employee():
    num_emps = int(input('Enter the number of employee records'))
    emp_file = open('employees.txt','w')

    for count in range(1,num_emps+1):
        print('Enter data for employee #', count)
        name = input('Name: ')
        id_num = input('ID NUMBER: ')
        dept = input('DEPARTMENT: ')

        emp_file.write(name+'\n')
        emp_file.write(id_num+'\n')
        emp_file.write(dept+'\n')

        print()

    emp_file.close()
    print('recorded')
employee()

def readEmployee():
    ReadEmp = open('employees.txt','r')
    ReadEmployee = ReadEmp.read()
    ReadEmp.close()
    print(ReadEmployee)
readEmployee()

# %%
#Exercise #5
import tkinter as tk
from tkinter import messagebox

win = tk.Tk() #create the window interface
win.geometry("300x200") #width x height in pixels
win.title("Customer Information") #Label for the title

lblLastname = tk.Label(win, text = "Enter the Last Name").grid(column = 0, row = 0) #Label widget
lblFirstname = tk.Label(win, text = "Enter the First Name").grid(column = 0, row = 1)
lblAddress = tk.Label(win, text = "Enter the Address").grid(column = 0, row = 2)
lblCity = tk.Label(win, text = "Enter the City").grid(column = 0, row = 3)
lblState = tk.Label(win, text = "Enter the State").grid(column = 0, row = 4)
lblZip = tk.Label(win, text = "Enter the Zip code").grid(column = 0, row = 5)

def write():
    text_file = open("Customers.txt",'a')
    content = text_file.write('\nConfirmation:' + str(LN.get()) + ", " + str(FN.get()) + "\n" + str(Addy.get()) + str(City.get()) + str(State.get()) + str(ZipCode.get()))
    text_file.close()
    messagebox.showinfo("Information","Data Recorded")

def quite():
    messagebox.showinfo("Information","Thank you...")
    win.destroy() #closes the interface

def submit(): #function name
    messagebox.showinfo("Information","entered : " + LN.get() + "," + FN.get()) #display info

LN = tk.StringVar() #the StringVar manages the Entry widget
txtLastname = tk.Entry(win, width = 12, textvariable= LN).grid(column = 1, row = 0)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width = 12, textvariable= FN).grid(column = 1, row = 1)
Addy = tk.StringVar()
txtAddy = tk.Entry(win, width = 20, textvariable=Addy).grid(column = 1, row = 2)
City = tk.StringVar()
txtCity = tk.Entry(win, width = 20, textvariable=City).grid(column = 1, row = 3)
State = tk.StringVar()
txtState = tk.Entry(win, width = 20, textvariable=State).grid(column = 1, row = 4)
ZipCode = tk.StringVar()
txtZip = tk.Entry(win, width = 20, textvariable=ZipCode).grid(column = 1, row = 5)

btnSubmit = tk.Button(win, text = "Submit", command = submit).grid(column = 0, row = 8) #Button widget
btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 1, row = 8)
btnWrite = tk.Button(win, text = "Transfer", command = write).grid(column = 2, row = 8)

win.mainloop() #ensures the interfaces stays on the screen or window

# %%
#Exercise #6
import tkinter as tk
from tkinter import messagebox

win = tk.Tk() 
win.geometry("300x100") 
win.title("Numbers")

lblFirstNum = tk.Label(win, text = "Enter the 1st number: ").grid(column = 0, row = 0) 
lblSecondNum = tk.Label(win, text = "Enter the 2nd number: ").grid(column = 0, row = 1)
lblThirdNum = tk.Label(win, text = "Enter the 3rd number: ").grid(column = 0, row = 2)

def writeNum():
    num_file = open("GUINumbers.txt","a")
    total = int(FirstNum.get()) + int(SecondNum.get()) + int(ThirdNum.get())
    avg = total/3
    num_file.write(f'The three numbers are: {FirstNum.get()}, {SecondNum.get()}, {ThirdNum.get()}. The total is {total}. The average is {avg}\n')
    num_file.close()
    messagebox.showinfo("Information","Numbers Recorded")

def Resubmit(): 
    messagebox.showinfo("Information","You've entered : " + FirstNum.get() + "," + SecondNum.get() + "," + ThirdNum.get())

FirstNum = tk.StringVar()
txtFirstNum = tk.Entry(win, width=10, textvariable = FirstNum).grid(column = 1, row = 0) 
SecondNum = tk.StringVar()
txtSecondNum = tk.Entry(win, width=10, textvariable = SecondNum).grid(column = 1, row = 1) 
ThirdNum = tk.StringVar()
txtThirdNum = tk.Entry(win, width=10, textvariable = ThirdNum).grid(column = 1, row = 2)

buttonSubmit = tk.Button(win, text = "Submit", command = Resubmit).grid(column = 0, row = 5)
buttonWrite = tk.Button(win, text = "Transfer", command = writeNum).grid(column = 3, row = 5)

win.mainloop()

# %%
#Exercise #7
#user inputs full name, midterm grade, final exam grade
#program calculates the average grade of midterm and final exam & returns a letter grade associated with the average grade
#the outcome is recorded into the file and read from the file

def GradeInput(): 
    print("Please enter your Full name and test scores")
    
    Name = input('Full name: ')
    grade = 'na'
    try:
        Midterm = int(input('Midterm score: '))
        Final = int(input('Final exam score: '))
        average = (Midterm + Final) / 2
        if average < 0 or average > 100:
            print('Please re-enter valid test scores')
            return
        elif average < 60:
            grade = 'F'
        elif average <= 69:
            grade = 'D'
        elif average <= 79:
            grade = 'C'
        elif average <= 89:
            grade = 'B'
        elif average <=100:
            grade = 'A'
        Grades = open('Grades.txt','a') 
        Grades.write (Name + '\n')
        Grades.write (grade + '\n')
        Grades.close()
    except ValueError:
        print('Invalid value entered') 

GradeInput()

def read():
    infile = open('Grades.txt','r')
    fileContents = infile.read()
    infile.close()
    print(fileContents)
read()

# %%
#Exercise #8
import random

RandNumber = random.randint(1,10)
def WriteRandNumber(): 
    print("The program will generate a random number between 1 - 10")
    RandNum = open('Random Number.txt','a') 
    RandNum.write (f'The program selected {RandNumber}.')
    RandNum.close()

    print('A random number has been recorded')

def read():
    infile = open('Random Number.txt','r')
    fileContents = infile.read()
    infile.close()
    print(fileContents)

WriteRandNumber()
read()


