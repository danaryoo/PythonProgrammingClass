#Project #1-1
#user inputs animal, fruit, country
#program outputs a file things.txt

def UserInput():
  print('Please enter an animal, a fruit, and a country')
  animal = input('Enter an animal: ')
  fruit = input('Enter a fruit: ')
  country = input('Enter a country: ')

  things = open('things.txt','a')
  things.write (animal + '\n')
  things.write (fruit + '\n')
  things.write (country + '\n')
  things.close()

  print('Inputs recorded')

#Project #1-2
def ReadUserInput():
  openUserInput = open('things.txt','r')
  fileContents = openUserInput.read()
  openUserInput.close()
  print(fileContents)

UserInput()
ReadUserInput()

#Project #1-3
#program opens an output file 'number_list.txt' which uses a loop to write 1-100

def createfile():
  num = 0
  print('This program will write numbers from 1 to 100')
  number_list = open('number_list.txt','a')
  for count in range(1,100+1):
    num+=1
    number_list.write(str(num) + '\n')
  print('numbers recorded')
  number_list.close()

createfile()

#Project #2
#program creates a 'numbers.txt' file which reads the numbers in the file and calculate the total

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("300x300")
win.title('Enter a number')

lblNum = tk.Label(win, text = "Enter a number: ").grid(column = 0, row = 0) 

def writeNumber():
  num_file = open('numbers.txt','a')
  num_file.write(Num.get())
  num_file.close()
  messagebox.showinfo('Information','Number recorded. Enter another')

Num = tk.StringVar()
txtNum = tk.Entry(win, width=10, textvariable = Num).grid(column = 1, row = 0)

buttonStore = tk.Button(win, text = "Store", command = writeNumber).grid(column = 0, row = 5)

win.mainloop()

def readNumber():
  file = open('numbers.txt','r')
  line = file.readline()
  total = 0 
  while line !='':
    amount = int(line)
    total += amount
    line = file.readline()
  file.close()
  print(f'The sum of entered numbers is {total}')

readNumber()