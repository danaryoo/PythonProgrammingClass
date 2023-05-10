import tkinter

class MyGUI:
    def __init__ (self):
        self.main_window = tkinter.Tk()
        self.main_window.title('My First GUI')
        self.main_window.geometry("300x300")
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
