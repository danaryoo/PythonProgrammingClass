#This program demonstrates internal padding
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300")
        self.label1 = tkinter.Label(self.main_window,
                                    text = 'Hellow World!',
                                    borderwidth=1,
                                    relief = 'solid')
    
        self.label2 = tkinter.Label(self.main_window,
                                    text = 'This is my GUI program.',
                                    borderwidth=1,
                                    relief ='solid')

        self.affirmation1 = tkinter.Label(self.main_window,
                                          text ='It is Choice not Chance, that Determines Your Destiny',
                                          borderwidth =1,
                                          relief = 'ridge')
        
        self.affirmation2 = tkinter.Label(self.main_window,
                                          text = 'This too shall also come to pass',
                                          borderwidth=1,
                                          relief ='sunken')
        
        self.label1.pack(ipadx=20,ipady=20)
        self.label2.pack(ipadx=20,ipady=20)
        self.affirmation1.pack(ipadx=20,ipady=20)
        self.affirmation2.pack(ipadx=20,ipady=20)

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()