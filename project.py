# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk() #หน้าจอหลักโปรแกรม
root.geometry('780x580+280+70')
root.title("How Smoking Affects Your Life")
root.configure(bg='light blue')
label1 = Label(root, text="How Smoking Affects Your Life!",fg='blue',bg = 'light blue', font = "Times 30 bold").place(x=165, y=200)
labelna = Label(root, text="โปรแกรมสำหรับผู้ที่ต้องการเลิกบุหรี่",fg='blue',bg = 'light blue', font = "Times 30 bold").place(x=160, y=252)
def start(): #หน้าที่2 --> หน้ากรอกข้อมูลพร้อมปุ่มคำนวณ
    root.destroy()
    global input_num1
    main = Tk()
    main.title("How Smoking Affects Your Life")
    main.geometry('780x580+280+70')
    main.configure(bg='light green')
    labeln = Label(main, text="          ",bg = 'light green')
    labeln.grid(row=1,column=1)
    labelnn = Label(main, text="          ",bg = 'light green')
    labelnn.grid(row=2,column=1)
    labelnnn = Label(main, text="          ",bg = 'light green')
    labelnnn.grid(row=3,column=1)
    labelnnnn = Label(main, text="          ",bg = 'light green')
    labelnnnn.grid(row=4,column=1)
    labelnnn1 = Label(main, text="          ",bg = 'light green')
    labelnnn1.grid(row=5,column=1)
    labelnnnn2 = Label(main, text="          ",bg = 'light green')
    labelnnnn2.grid(row=6,column=1)
    label2 = Label(main, text="       คุณสูบบุหรี่เฉลี่ย  ",fg='blue',bg = 'light green', font = "Times 40 bold")
    label2.grid(row=7,column=1)
    input_num1 = Entry(main)
    input_num1.grid(row=7,column=2)#ส่วนรับอินพุท
    label3 = Label(main, text='   มวน/วัน',fg='blue',bg = 'light green', font = "Times 40 bold")
    label3.grid(row=7,column=3)
    def process_2(): #ส่วนคำนวณที่ฟังก์ชั่นprocessเรียกใช้
        a = input_num1.get()
        b = str(((int(a)*7*365)/1440))+' วัน '+str(((int(a)*7*365)%1440)/60)+' ชั่วโมง'
        return b
    def process_3(): #func processเรียกอีกที
        num = input_num1.get()
        money = str(((int(num)*365)/20)*70)
        return money
    def process():#หน้าที่สาม --> หน้าโชว์ผลการคำนวณ
        pop = Tk()
        pop.configure(bg = "light pink")
        pop.title("How Smoking Affects Your Life")
        pop.geometry('780x580+280+70')
        label4 = Label(pop, text="ชีวิตลดลงเฉลี่ย " + str(process_2() + " ต่อปี"), font = "Times 45 bold",fg = 'red',bg ='light pink').place(x=70, y=200)
        label_money = Label(pop, text="   สูญเสียเงินเฉลี่ย " + str(process_3() + " บาท ต่อปี"), font = "Times 30 ",fg = 'purple',bg = 'light pink').place (x=170,y=260)
        label5 = Label(pop, text="คุณต้องการคำแนะนำการเลิกบุหรี่หรือไม่?", font = "Times 20 bold",fg = 'blue',bg = 'light pink').place(x=220, y=310)
        def yes():#หน้าสุดท้าย --> แนะนำการเลิกบุหรี่
            main.destroy()
            pop.destroy()
            last = Tk()
            last.configure(bg = "light yellow")
            last.title("How Smoking Affects Your Life")
            last.geometry('780x580+280+70')
            label6 = Label(last, text="คำแนะนำ", font = "Times 30 bold",fg = 'dark green',bg = 'light yellow').place(x=310 ,y=20)
            label7 = Label(last, text="1.ขอคำปรึกษาจากคนที่สามารถเลิกสูบบุหรี่ได้สำเร็จมาแล้ว หรือขอคำแนะนำในการเลิกบุหรี่ได้ที่ โทร.1600", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=70)
            label8 = Label(last, text="2.ควรบอกให้คนใกล้ชิดทราบถึงความตั้งใจที่จะเลิกบุหรี่ เพราะกำลังใจจากคนรอบข้างจะช่วยให้คุณมีความพยายามที่จะเลิกสูบบุหรี่ได้", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=110)
            label9 = Label(last, text="3.ควรวางแผนการปฏิบัติตัว โดยกำหนดวันที่จะลงมือเลิกสูบบุหรี่ เช่น วันเกิดตัวเองหรือของลูก", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=150)
            label10 = Label(last, text="4.ควรเตรียมตัวให้พร้อม ด้วยการทิ้งอุปกรณ์ที่เกี่ยวข้องกับบุหรี่ให้หมด เตรียมผลไม้รสเปรี้ยวหรือของขบเคี้ยว เพื่อช่วยลดความอยาก", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=190)
            label11 = Label(last, text="5.เมื่อถึงวันลงมือ ควรตื่นนอนด้วยความสดชื่น บอกตัวเองว่าคุณกำลังทำสิ่งที่ดีที่สุดให้กับตนเองและคนใกล้ชิด", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=230)
            label12 = Label(last, text="6.ในระหว่างนี้ขอให้คุณหลีกเลี่ยงกิจกรรมที่จะทำให้คุณอยากสูบบุหรี่ เช่น ถ้าเคยดื่มกาแฟ หรือเครื่องดื่มที่มีแอลกอฮอล์", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=270)
            label13 = Label(last, text="7.เมื่อรู้สึกเครียด ให้หยุดพักสมองสักครู่ คลายความเครียด ระลึกถึงเสมอว่า มีคนไม่สูบบุหรี่อีกมากที่คลายเครียดได้โดยไม่ต้องสูบบุหรี่", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=310)
            label14 = Label(last, text="8.ควรจัดเวลาออกกำลังกายบ้างอย่างน้อยวันละ 15-20 นาที เพราะนอกจากจะเป็นการควบคุมน้ำหนัก ยังช่วยให้สมองปลอดโปร่ง", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=350)
            label15 = Label(last, text="9.อย่าคิดว่ากลับไปลองสูบบ้างเป็นครั้งคราวคงไม่เป็นไร เพราะการลองสูบบุหรี่เพียงมวนเดียวอาจหมายถึงการหวนคืนไปสูความเคยชินเก่าๆ", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=390)
            label16 = Label(last, text="10.หากต้องหันกลับไปสูบอีก ไม่ได้หมายถึงคุณเป็นคนล้มเหลว อย่างน้อยคุณก็ได้เรียนรู้ที่จะปรับปรุงตัวเอง ขอเพียงพยายามต่อไป", font = "Times 13 bold",fg = 'dark green',bg = 'light yellow').place(x=15 ,y=430)
            def ex():
                last.destroy()
            buttonex = Button(last, text = "ออกจากโปรแกรม",command = ex, font = "Times 15 bold").place(x=320,y=490)
        button3 = Button(pop,text = "ต้องการ", command = yes, font = "Times 15 bold").place(x=300, y=360)
        def exitall():
            pop.destroy()
            main.destroy()
        button4 = Button(pop,text = "ไม่ต้องการ", command = exitall, font = "Times 15 bold").place(x=410, y=360) 
    button_main = Button(main, text="คำนวณ",command = process, font = "Times 25 bold").place(x=340, y=350)
button1 = Button(root, text="เข้าสู่โปรแกรม",command = start, font = "Times 15 bold").place(x=200, y=330)
def exit1():
    root.destroy()
button2 = Button(root, text="ออกจากโปรแกรม",command = exit1, font = "Times 15 bold").place(x=430, y=330)
    
root.mainloop()
