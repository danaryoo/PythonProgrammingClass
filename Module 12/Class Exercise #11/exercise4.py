#This program demonstrates a Button widget, when the user clicks the button, a dialog box is displayed w/ positive quote
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x150")
        self.my_button = tkinter.Button(self.main_window,
                                        text = 'Click for a positive quote!',
                                        command =self.do_something) #create a button widget
        self.my_button.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response',
                                    'We need, in every community, a group of angelic troublemakers. - Bayard Rustin') 

if __name__ == '__main__':
    my_gui = MyGUI()