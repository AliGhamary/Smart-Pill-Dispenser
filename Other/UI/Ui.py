
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font



class HomeScreen():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.ltext1 = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 12, weight = "normal"), cursor = "arrow", state = "normal")
        self.ltext1.place(x = 60, y = 20, width = 390, height = 52)
        self.ltext1.insert(INSERT, "Hello, please select a container to continue")
        self.button1 = Button(self.w1, text = "Container 1", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button1.place(x = 150, y = 100, width = 200, height = 52)
        self.button1['command'] = self.Name1
        self.button2 = Button(self.w1, text = "Container 2", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button2.place(x = 150, y = 180, width = 200, height = 52)
        self.button2['command'] = self.Name2
        self.button3 = Button(self.w1, text = "Container 3", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button3.place(x = 150, y = 260, width = 200, height = 52)
        self.button3['command'] = self.Name3
        self.button4 = Button(self.w1, text = "Container 4", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button4.place(x = 150, y = 340, width = 200, height = 52)
        self.button4['command'] = self.Name4

    def Name1(self):
        print('Name1')

    def Name2(self):
        print('Name2')

    def Name3(self):
        print('Name3')

    def Name4(self):
        print('Name4')

if __name__ == '__main__':
    a = HomeScreen(0)
    a.w1.mainloop()

class Container1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#00ffff')
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#00ffff')
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.ltext2 = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16), cursor = "arrow", state = "normal")
        self.ltext2.place(x = 130, y = 230, width = 250, height = 42)
        self.button1 = Button(self.w1, text = "Save", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button1.place(x = 40, y = 320, width = 120, height = 62)
        self.button1['command'] = self.Save
        self.button2 = Button(self.w1, text = "Reset", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button2.place(x = 330, y = 320, width = 130, height = 62)
        self.button2['command'] = self.Reset
        self.text1 = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "normal"), cursor = "arrow", state = "normal")
        self.text1.place(x = 80, y = 120, width = 350, height = 50)
        self.text1.insert(INSERT, "Please type the name of the pill")
        self.button3 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8, weight = "normal"), cursor = "arrow", state = "normal")
        self.button3.place(x = 190, y = 20, width = 120, height = 62)
        self.button3['command'] = self.Home

    def Save(self):
        print('Save')

    def Reset(self):
        print('Reset')

    def Home(self):
        print('Home')

if __name__ == '__main__':
    a = Container1(0)
    a.w1.mainloop()
class Container2():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#00ffff')
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#00ffff')
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.ltext2 = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16), cursor = "arrow", state = "normal")
        self.ltext2.place(x = 130, y = 230, width = 250, height = 42)
        self.button1 = Button(self.w1, text = "Save", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button1.place(x = 40, y = 320, width = 120, height = 62)
        self.button1['command'] = self.Save
        self.button2 = Button(self.w1, text = "Reset", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button2.place(x = 330, y = 320, width = 130, height = 62)
        self.button2['command'] = self.Reset
        self.text1 = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "normal"), cursor = "arrow", state = "normal")
        self.text1.place(x = 80, y = 120, width = 350, height = 50)
        self.text1.insert(INSERT, "Please type the name of the pill")
        self.button3 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8, weight = "normal"), cursor = "arrow", state = "normal")
        self.button3.place(x = 190, y = 20, width = 120, height = 62)
        self.button3['command'] = self.Home

    def Save(self):
        print('Save')

    def Reset(self):
        print('Reset')

    def Home(self):
        print('Home')

if __name__ == '__main__':
    a = Container2(0)
    a.w1.mainloop()
class Container3():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#00ffff')
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#00ffff')
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.ltext2 = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16), cursor = "arrow", state = "normal")
        self.ltext2.place(x = 130, y = 230, width = 250, height = 42)
        self.button1 = Button(self.w1, text = "Save", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button1.place(x = 40, y = 320, width = 120, height = 62)
        self.button1['command'] = self.Save
        self.button2 = Button(self.w1, text = "Reset", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button2.place(x = 330, y = 320, width = 130, height = 62)
        self.button2['command'] = self.Reset
        self.text1 = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "normal"), cursor = "arrow", state = "normal")
        self.text1.place(x = 80, y = 120, width = 350, height = 50)
        self.text1.insert(INSERT, "Please type the name of the pill")
        self.button3 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8, weight = "normal"), cursor = "arrow", state = "normal")
        self.button3.place(x = 190, y = 20, width = 120, height = 62)
        self.button3['command'] = self.Home

    def Save(self):
        print('Save')

    def Reset(self):
        print('Reset')

    def Home(self):
        print('Home')

if __name__ == '__main__':
    a = Container3(0)
    a.w1.mainloop()
class Container4():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#00ffff')
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#00ffff')
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.ltext2 = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16), cursor = "arrow", state = "normal")
        self.ltext2.place(x = 130, y = 230, width = 250, height = 42)
        self.button1 = Button(self.w1, text = "Save", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button1.place(x = 40, y = 320, width = 120, height = 62)
        self.button1['command'] = self.Save
        self.button2 = Button(self.w1, text = "Reset", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), cursor = "arrow", state = "normal")
        self.button2.place(x = 330, y = 320, width = 130, height = 62)
        self.button2['command'] = self.Reset
        self.text1 = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "normal"), cursor = "arrow", state = "normal")
        self.text1.place(x = 80, y = 120, width = 350, height = 50)
        self.text1.insert(INSERT, "Please type the name of the pill")
        self.button3 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8, weight = "normal"), cursor = "arrow", state = "normal")
        self.button3.place(x = 190, y = 20, width = 120, height = 62)
        self.button3['command'] = self.Home

    def Save(self):
        print('Save')

    def Reset(self):
        print('Reset')

    def Home(self):
        print('Home')

if __name__ == '__main__':
    a = Container4(0)
    a.w1.mainloop()