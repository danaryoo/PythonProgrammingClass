#This program displays an empty window
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() #create the main window widget
        self.main_window.title('My First GUI') #display a title
        self. label = tkinter.Label (self.main_window, text = 'my text')
        tkinter.mainloop() #enter the tkinter main loop
        self.label.pack()

if __name__ == '__main__':
    my_gui = MyGUI()