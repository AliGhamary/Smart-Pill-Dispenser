from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
import sys, os
from xml.dom.expatbuilder import parseFragmentString
from time import sleep
from os.path import exists
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


class onKeyboard():
  def __init__(self,text_label=None,exp=""):
    self.text_box_label=text_label
    self.exp=exp

  def press(self,num):
    self.exp = self.exp + str(num)
    print(self.exp)
    text_box_label.delete(0,END)
    text_box_label.insert(0,self.exp)

  def Backspace(self):
    self.exp = self.exp[:-1]
    print(self.exp)
    text_box_label.delete(0,END)
    text_box_label.insert(0,self.exp)

  def Clear(self):
     self.exp=""
     text_box_label.delete(0,END)
  def Shift(self,key):
    global is_shift
    is_shift = not is_shift
    self.display(key)

  def display(self,key):
    if (True):
        # Adding keys line wise
        # First Line Button
        # tilda = Button(key, text='~', width=6, command=lambda:  self.press('~'))
        # tilda.place(x = 2, y = 280, width = 55, height = 55)
        color='#23c4ed'

        num1 = Button(key, text='!', width=6, command=lambda:  self.press('!'),background=color)
        num1.place(x = 60, y = 280, width = 55, height = 55)

        num2 = Button(key, text='@', width=6, command=lambda:  self.press('@'),background=color)
        num2.place(x = 120, y = 280, width = 55, height = 55)

        num3 = Button(key, text='#', width=6, command=lambda:  self.press('#'),background=color)
        num3.place(x = 180, y = 280, width = 55, height = 55)

        num4 = Button(key, text='$', width=6, command=lambda:  self.press('$'),background=color)
        num4.place(x = 240, y = 280, width = 55, height = 55)

        num5 = Button(key, text='%', width=6, command=lambda:  self.press('%'),background=color)
        num5.place(x = 300, y = 280, width = 55, height = 55)

        num6 = Button(key, text='^', width=6, command=lambda:  self.press('^'),background=color)
        num6.place(x = 360, y = 280, width = 55, height = 55)

        num7 = Button(key, text='&', width=6, command=lambda:  self.press('&'),background=color)
        num7.place(x = 420, y = 280, width = 55, height = 55)

        num8 = Button(key, text='*', width=6, command=lambda:  self.press('*'),background=color)
        num8.place(x = 480, y = 280, width = 55, height = 55)

        num9 = Button(key, text='(', width=6, command=lambda:  self.press('('),background=color)
        num9.place(x = 540, y = 280, width = 55, height = 55)

        num0 = Button(key, text=')', width=6, command=lambda:  self.press(')'),background=color)
        num0.place(x = 600, y = 280, width = 55, height = 55)

        under = Button(key, text='_', width=6, command=lambda:  self.press('_'),background=color)
        under.place(x = 660, y = 280, width = 55, height = 55)

        plus = Button(key, text='+', width=6, command=lambda:  self.press('+'),background=color)
        plus.place(x = 720, y = 280, width = 55, height = 55)

        backspace = Button(
            key, text='BackSpace', font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7),width=6, command=self.Backspace,background=color)
        backspace.place(x = 780, y = 280, width = 55, height = 55)

        num_1 =  Button(key, text='1', width=6, command=lambda:  self.press('1'),background=color)
        num_1.place(x = 855, y = 280, width = 50, height = 50)

        num_2 =  Button(key, text='2', width=6, command=lambda:  self.press('2'),background=color)
        num_2.place(x = 913, y = 280, width = 50, height = 50)

        num_3 =  Button(key, text='3', width=6, command=lambda:  self.press('3'),background=color)
        num_3.place(x = 970, y = 280, width = 50, height = 50)
        # Second Line Buttons

        # tab_button = Button(key, text='Tab',font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 7), width=6,
        #                         command=lambda:  self.press('\t'))
        # tab_button.place(x = 2, y = 340, width = 55, height = 55)

        Q = Button(key, text='Q', width=6, command=lambda:  self.press('Q'),background=color)
        Q.place(x = 60, y = 340, width = 55, height = 55)

        W = Button(key, text='W', width=6, command=lambda:  self.press('W'),background=color)
        W.place(x = 120, y = 340, width = 55, height = 55)

        E = Button(key, text='E', width=6, command=lambda:  self.press('E'),background=color)
        E.place(x = 180, y = 340, width = 55, height = 55)
        R = Button(key, text='R', width=6, command=lambda:  self.press('R'),background=color)
        R.place(x = 240, y = 340, width = 55, height = 55)

        T = Button(key, text='T', width=6, command=lambda:  self.press('T'),background=color)
        T.place(x = 300, y = 340, width = 55, height = 55)

        Y = Button(key, text='Y', width=6, command=lambda:  self.press('Y'),background=color)
        Y.place(x = 360, y = 340, width = 55, height = 55)

        U = Button(key, text='U', width=6, command=lambda:  self.press('U'),background=color)
        U.place(x = 420, y = 340, width = 55, height = 55)

        I = Button(key, text='I', width=6, command=lambda:  self.press('I'),background=color)
        I.place(x = 480, y = 340, width = 55, height = 55)

        O = Button(key, text='O', width=6, command=lambda:  self.press('O'),background=color)
        O.place(x = 540, y = 340, width = 55, height = 55)

        P = Button(key, text='P', width=6, command=lambda:  self.press('P'),background=color)
        P.place(x = 600, y = 340, width = 55, height = 55)

        curly_l = Button(
            key, text='{', width=6, command=lambda:  self.press('{'),background=color)
        curly_l.place(x = 660, y = 340, width = 55, height = 55)

        curly_r = Button(key, text='}', width=6,
                             command=lambda:  self.press('}'),background=color)
        curly_r.place(x = 720, y = 340, width = 55, height = 55)
        
        back_slash = Button(key, text='\\', width=6,
                             command=lambda:  self.press('\\'),background=color)
        back_slash.place(x = 780, y = 340, width = 55, height = 55)
        
        num_4 =  Button(key, text='4', width=6, command=lambda:  self.press('4'),background=color)
        num_4.place(x =855, y = 340, width = 50, height = 50)

        num_5 =  Button(key, text='5', width=6, command=lambda:  self.press('5'),background=color)
        num_5.place(x = 913, y = 340, width = 50, height = 50)

        num_6 =  Button(key, text='6', width=6, command=lambda:  self.press('6'),background=color)
        num_6.place(x = 970, y = 340, width = 50, height = 50)
        # Third Line Buttons

        A = Button(key, text='A', width=6, command=lambda:  self.press('A'),background=color)
        A.place(x = 60, y = 400, width = 55, height = 55)

        S = Button(key, text='S', width=6, command=lambda:  self.press('S'),background=color)
        S.place(x = 120, y = 400, width = 55, height = 55)

        D = Button(key, text='D', width=6, command=lambda:  self.press('D'),background=color)
        D.place(x = 180, y = 400, width = 55, height = 55)

        F = Button(key, text='F', width=6, command=lambda:  self.press('F'),background=color)
        F.place(x = 240, y = 400, width = 55, height = 55)

        G = Button(key, text='G', width=6, command=lambda:  self.press('G'),background=color)
        G.place(x = 300, y = 400, width = 55, height = 55)

        H = Button(key, text='H', width=6, command=lambda:  self.press('H'),background=color)
        H.place(x = 360, y = 400, width = 55, height = 55)

        J = Button(key, text='J', width=6, command=lambda:  self.press('J'),background=color)
        J.place(x = 420, y = 400, width = 55, height = 55)

        K = Button(key, text='K', width=6, command=lambda:  self.press('K'),background=color)
        K.place(x = 480, y = 400, width = 55, height = 55)

        L = Button(key, text='L', width=6, command=lambda:  self.press('L'),background=color)
        L.place(x = 540, y = 400, width = 55, height = 55)

        colon = Button(key, text=':', width=6,
                           command=lambda:  self.press(':'),background=color)
        colon.place(x = 600, y = 400, width = 55, height = 55)

        quotation = Button(key, text='"', width=6,
                               command=lambda:  self.press('"'),background=color)
        quotation.place(x = 660, y = 400, width = 55, height = 55)

        pipe =  Button(key, text='|', width=6, command=lambda:  self.press('|'),background=color)
        pipe.place(x = 720, y = 400, width = 55, height = 55)

        # enter =  Button(key, text='Enter', width=6,
        #                    command=lambda:  self.press('\n'))
        # enter.place(x = 780, y = 400, width = 55, height = 55)

        num7 =  Button(key, text='7', width=6, command=lambda:  self.press('7'),background=color)
        num7.place(x = 855, y = 400, width = 50, height = 50)

        num8 =  Button(key, text='8', width=6, command=lambda:  self.press('8'),background=color)
        num8.place(x = 913, y = 400, width = 50, height = 50)


        num9 =  Button(key, text='9', width=6, command=lambda:  self.press('9'),background=color)
        num9.place(x = 970, y = 400, width = 50, height = 50)


        # Fourth line Buttons

        # shift =  Button(key, text='Shift', width=6, command=lambda: self.Shift(key))
        # shift.place(x = 2, y = 460, width = 55, height = 55)

        Z =  Button(key, text='Z', width=6, command=lambda:  self.press('Z'),background=color)
        Z.place(x = 60, y = 460, width = 55, height = 55)
        X =  Button(key, text='X', width=6, command=lambda:  self.press('X'),background=color)
        X.place(x = 120, y = 460, width = 55, height = 55)

        C =  Button(key, text='C', width=6, command=lambda:  self.press('C'),background=color)
        C.place(x = 180, y = 460, width = 55, height = 55)

        V =  Button(key, text='V', width=6, command=lambda:  self.press('V'),background=color)
        V.place(x = 240, y = 460, width = 55, height = 55)

        B =  Button(key, text='B', width=6, command=lambda:  self.press('B'),background=color)
        B.place(x = 300, y = 460, width = 55, height = 55)

        N =  Button(key, text='N', width=6, command=lambda:  self.press('N'),background=color)
        N.place(x = 360, y = 460, width = 55, height = 55)

        M =  Button(key, text='M', width=6, command=lambda:  self.press('M'),background=color)
        M.place(x = 420, y = 460, width = 55, height = 55)

        ang_l =  Button(key, text='<', width=6, command=lambda:  self.press('<'),background=color)
        ang_l.place(x = 480, y = 460, width = 55, height = 55)

        ang_r =  Button(key, text='>', width=6, command=lambda:  self.press('>'),background=color)
        ang_r.place(x = 540, y = 460, width = 55, height = 55)

        question =  Button(key, text='?', width=6,
                              command=lambda:  self.press('?'),background=color)
        question.place(x = 600, y = 460, width = 55, height = 55)

        clear =  Button(key, text='Clear', width=6, command=self.Clear,background=color)
        clear.place(x = 660, y = 460, width = 55, height = 55)

        num_0 =  Button(key, text='0', width=6, command=lambda:  self.press('0'),background=color)
        num_0.place(x=903, y = 460, width = 80, height = 50)
        # Fifth Line Buttons

        space =  Button(key, text='Space', width=6,
                           command=lambda:  self.press(' '),background=color)
        space.place(x = 120, y = 520, width = 450, height = 70)

        
       

class HomeScreen():
    def __init__(self,home=True):
        
        self.color_container='#23c4ed'
        self.home=home

        #reading from file 
        self.initial_timer_value = [["Container 1",'12:00 AM'], ["Container 2",'12:00 AM'], ["Container 3",'12:00 AM'], ["Container 4",'12:00 AM'],
                       ["Container 5",'12:00 AM'], ["Container 6",'12:00 AM'], ["Container 7",'12:00 AM'], ["Container 8",'12:00 AM']]
        
        self.fileName = 'features'
        text_to_save=self.arr_to_txt(self.initial_timer_value)
        print(text_to_save)
        if not exists(self.fileName):
          with open(self.fileName, 'w') as f:
            f.write(text_to_save)
            
        if exists(self.fileName):
            with open(self.fileName) as f:
               readf =  f.read()
               total_containers=readf.split(",")
               for i in range (len(total_containers)-1):
                  t=total_containers[i].split(";")
                  self.initial_timer_value[7-i][0]=t[0]
                  self.initial_timer_value[7-i][1]=t[1]

        self.btn1=self.initial_timer_value[0][0]
        self.btn2=self.initial_timer_value[1][0]
        self.btn3=self.initial_timer_value[2][0]
        self.btn4=self.initial_timer_value[3][0]
        self.btn5=self.initial_timer_value[4][0]
        self.btn6=self.initial_timer_value[5][0]
        self.btn7=self.initial_timer_value[6][0]
        self.btn8=self.initial_timer_value[7][0]
        self.gui()

    def arr_to_txt(self,arr):
        txt_out=""
        for i in range(len(arr)):
            txt_out=str(arr[i][0])+";"+str(arr[i][1])+","+txt_out 
        return txt_out
    def gui(self):
        self.w1 = Tk()
        self.w1.geometry('1024x600')
        self.w1.configure(bg='blue')
        self.w1.maxsize(width=1024,height=600)
        self.w1.minsize(width=1024,height=600)
       
        self.label = Label(self.w1, text="Hello, please select a container to continue",font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 12, weight = "normal"), cursor = "arrow", state = "normal",bg="#ffffff")
        self.label.place(x = 210, y = 20, width = 390, height = 52)
        self.button1 = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button1.place(x = 150, y = 100, width = 200, height = 52)
        self.button1['command'] = lambda: self.configure(param = 1)
        self.button1['text'] = self.btn1
        self.button2 = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button2.place(x = 150, y = 180, width = 200, height = 52)
        self.button2['command'] =lambda: self.configure(param = 2)
        self.button2['text'] = self.btn2
        self.button3 = Button(self.w1,font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button3.place(x = 150, y = 260, width = 200, height = 52)
        self.button3['command'] =  lambda:self.configure(param = 3)
        self.button3['text'] = self.btn3
        self.button4 = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button4.place(x = 150, y = 340, width = 200, height = 52)
        self.button4['command'] = lambda:self.configure(param = 4)
        self.button4['text'] = self.btn4
        
        #new container buttons
        self.button5 = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button5.place(x = 450, y = 100, width = 200, height = 52)
        self.button5['command'] = lambda: self.configure(param = 5)
        self.button5['text'] = self.btn5
        self.button6 = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button6.place(x = 450, y = 180, width = 200, height = 52)
        self.button6['command'] =lambda: self.configure(param = 6)
        self.button6['text'] = self.btn6
        self.button7 = Button(self.w1,font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button7.place(x = 450, y = 260, width = 200, height = 52)
        self.button7['command'] =  lambda:self.configure(param = 7)
        self.button7['text'] = self.btn7
        self.button8 = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="16",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button8.place(x = 450, y = 340, width = 200, height = 52)
        self.button8['command'] = lambda:self.configure(param = 8)
        self.button8['text'] = self.btn8
      
       
    def configure(self,param):
        global text_box_label
        self.w1.destroy()
        self.home=False
        self.w1 = Tk()
        sreenKeyboard=onKeyboard()
        self.w1.geometry('1024x600')
        self.w1.configure(bg='blue')
        self.w1.maxsize(width=1024,height=600)
        self.w1.minsize(width=1024,height=600)
        text_box_label = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 16), cursor = "arrow", state = "normal")
        text_box_label.place(x = 150, y = 150, width = 350, height = 42)
        self.button1 = Button(self.w1, text = "Save", font = tkinter.font.Font(family = "Helvetica", size="12",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button1.place(x = 100, y = 200, width = 120, height = 62)
        self.button1['command'] = lambda:self.Save(param)

        # new timer button
        time_val=self.initial_timer_value[param-1][1].split(":")
        time_val2=time_val[1].split(" ")
        self.timer_value_hours = int(time_val[0])
        self.timer_value_minutes = int(time_val2[0])
        self.timer_AM_PM = time_val2[1]

        self.label_timer = Label(self.w1, text="TIMER",font = tkinter.font.Font(family = "Helvetica", size="24", weight="bold",slant="italic"), cursor = "arrow", state = "normal",bg='blue',fg='white')
        self.label_timer.place(x =650, y = 40, width = 120, height = 52)
        self.label1_timer = Label(self.w1, text='{:0>2}:{:0>2} {}'.format(self.timer_value_hours, self.timer_value_minutes, self.timer_AM_PM),font = tkinter.font.Font(family = "Helvetica", size="35", weight="bold"), cursor = "arrow", state = "normal",bg='white')
        self.label1_timer.place(x = 620, y = 100, width = 200, height = 80)
        self.button1_timer = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="11", weight="bold"), text="TIMER UP",bg='#23c4ed',activebackground='grey',command=self.timer_up)
        self.button1_timer.place(x = 850, y = 80, width = 120, height = 62)
        self.button2_timer = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="11", weight="bold"), text="TIMER DOWN",bg='#23c4ed',activebackground='grey',command=self.timer_down)
        self.button2_timer.place(x = 850, y = 180, width = 120, height = 62)
        self.button3_timer = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="11", weight="bold"), text="TIMER SAVE",bg='#23c4ed',activebackground='grey',command=lambda:self.timer_save(param))
        self.button3_timer.place(x = 650, y = 200, width = 120, height = 62)
        self.button4_timer = Button(self.w1, font = tkinter.font.Font(family = "Helvetica", size="11", weight="bold"), text="AM/PM",bg='#23c4ed',activebackground='grey',command=lambda:self.timer_AMPM_Toggle())
        self.button4_timer.place(x = 870, y = 30, width = 70, height = 30)

      

        self.button2 = Button(self.w1, text = "Reset", font = tkinter.font.Font(family = "Helvetica", size="12",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button2.place(x = 430, y = 200, width = 130, height = 62)
        self.button2['command'] = lambda:self.Reset(param)
        self.button2 = Button(self.w1, text = "Run", font = tkinter.font.Font(family = "Helvetica", size="12",weight="bold"), cursor = "arrow", state = "normal",bg=self.color_container)
        self.button2.place(x = 280, y = 200, width = 100, height = 62)
        self.button2['command'] = lambda:self.motor_command(param)
        self.label = Label(self.w1, text="Please type the name of the pill", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 14, weight = "normal"), cursor = "arrow", state = "normal",bg='#ffff00')
        self.label.place(x = 150, y = 80, width = 350, height = 50)
        self.button3 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "Helvetica", size="12",weight="bold"), cursor = "arrow", state = "normal",bg= self.color_container)
        self.button3.place(x = 260, y = 10, width = 120, height = 62)
        self.button3['command'] = self.Home
        sreenKeyboard.text_label=text_box_label
        sreenKeyboard.display(self.w1)


    def timer_up(self):
      self.timer_last_hour = self.timer_value_hours
      self.timer_value_minutes += 10
      
      if self.timer_value_minutes >= 60:
         self.timer_value_hours+=1
         self.timer_value_minutes = 0
      
      if self.timer_value_hours == 12 and self.timer_last_hour == 11:
         # self.timer_value_hours = 12
         self.timer_value_minutes = 0
         if self.timer_AM_PM == 'AM':
            self.timer_AM_PM ='PM'
         else:
            self.timer_AM_PM ='AM'

      if self.timer_value_hours == 13 and self.timer_last_hour ==12:
         self.timer_value_hours = 1


     
      self.label1_timer.configure(text='{:0>2}:{:0>2} {}'.format(self.timer_value_hours, self.timer_value_minutes, self.timer_AM_PM))
   
    def timer_down(self):
      #counter in initial positon
      
      self.timer_last_hour = self.timer_value_hours
      self.timer_value_minutes-=10
      if self.timer_value_minutes < 0:
         self.timer_value_hours-=1
         self.timer_value_minutes = 50
      
      if self.timer_value_hours == 0 and self.timer_last_hour==1:
         self.timer_value_hours = 12
      
      if self.timer_value_hours == 11 and self.timer_last_hour==12:
         if self.timer_AM_PM == 'AM':
            self.timer_AM_PM ='PM'
         else:
            self.timer_AM_PM ='AM'

      self.label1_timer.configure(text='{:0>2}:{:0>2} {}'.format(self.timer_value_hours, self.timer_value_minutes, self.timer_AM_PM))

    def timer_save(self, param):
      param=param-1
      self.initial_timer_value[param][1]=str(str(self.timer_value_hours)+":"+str(self.timer_value_minutes)+" "+self.timer_AM_PM)
      text_to_save=self.arr_to_txt(self.initial_timer_value)
      with open(self.fileName, 'w') as f:
            f.write(text_to_save)

    def timer_AMPM_Toggle(self):
      if self.timer_AM_PM == 'AM':
         self.timer_AM_PM = 'PM'
      else:
         self.timer_AM_PM = 'AM'
      self.label1_timer.configure(text='{:0>2}:{:0>2} {}'.format(self.timer_value_hours, self.timer_value_minutes, self.timer_AM_PM))

    def Save(self,param):
        global text_box_label
        btn_label=str(text_box_label.get())
        btn_label=btn_label.rstrip("\n")
        if param==1:
           self.btn1=btn_label
        elif param==2:
           self.btn2=btn_label
        elif param==3:
           self.btn3=btn_label
        elif param==4:
           self.btn4=btn_label
        elif param==5:
           self.btn5=btn_label
        elif param==6:
           self.btn6=btn_label
        elif param==7:
           self.btn7=btn_label
        elif param==8:
           self.btn8=btn_label
        param=param-1
        self.initial_timer_value[param][0]=str(btn_label)
        text_to_save=self.arr_to_txt(self.initial_timer_value)
        with open(self.fileName, 'w') as f:
            f.write(text_to_save)
   

    def Reset(self,param):
        if param==1:
           self.btn1="Container 1"
        elif param==2:
           self.btn2="Container 4"
        elif param==3:
           self.btn3="Container 3"
        elif param==4:
           self.btn4="Container 4"

        elif param==5:
           self.btn5="Container 5"
        elif param==6:
           self.btn6="Container 6"
        elif param==7:
           self.btn7="Container 7"
        elif param==8:
           self.btn8="Container 8"
        print('Reset')

    def motor_command(self,param):
         if param==1:
            self.motor_1()
         elif param==2:
            self.motor_2()
         elif param==3:
            self.motor_3()
         elif param==4:
            self.motor_4()

         # new motors
         elif param==5:
            self.motor_1()
         elif param==6:
            self.motor_2()
         elif param==7:
            self.motor_3()
         elif param==8:
            self.motor_4()
    
    
    ## HAVE TO ADD NEW MOTORS FUNCTIONS

    def motor_1(self):
       print("Motor 1")

       kit.servo[0].angle = 0
       sleep(.5)
       kit.servo[0].angle = 180
       sleep(.5)
       kit.servo[0].angle = 0
      #  GPIO.setmode(GPIO.BOARD)
      #  GPIO.setup(7,GPIO.OUT)

      #  pwm=GPIO.PWM(7,50)
      #  pwm.start(0)

      #  pwm.ChangeDutyCycle(5) #left
      #  sleep(1)
      #  #pwm.ChangeDutyCycle(7.5) # neutral position not neeeded since its a 360deg servo
      #  #sleep(1)
      #  pwm.ChangeDutyCycle(12.5) # right
      #  sleep(1)

      #  pwm.stop()
      #  GPIO.cleanup()  

    def motor_2(self):
       print("Motor 2")

       kit.servo[1].angle = 0
       sleep(.5)
       kit.servo[1].angle = 180
       sleep(.5)
       kit.servo[1].angle = 0
      #  GPIO.setmode(GPIO.BOARD)
      #  GPIO.setup(11,GPIO.OUT)

      #  pwm=GPIO.PWM(11,50)
      #  pwm.start(0)

      #  pwm.ChangeDutyCycle(5) #left
      #  sleep(1)
      #  pwm.ChangeDutyCycle(12.5) # right
      #  sleep(1)

      #  pwm.stop()
      #  GPIO.cleanup() 
    
    def motor_3(self):
        print("Motor 3")
        kit.servo[2].angle = 0
        sleep(.5)
        kit.servo[2].angle = 180
        sleep(.5)
        kit.servo[2].angle = 0
      #   GPIO.setmode(GPIO.BOARD)
      #   GPIO.setup(13,GPIO.OUT)

      #   pwm=GPIO.PWM(13,50)
      #   pwm.start(0)

      #   pwm.ChangeDutyCycle(5) #left
      #   sleep(1)
      #   pwm.ChangeDutyCycle(12.5) # right
      #   sleep(1)

      #   pwm.stop()
      #   GPIO.cleanup()
    def motor_4(self):
        print("Motor 4")

        kit.servo[3].angle = 0
        sleep(.5)
        kit.servo[3].angle = 180
        sleep(.5)
        kit.servo[3].angle = 0
      #   GPIO.setmode(GPIO.BOARD)
      #   GPIO.setup(15,GPIO.OUT)

      #   pwm=GPIO.PWM(15,50)
      #   pwm.start(0)

      #   pwm.ChangeDutyCycle(5) #left
      #   sleep(1)
      #   pwm.ChangeDutyCycle(12.5) # right
      #   sleep(1)

      #   pwm.stop()
      #   GPIO.cleanup()   
          
    def Home(self):
        self.w1.destroy()
        self.gui()

class controller():
   def sens():
      #GPIO SETUP
      channel = 17
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(channel, GPIO.IN)
      
      def callback(channel):
            if GPIO.input(channel):
                     print ("Movement Detected!")
            else:
                     print ("Movement Detected!")
      
      GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
      GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
#This is a test

if __name__ == '__main__':
    a = HomeScreen(0)
    a.w1.mainloop()