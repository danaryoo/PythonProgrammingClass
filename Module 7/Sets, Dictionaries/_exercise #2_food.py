#Challenge Exercise #2 print the food items
#create GUI with some listboxes items
from tkinter import *
top = Tk() #create a Tk root window named top

listbox = Listbox(top, #create listbox object
                  height =10, width = 15, bg = 'grey', 
                  activestyle = 'dotbox',
                  font = 'Helvita',
                  fg='yellow',
                  selectmode=MULTIPLE)

top.geometry('300x250') #size of the window
label = Label(top, text = 'FOOD ITEMS') #label for the list

listbox.insert(1,'Sandwich') #insert elements by index w/ their names as parameters
listbox.insert(2,'Burger')
listbox.insert(3,'Pizza')
listbox.insert(4,'French Fries')
listbox.insert(5,'Hot Dogs')
listbox.insert(6,'CheeseBurger')

def selected_item(): #print the selected value form in the listbox
    for i in listbox.curselection():
        print(listbox.get(i)) #traverse the tuple return by curselection method + print the corresponding value(s)

btn = Button(top, text='Print selection', command=selected_item) #create a button widget and map the command parameter to selected_item function
btn.pack(side='bottom') #placing the bottom on the listbox

label.pack() #pack the widgets
listbox.pack()

top.mainloop() #Display until user exists themselves