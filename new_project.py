from tkinter import *
from tkinter import ttk
import sqlite3

'''conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
c = conn.cursor()
c.execute("""CREATE TABLE menulist (id integer PRIMARY KEY AUTOINCREMENT,
    Menu varchar(100) NOT NULL,
    amoute varchar(30) NOT NULL)""")
conn.commit()
conn.close()'''

def frist_window():
    global root
    root = Tk()
    root.option_add("*font","thaisarabun 25")
    root.geometry("800x500")
    root.title("ยินดีต้อนรับ")
    photo01 = PhotoImage(file = "1st_pic.png")
    Label(root,image = photo01,bg='hotpink1').pack(fill=X)
    Button(root,text = "เข้าร้าน",width=10,command = pid).place(x=305,y=270)
    mainloop()

def pid():
    root.destroy()
    main_window()
def paimenu():
    ro.destroy()
    deletetable()
    menu_window()
def gotomeet():
    menu1.destroy()
    meet_window()
def backfrommeet():
    meet.destroy()
    menu_window()
def gotopork():
    menu1.destroy()
    pork_window()
def backfrompork():
    pork.destroy()
    menu_window()
def gotodrink():
    menu1.destroy()
    drink_window()
def backfromdrink():
    drink.destroy()
    menu_window()
def backmain():
    menu1.destroy()
    main_window()
def openlistmenu():
    me.destroy()
    listmenu()
def gotolistmenu():
    ro.destroy()
    listmenu()
def huya():
    lm.destroy()
    menuedit()
def gotobill():
    ro.destroy()
    bill()
def huya2():
    lm.destroy()
    main_window()
def deletetable():
    conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
    c = conn.cursor()
    try:
        #c.execute( DELETE FROM menulist;
        #DELETE FROM sqlite_sequence WHERE name = "menulist")
        c.execute('DELETE FROM menulist')
        conn.commit()
        c.close
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
def main_window():
    global ro
    ro = Tk()
    ro.geometry("800x500")
    ro.option_add("*font","thaisarabun 25")
    ro.title("หน้าหลัก")
    photo02 = PhotoImage(file = "2nd_pic.png")
    Label(ro,image = photo02).pack(fill=X)
    Button(ro,text = "สั่งอาหาร",width=15,command = paimenu).place(x=270,y=170)
    Button(ro,text = "รายการที่สั่ง",width=15,command = gotolistmenu).place(x=270,y=250)
    Button(ro,text = "ใบเสร็จ",width=15,command = gotobill ).place(x=270,y=330)
    Button(ro,text = "ออกจากโปรแกม",width=15,command = ro.destroy).place(x=270,y=410)
    mainloop()

def menu_window():
    global menu1
    menu1 = Tk()
    menu1.geometry("800x500")
    menu1.option_add("*font","thaisarabun 15")
    menu1.title("สั่งอาหาร")
    photo03 = PhotoImage(file = "3rd_pic.png")
    Label(menu1,image = photo03,bg='hotpink1').pack(fill=X)
    Button(menu1,text = "เมนูเนื้อ",width=10,command = gotomeet).place(x=150,y=320)
    Button(menu1,text = "เมนูหมู",width=10,command = gotopork).place(x=335,y=320)
    Button(menu1,text = "เครื่องดื่ม",width=10,command = gotodrink).place(x=540,y=320)
    Button(menu1,text = "กลับหน้าหลัก",width=10,command = backmain).place(x=335,y=400)
    mainloop()
     
def meet_window():
    global meet
    def inputmenumeet():
        conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
        c = conn.cursor()
        try :
            sql = '''INSERT INTO menulist (Menu,amoute) VALUES (?,?)'''
            data = (meet_menu.get(),meet_amount.get())
            c.execute(sql,data)
            conn.commit()
            c.close()
        except sqlite3.Error as e:
            print("Failed to insert : ",e)
        finally :
            if conn :
                conn.close()
    meet = Tk()
    meet.geometry("800x500")
    meet.option_add("*font","thaisarabun 20")
    meet.title("เมนูเนื้อ")
    photo04 = PhotoImage(file = "4th_pic.png")
    Label(meet,image = photo04,bg='hotpink1').pack(fill=X)
    meetmenu = ["ลาบดิบ        70","ลาบสุก        70","ก้อยขม        70","ก้อยสุก        70","ต้มแซ่บ        60","อ่อม            50","ย่างพวงนม   70"]
    meet_menu = ttk.Combobox(meet,value = meetmenu,width = 10,state = "readonly")
    meet_menu.place(x = 270,y = 200)
    meet_amount = ttk.Combobox(meet,value = list(range(1,10)),width = 3)
    meet_amount.place(x = 500,y = 200)
    #meet_amount.current(0)
    Button(meet,text = "สั่งอาหาร",width=10,command = inputmenumeet).place(x = 320,y = 280)
    Button(meet,text = "กลับหน้าเมนู",width=10,command = backfrommeet).place(x = 320,y = 350)
    mainloop()

def pork_window():
    global pork
    def inputmenupork():
        conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
        c = conn.cursor()
        try :
            sql = '''INSERT INTO menulist (Menu,amoute) VALUES (?,?)'''
            data = (pork_menu.get(),pork_amount.get())
            c.execute(sql,data)
            conn.commit()
            c.close()
        except sqlite3.Error as e:
            print("Failed to insert : ",e)
        finally :
            if conn :
                conn.close()
    pork = Tk()
    pork.geometry("800x500")
    pork.option_add("*font","thaisarabun 20")
    pork.title("เมนูเนื้อ")
    photo05 = PhotoImage(file = "5th_pic.png")
    Label(pork,image = photo05,bg='hotpink1').pack(fill=X)
    porkmenu = ["ลาบหมู        60","น้ำตก          60","คอหมูย่าง     60","ย่างไส้          60","ต้มแซ่บ        50"]
    pork_menu = ttk.Combobox(pork,value = porkmenu,width = 10,state = "readonly")
    pork_menu.place(x = 270,y = 200)
    pork_amount = ttk.Combobox(pork,value = list(range(1,10)),width = 3)
    #pork_amount.current(0)
    pork_amount.place(x = 500,y = 200)
    Button(pork,text = "สั่งอาหาร",width=10,command = inputmenupork).place(x = 320,y = 280)
    Button(pork,text = "กลับหน้าเมนู",width=10,command = backfrompork).place(x = 320,y = 350)
    mainloop()

def drink_window():
    global drink
    def inputmenudrink():
        conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
        c = conn.cursor()
        try :
            sql = '''INSERT INTO menulist (Menu,amoute) VALUES (?,?)'''
            data = (drink_menu.get(),drink_amount.get())
            c.execute(sql,data)
            conn.commit()
            c.close()
        except sqlite3.Error as e:
            print("Failed to insert : ",e)
        finally :
            if conn :
                conn.close()
    drink = Tk()
    drink.geometry("800x500")
    drink.option_add("*font","thaisarabun 20")
    drink.title("เมนูเนื้อ")
    photo06 = PhotoImage(file = "6th_pic.png")
    Label(drink,image = photo06,bg='hotpink1').pack(fill=X)
    drinkmenu = ["น้ำเปล่า       15","น้ำโค้ก        30","น้ำอัดลม      30","เบียร์           70","น้ำแข็ง         20"]
    drink_menu = ttk.Combobox(drink,value = drinkmenu,width = 10,state = "readonly")
    drink_menu.place(x = 270,y = 200)
    drink_amount = ttk.Combobox(drink,value = list(range(1,10)),width = 3)
    #drink_amount.current(0)
    drink_amount.place(x = 500,y = 200)
    Button(drink,text = "สั่งอาหาร",width=10,command = inputmenudrink).place(x = 320,y = 280)
    Button(drink,text = "กลับหน้าเมนู",width=10,command = backfromdrink).place(x = 320,y = 350)
    mainloop()

def listmenu():
    global lm
    lm = Tk()
    lm.geometry("800x500")
    lm.option_add("*font","thaisarabun 15")
    lm.title("รายการที่สั่ง")
    photo07 = PhotoImage(file = "7th_pic.png")
    Label(lm,image = photo07).pack(fill=X)
    Label(lm,text = "รายการที่เลือก    ราคา" ,bg = "#CD853F",width = 20).place(x = 220,y=160)
    Label(lm,text = "จำนวน" ,bg = "#CD853F",width = 5).place(x = 480,y=160)
    conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(lm,text = result[x] ,bg = "#CD853F",width = 20).place(x = 220,y=200+x*29)
        c.execute('''SELECT amoute FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(lm,text = result[x] ,bg = "#CD853F",width = 5).place(x = 480,y=200+x*29)
        c.execute('''SELECT id FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(lm,text = result[x] ,bg = "#CD853F",width = 2).place(x = 220,y=200+x*29)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    Button(lm,text = "แก้ไขรายการ",bg = "gold",command = huya).place(x = 650,y = 400)
    Button(lm,text = "กลับหน้าหลัก",bg = "gold",command = huya2).place(x = 650,y = 450)
    mainloop()

def menuedit():
    global me
    me = Tk()
    me.geometry("800x500")
    me.option_add("*font","thaisarabun 15")
    me.title("แก้ไขรายการ")
    photo08 = PhotoImage(file = "8th_pic.png")
    Label(me,image = photo08).pack(fill=X)
    Label(me,text = "รายการที่เลือก    ราคา" ,bg = "#CD853F",width = 20).place(x = 70,y=160)
    Label(me,text = "จำนวน" ,bg = "#CD853F",width = 5).place(x = 290,y=160)
    conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(me,text = result[x] ,bg = "#CD853F",width = 20).place(x = 70,y=200+x*29)
        c.execute('''SELECT amoute FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(me,text = result[x] ,bg = "#CD853F",width = 5).place(x = 290,y=200+x*29)
        c.execute('''SELECT id FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(me,text = result[x] ,bg = "#CD853F",width = 2).place(x = 70,y=200+x*29)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    def changlist():
        conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
        c = conn.cursor()
        try:
            data = (c_menu.get(),c_amoute.get(),e_number.get())
            c.execute('''UPDATE menulist SET Menu =?, amoute =?  WHERE id = ?''',data)
            conn.commit()
            c.close()
            openlistmenu()
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn :
                conn.close()
    Label(me,text = "เลือกหมายเลขเมนูที่ต้องการเปลี่ยน").place(x=350,y = 160)
    e_number = ttk.Combobox(me,value = list(range(0,12)),width = 3)
    e_number.place(x = 450,y = 200)
    Label(me,text = "เลือกเมนูใหม่").place(x = 430,y = 250)
    Label(me,text = "จำนวน").place(x = 600,y = 250)
    allmenu = ["ลาบดิบ        70","ลาบสุก        70","ก้อยขม        70","ก้อยสุก        70","ต้มแซ่บ        60","อ่อม            50","ย่างพวงนม    70",
                "ลาบหมู        60","น้ำตก          60","คอหมูย่าง     60","ย่างไส้          60","ต้มแซ่บ        50","น้ำเปล่า       15","น้ำโค้ก        30","น้ำอัดลม      30","เบียร์           70","น้ำแข็ง         20"]
    c_menu = ttk.Combobox(me,value = allmenu,width = 15,state = "readonly")
    c_menu.place(x = 380,y = 300)
    c_amoute = ttk.Combobox(me,value = list(range(0,10)),width = 3)
    c_amoute.place(x = 600,y = 300)
    Button(text = "ยืนยันการแก้ไข",bg = "gold",command = changlist).place(x = 415,y = 400)
    mainloop()

def bill():
    global bil
    bil = Tk()
    bil.geometry("800x500")
    bil.option_add("*font","thaisarabun 15")
    bil.title("ใบเสร็จ")
    Label(bil,text = "-"*800).pack(fill = X)
    Label(bil,text = "ส.สุสานการลาบ \n ใบเสร็จ").pack(fill = X)
    Label(bil,text = "-"*800).pack(fill = X)
    Label(bil,text = "รายการที่เลือก    ราคา",width = 20).place(x = 240,y=110)
    Label(bil,text = "จำนวน" ,width = 5).place(x = 500,y=110)
    conn = sqlite3.connect(r"D:\Akaradech_Python\new_project.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(bil,text = result[x] ,width = 20).place(x = 240,y=150+x*29)
        c.execute('''SELECT amoute FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(bil,text = result[x] ,width = 5).place(x = 500,y=150+x*29)
        c.execute('''SELECT id FROM menulist''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(bil,text = result[x] ,width = 2).place(x = 240,y=150+x*29)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    mainloop()


frist_window()
#listmenu()
#main_window()
#bill()
#deletetable()
