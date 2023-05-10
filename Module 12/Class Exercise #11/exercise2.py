import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = 'Exercise 2')
        self.main_window.geometry("300x300")
        self.label2 = tkinter.Label(self.main_window,
                                    text='Last Name',
                                    borderwidth = 1,
                                    relief ='solid')
        self.label3 = tkinter.Label(self.main_window,
                                    text ='First Name',
                                    borderwidth=1,
                                    relief='solid')
        self.label4 = tkinter.Label(self.main_window,
                                    text = 'Age',
                                    borderwidth= 1,
                                    relief ='solid')
        self.label.pack()
        self.label2.pack(ipadx=20,ipady=20,padx=20,pady=20)
        self.label3.pack(ipadx=20, ipady=20, padx=20, pady=20)
        self.label4.pack(ipadx=20, ipady=20,padx=20,pady=20)
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()