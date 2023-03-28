from tkinter import *
root = Tk() #create the root window
root.geometry('180x200')
listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE) #create a listbox

listbox.insert(1, "Data Structure") #inserting the listbox items
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(3, "Machine Learning")
listbox.insert(3, "Blockchain") 

def selected_item(): #prints the selected listbox value(s)
    for i in listbox.curselection():
        print(listbox.get(i)) #traverse the tuple returned by curselection method + print corresponding value(s) in the listbox
btn = Button(root, text='Print Selected', command=selected_item) #button widget + map the command parameter to selected_item function
btn.pack(side='bottom')
listbox.pack()
root.mainloop()