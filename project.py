# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk() #หน้าจอหลักโปรแกรม
root.geometry('780x580+280+70')
root.title("How Smoking Affects Your Life")
root.configure(bg='light blue')
label1 = Label(root, text="How Smoking Affects Your Life!",fg='blue',bg = 'light blue', font = "Times 30 bold").place(x=165, y=200)
labelna = Label(root, text="โปรแกรมสำหรับผู้ที่ต้องการเลิกบุหรี่",fg='blue',bg = 'light blue', font = "Times 30 bold").place(x=160, y=252)
button1 = Button(root, text="เข้าสู่โปรแกรม",command = start, font = "Times 15 bold").place(x=200, y=330)
def exit1():
    root.destroy()
button2 = Button(root, text="ออกจากโปรแกรม",command = exit1, font = "Times 15 bold").place(x=430, y=330)
    
root.mainloop()
