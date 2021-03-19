from tkinter import *
from tkinter import messagebox
import sys
import sqlite3
'''
conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
c = conn.cursor()
c.execute("""CREATE TABLE menutable4 (id integer PRIMARY KEY AUTOINCREMENT,
    Menu varchar(100) NOT NULL,
    Price varchar(30) NOT NULL)""")
conn.commit()
conn.close()
'''
amoute1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
amoute2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
amoute3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
amoute4 = [0,0,0,0,0,0,0,0,0,0,0,0,0]

def billtable1():
    chb = Tk()
    chb.title("ใบเสร็จ")
    chb.option_add("*font","impact 15")
    Label(chb,text = "รวมรายการที่สั่งทั้งหมด").pack(fill = X)
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu,Price FROM menutable1''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(chb,text = result[x] ,bg = "#CD853F",height = 2,width = 10).pack(fill = X)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    summ = amoute1[1]*60 + amoute1[2]*60 + amoute1[3]*40 + amoute1[4]*60 + amoute1[5]*60 + amoute1[6]*50 + amoute1[7]*50 + amoute1[8]*50 + amoute1[9]*60 + amoute1[10]*10 + amoute1[11]*15 + amoute1[12]*70
    Label(chb,text = "ราคารวม :").pack(side = LEFT)
    Label(chb,text = summ).pack(side = RIGHT)
    chb.mainloop()
def billtable2():
    chb = Tk()
    chb.title("ใบเสร็จ")
    chb.option_add("*font","impact 15")
    Label(chb,text = "รวมรายการที่สั่งทั้งหมด").pack(fill = X)
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu,Price FROM menutable2''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(chb,text = result[x] ,bg = "#CD853F",height = 2,width = 10).pack(fill = X)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    summ = amoute2[1]*60 + amoute2[2]*60 + amoute2[3]*40 + amoute2[4]*60 + amoute2[5]*60 + amoute2[6]*50 + amoute2[7]*50 + amoute2[8]*50 + amoute2[9]*60 + amoute2[10]*10 + amoute2[11]*15 + amoute2[12]*70
    Label(chb,text = "ราคารวม :").pack(side = LEFT)
    Label(chb,text = summ).pack(side = RIGHT)
    chb.mainloop()
def billtable3():
    chb = Tk()
    chb.title("ใบเสร็จ")
    chb.option_add("*font","impact 15")
    Label(chb,text = "รวมรายการที่สั่งทั้งหมด").pack(fill = X)
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu,Price FROM menutable3''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(chb,text = result[x] ,bg = "#CD853F",height = 2,width = 10).pack(fill = X)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    summ = amoute3[1]*60 + amoute3[2]*60 + amoute3[3]*40 + amoute3[4]*60 + amoute3[5]*60 + amoute3[6]*50 + amoute3[7]*50 + amoute3[8]*50 + amoute3[9]*60 + amoute3[10]*10 + amoute3[11]*15 + amoute3[12]*70
    Label(chb,text = "ราคารวม :").pack(side = LEFT)
    Label(chb,text = summ).pack(side = RIGHT)
    chb.mainloop()
def billtable4():
    chb = Tk()
    chb.title("ใบเสร็จ")
    chb.option_add("*font","impact 15")
    Label(chb,text = "รวมรายการที่สั่งทั้งหมด").pack(fill = X)
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try:
        c.execute('''SELECT Menu,Price FROM menutable4''')
        conn.commit()
        result = c.fetchall()
        for x in range(0,len(result)):
            Label(chb,text = result[x] ,bg = "#CD853F",height = 2,width = 10).pack(fill = X)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    summ = amoute4[1]*60 + amoute4[2]*60 + amoute4[3]*40 + amoute4[4]*60 + amoute4[5]*60 + amoute4[6]*50 + amoute4[7]*50 + amoute4[8]*50 + amoute4[9]*60 + amoute4[10]*10 + amoute4[11]*15 + amoute4[12]*70
    Label(chb,text = "ราคารวม :").pack(side = LEFT)
    Label(chb,text = summ).pack(side = RIGHT)
    chb.mainloop()

def check1():
    
    ch = messagebox.askyesno(title="ยืนยันรายการ",message="ท่านต้องการยืนยันรายการหรือไม่")
    if ch == 0:
        sys.exit()
    if ch > 0:
        ch = messagebox.showinfo(title="เรียยบร้อย",message = "ยืนยันราบการเรียบร้อย กรุณารออาหารสักครู่ ผักและนำ้แข็งฟรีโปรดบริการตนเอง")

def table1():
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        c.execute('DELETE FROM menutable1')
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    tb1 = Tk()
    tb1.title("โต๊ะ 1")
    tb1.option_add("*font","impact 15")
    Label(tb1,text = "โต๊ะ 1",bg = "#CD853F",height = 2).pack(fill = X)
    Label(tb1,text = "กรุณาเลือกเมนูอาหารและเครื่องดื่ม",bg = "#F5DEB3",wraplength=400,height = 2).pack(fill = X)
    menu1 = Button(tb1,text = "1.ลาบเนื้อดิบ....60.บาท",command = menu1teble1).pack(pady = 2,side = TOP,fill = X)
    menu2 = Button(tb1,text = "2.ลาบเนื้อสุก....60.บาท",command = menu2teble1).pack(pady = 2,side = TOP,fill = X)
    menu3 = Button(tb1,text = "3.ลาบหมูสุก.....40.บาท",command = menu3teble1).pack(pady = 2,side = TOP,fill = X)
    menu4 = Button(tb1,text = "4.ก้อยเนื้อดิบ....60.บาท",command = menu4teble1).pack(pady = 2,side = TOP,fill = X)
    menu5 = Button(tb1,text = "5.ก้อยเนื้อสุก....60.บาท",command = menu5teble1).pack(pady = 2,side = TOP,fill = X)
    menu6 = Button(tb1,text = "6.ต้มแซ่บ.........50.บาท",command = menu6teble1).pack(pady = 2,side = TOP,fill = X)
    menu7 = Button(tb1,text = "7.ต้มขม...........50.บาท",command = menu7teble1).pack(pady = 2,side = TOP,fill = X)
    menu8 = Button(tb1,text = "8.อ่อมเนื้อ.......50.บาท",command = menu8teble1).pack(pady = 2,side = TOP,fill = X)
    menu9 = Button(tb1,text = "9.คอหมูย่าง.....60.บาท",command = menu9teble1).pack(pady = 2,side = TOP,fill = X)
    menu10 = Button(tb1,text = "10.ข้าวเหนียว....10.บาท",command = menu10teble1).pack(pady = 2,side = TOP,fill = X)
    menu11 = Button(tb1,text = "11.น้ำอัดลม......15.บาท",command = menu11teble1).pack(pady = 2,side = TOP,fill = X)
    menu12 = Button(tb1,text = "12.เบียร์.........70.บาท",command = menu12teble1).pack(pady = 2,side = TOP,fill = X)
    Button(tb1,text = "ยืนยันรายการ",bg = "#00FA9A",command = check1).pack(pady = 2,side = BOTTOM)
    tb1.mainloop()
def table2():
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        c.execute('DELETE FROM menutable2')
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    tb1 = Tk()
    tb1.title("โต๊ะ 2")
    tb1.option_add("*font","impact 15")
    Label(tb1,text = "โต๊ะ 2",bg = "#CD853F",height = 2).pack(fill = X)
    Label(tb1,text = "กรุณาเลือกเมนูอาหารและเครื่องดื่ม",bg = "#F5DEB3",wraplength=400,height = 2).pack(fill = X)
    menu1 = Button(tb1,text = "1.ลาบเนื้อดิบ....60.บาท",command = menu1teble2).pack(pady = 2,side = TOP,fill = X)
    menu2 = Button(tb1,text = "2.ลาบเนื้อสุก....60.บาท",command = menu2teble2).pack(pady = 2,side = TOP,fill = X)
    menu3 = Button(tb1,text = "3.ลาบหมูสุก.....40.บาท",command = menu3teble2).pack(pady = 2,side = TOP,fill = X)
    menu4 = Button(tb1,text = "4.ก้อยเนื้อดิบ....60.บาท",command = menu4teble2).pack(pady = 2,side = TOP,fill = X)
    menu5 = Button(tb1,text = "5.ก้อยเนื้อสุก....60.บาท",command = menu5teble2).pack(pady = 2,side = TOP,fill = X)
    menu6 = Button(tb1,text = "6.ต้มแซ่บ.........50.บาท",command = menu6teble2).pack(pady = 2,side = TOP,fill = X)
    menu7 = Button(tb1,text = "7.ต้มขม...........50.บาท",command = menu7teble2).pack(pady = 2,side = TOP,fill = X)
    menu8 = Button(tb1,text = "8.อ่อมเนื้อ.......50.บาท",command = menu8teble2).pack(pady = 2,side = TOP,fill = X)
    menu9 = Button(tb1,text = "9.คอหมูย่าง.....60.บาท",command = menu9teble2).pack(pady = 2,side = TOP,fill = X)
    menu10 = Button(tb1,text = "10.ข้าวเหนียว....10.บาท",command = menu10teble2).pack(pady = 2,side = TOP,fill = X)
    menu11 = Button(tb1,text = "11.น้ำอัดลม......15.บาท",command = menu11teble2).pack(pady = 2,side = TOP,fill = X)
    menu12 = Button(tb1,text = "12.เบียร์.........70.บาท",command = menu12teble2).pack(pady = 2,side = TOP,fill = X)
    Button(tb1,text = "ยืนยันรายการ",bg = "#00FA9A",command = check1).pack(pady = 2,side = BOTTOM)
    tb1.mainloop()
def table3():
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        c.execute('DELETE FROM menutable3')
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    tb1 = Tk()
    tb1.title("โต๊ะ 3")
    tb1.option_add("*font","impact 15")
    Label(tb1,text = "โต๊ะ 3",bg = "#CD853F",height = 2).pack(fill = X)
    Label(tb1,text = "กรุณาเลือกเมนูอาหารและเครื่องดื่ม",bg = "#F5DEB3",wraplength=400,height = 2).pack(fill = X)
    menu1 = Button(tb1,text = "1.ลาบเนื้อดิบ....60.บาท",command = menu1teble3).pack(pady = 2,side = TOP,fill = X)
    menu2 = Button(tb1,text = "2.ลาบเนื้อสุก....60.บาท",command = menu2teble3).pack(pady = 2,side = TOP,fill = X)
    menu3 = Button(tb1,text = "3.ลาบหมูสุก.....40.บาท",command = menu3teble3).pack(pady = 2,side = TOP,fill = X)
    menu4 = Button(tb1,text = "4.ก้อยเนื้อดิบ....60.บาท",command = menu4teble3).pack(pady = 2,side = TOP,fill = X)
    menu5 = Button(tb1,text = "5.ก้อยเนื้อสุก....60.บาท",command = menu5teble3).pack(pady = 2,side = TOP,fill = X)
    menu6 = Button(tb1,text = "6.ต้มแซ่บ.........50.บาท",command = menu6teble3).pack(pady = 2,side = TOP,fill = X)
    menu7 = Button(tb1,text = "7.ต้มขม...........50.บาท",command = menu7teble3).pack(pady = 2,side = TOP,fill = X)
    menu8 = Button(tb1,text = "8.อ่อมเนื้อ.......50.บาท",command = menu8teble3).pack(pady = 2,side = TOP,fill = X)
    menu9 = Button(tb1,text = "9.คอหมูย่าง.....60.บาท",command = menu9teble3).pack(pady = 2,side = TOP,fill = X)
    menu10 = Button(tb1,text = "10.ข้าวเหนียว....10.บาท",command = menu10teble3).pack(pady = 2,side = TOP,fill = X)
    menu11 = Button(tb1,text = "11.น้ำอัดลม......15.บาท",command = menu11teble3).pack(pady = 2,side = TOP,fill = X)
    menu12 = Button(tb1,text = "12.เบียร์.........70.บาท",command = menu12teble3).pack(pady = 2,side = TOP,fill = X)
    Button(tb1,text = "ยืนยันรายการ",bg = "#00FA9A",command = check1).pack(pady = 2,side = BOTTOM)
    tb1.mainloop()
def table4():
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        c.execute('DELETE FROM menutable4')
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    tb1 = Tk()
    tb1.title("โต๊ะ 4")
    tb1.option_add("*font","impact 15")
    Label(tb1,text = "โต๊ะ 4",bg = "#CD853F",height = 2).pack(fill = X)
    Label(tb1,text = "กรุณาเลือกเมนูอาหารและเครื่องดื่ม",bg = "#F5DEB3",wraplength=400,height = 2).pack(fill = X)
    menu1 = Button(tb1,text = "1.ลาบเนื้อดิบ....60.บาท",command = menu1teble4).pack(pady = 2,side = TOP,fill = X)
    menu2 = Button(tb1,text = "2.ลาบเนื้อสุก....60.บาท",command = menu2teble4).pack(pady = 2,side = TOP,fill = X)
    menu3 = Button(tb1,text = "3.ลาบหมูสุก.....40.บาท",command = menu3teble4).pack(pady = 2,side = TOP,fill = X)
    menu4 = Button(tb1,text = "4.ก้อยเนื้อดิบ....60.บาท",command = menu4teble4).pack(pady = 2,side = TOP,fill = X)
    menu5 = Button(tb1,text = "5.ก้อยเนื้อสุก....60.บาท",command = menu5teble4).pack(pady = 2,side = TOP,fill = X)
    menu6 = Button(tb1,text = "6.ต้มแซ่บ.........50.บาท",command = menu6teble4).pack(pady = 2,side = TOP,fill = X)
    menu7 = Button(tb1,text = "7.ต้มขม...........50.บาท",command = menu7teble4).pack(pady = 2,side = TOP,fill = X)
    menu8 = Button(tb1,text = "8.อ่อมเนื้อ.......50.บาท",command = menu8teble4).pack(pady = 2,side = TOP,fill = X)
    menu9 = Button(tb1,text = "9.คอหมูย่าง.....60.บาท",command = menu9teble4).pack(pady = 2,side = TOP,fill = X)
    menu10 = Button(tb1,text = "10.ข้าวเหนียว....10.บาท",command = menu10teble4).pack(pady = 2,side = TOP,fill = X)
    menu11 = Button(tb1,text = "11.น้ำอัดลม......15.บาท",command = menu11teble4).pack(pady = 2,side = TOP,fill = X)
    menu12 = Button(tb1,text = "12.เบียร์.........70.บาท",command = menu12teble4).pack(pady = 2,side = TOP,fill = X)
    Button(tb1,text = "ยืนยันรายการ",bg = "#00FA9A",command = check1).pack(pady = 2,side = BOTTOM)
    tb1.mainloop()

def menu1teble1():#1.ลาบเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[1] += 1
def menu2teble1():#2.ลาบเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[2] += 1
def menu3teble1():#3.ลาบหมูสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบหมูสุก","40")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[3] += 1
def menu4teble1():#4.ก้อยเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[4] += 1
def menu5teble1():#5.ก้อยเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[5] += 1
def menu6teble1():#6.ต้มแซ่บ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มแซ่บ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[6] += 1
def menu7teble1():#7.ต้มขม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มขม","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute[7] += 1
def menu8teble1():#8.อ่อมเนื้อ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("อ่อมเนื้อ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[8] += 1
def menu9teble1():#9.คอหมูย่าง
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("คอหมูย่าง","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[9] += 1
def menu10teble1():#10.ข้าวเหนียว
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("ข้าวเหนียว","10")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[10] += 1
def menu11teble1():#11.นำ้อัดลม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("น้ำอัดลม","15")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[11] += 1
def menu12teble1():#12.เบียร์
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable1 (Menu,Price) VALUES (?,?)'''
        data = ("เบียร์","70")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute1[12] += 1

def menu1teble2():#1.ลาบเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[1] += 1
def menu2teble2():#2.ลาบเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[2] += 1
def menu3teble2():#3.ลาบหมูสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบหมูสุก","40")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[3] += 1
def menu4teble2():#4.ก้อยเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[4] += 1
def menu5teble2():#5.ก้อยเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[5] += 1
def menu6teble2():#6.ต้มแซ่บ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มแซ่บ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[6] += 1
def menu7teble2():#7.ต้มขม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มขม","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[7] += 1
def menu8teble2():#8.อ่อมเนื้อ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("อ่อมเนื้อ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[8] += 1
def menu9teble2():#9.คอหมูย่าง
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("คอหมูย่าง","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[9] += 1
def menu10teble2():#10.ข้าวเหนียว
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("ข้าวเหนียว","10")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[10] += 1
def menu11teble2():#11.นำ้อัดลม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("น้ำอัดลม","15")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[11] += 1
def menu12teble2():#12.เบียร์
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable2 (Menu,Price) VALUES (?,?)'''
        data = ("เบียร์","70")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute2[12] += 1

def menu1teble3():#1.ลาบเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[1] += 1
def menu2teble3():#2.ลาบเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[2] += 1
def menu3teble3():#3.ลาบหมูสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบหมูสุก","40")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[3] += 1
def menu4teble3():#4.ก้อยเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[4] += 1
def menu5teble3():#5.ก้อยเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[5] += 1
def menu6teble3():#6.ต้มแซ่บ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มแซ่บ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[6] += 1
def menu7teble3():#7.ต้มขม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มขม","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[7] += 1
def menu8teble3():#8.อ่อมเนื้อ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("อ่อมเนื้อ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[8] += 1
def menu9teble3():#9.คอหมูย่าง
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("คอหมูย่าง","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[9] += 1
def menu10teble3():#10.ข้าวเหนียว
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("ข้าวเหนียว","10")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[10] += 1
def menu11teble3():#11.นำ้อัดลม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("น้ำอัดลม","15")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[11] += 1
def menu12teble3():#12.เบียร์
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable3 (Menu,Price) VALUES (?,?)'''
        data = ("เบียร์","70")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute3[12] += 1

def menu1teble4():#1.ลาบเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[1] += 1
def menu2teble4():#2.ลาบเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[2] += 1
def menu3teble4():#3.ลาบหมูสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ลาบหมูสุก","40")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[3] += 1
def menu4teble4():#4.ก้อยเนื้อดิบ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อดิบ","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[4] += 1
def menu5teble4():#5.ก้อยเนื้อสุก
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ก้อยเนื้อสุก","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[5] += 1
def menu6teble4():#6.ต้มแซ่บ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มแซ่บ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[6] += 1
def menu7teble4():#7.ต้มขม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ต้มขม","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[7] += 1
def menu8teble4():#8.อ่อมเนื้อ
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("อ่อมเนื้อ","50")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[8] += 1
def menu9teble4():#9.คอหมูย่าง
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("คอหมูย่าง","60")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[9] += 1
def menu10teble4():#10.ข้าวเหนียว
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("ข้าวเหนียว","10")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[10] += 1
def menu11teble4():#11.นำ้อัดลม
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("น้ำอัดลม","15")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[11] += 1
def menu12teble4():#12.เบียร์
    conn = sqlite3.connect(r"D:\Akaradech_Python\pythonproject1.db")
    c = conn.cursor()
    try :
        sql = '''INSERT INTO menutable4 (Menu,Price) VALUES (?,?)'''
        data = ("เบียร์","70")
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    amoute4[12] += 1

def mainwindow():
    window = Tk()
    window.title("หน้าหลัก")
    window.option_add("*font","impact 20")
    frame1 = Frame(master=window, width=50, height=100, bg="#CD5C5C")
    frame1.pack(fill= Y, side= LEFT)
    frame2 = Frame(master=window, width=50, height=100, bg="#CD5C5C")
    frame2.pack(fill= Y, side= RIGHT)
    Label(window,text = "ร้าน ท.เทศบาลการลาบ",bg = "#CD853F",height = 2).pack(fill = X)
    Label(window,text = "ร้าน ท.เทศบาลการลาบ ยินดีต้อนรับ กรุณาเลือกโต๊ะที่ต้องการ",bg = "#F5DEB3",wraplength=400,height = 2).pack(fill = X)
    Button(window,text = "โต๊ะ 1",bg = "#FFA07A",command = table1).pack(fill = X)
    Button(window,text = "โต๊ะ 2",bg = "#FFA07A",command = table2).pack(fill = X)
    Button(window,text = "โต๊ะ 3",bg = "#FFA07A",command = table3).pack(fill = X)
    Button(window,text = "โต๊ะ 4",bg = "#FFA07A",command = table4).pack(fill = X)
    menubar = Menu(window)
    filemenu = Menu(menubar,tearoff = 0)
    filemenu.add_command(label = "ใบเสร็จโต๊ะ 1",command = billtable1)
    filemenu.add_command(label = "ใบเสร็จโต๊ะ 2",command = billtable2)
    filemenu.add_command(label = "ใบเสร็จโต๊ะ 3",command = billtable3)
    filemenu.add_command(label = "ใบเสร็จโต๊ะ 4",command = billtable4)
    menubar.add_cascade(label = "ใบเสร็จ",menu = filemenu)
    window.config(menu = menubar)
    window.mainloop()
mainwindow()