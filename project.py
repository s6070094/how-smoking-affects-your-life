# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk() #หน้าจอหลักโปรแกรม
root.geometry('780x580+280+70')
root.title("How Smoking Affects Your Life")
root.configure(bg='light green')
label1 = Label(root, text="ยินดีต้อนรับเข้าสู่แอพ",fg='blue',bg = 'light blue')
label1.grid(row=0,column=0)
button1 = Button(root, text="เข้าสู่หน้าหลัก",fg='red',command = start)
button1.grid(row=1,column=2)
button2 = Button(root, text="ออกจากโปรแกรม",fg='red',command = exit)
button2.grid(row=1,column=3)
root.mainloop()
