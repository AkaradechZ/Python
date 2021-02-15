import sqlite3 #import sqlite3
conn = sqlite3.connect(r"D:\Akaradech_Phython\newwork6.db")
c = conn.cursor() #create a cursor object 
"""c.execute ('''CREATE TABLE student(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(10) NOT NULL,
    old varchar(10) NOT NULL,
    grade varchar(10) NOt NULL)''')
conn.commit() #save (commit) the change
conn.close() #close the connecton when done"""
def inputdata():
    conn = sqlite3.connect(r"D:\Akaradech_Phython\newwork6.db")
    c = conn.cursor()
    fn = input("กรุณากรอกชื่อ :")
    ln = input("กรุณากรอกนามสกุล :")
    em = input("กรุณากรอก email :")
    se = input("กรุณากรอกเพศ :")
    ol = input("กรุณากรอกอายุ :")
    gr = input("กรุณากรอกระดับชั้น :")
    try :
        sql = '''INSERT INTO student (fname,lname,email,sex,old,grade) VALUES (?,?,?,?,?,?)'''
        data = (fn,ln,em,se,ol,gr)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print("Failed to insert : ",e)
    finally :
        if conn :
            conn.close()
    
def presentdata():
    conn = sqlite3.connect(r"D:\Akaradech_Phython\newwork6.db")
    c = conn.cursor()
    print('{0:<12}{1:<15}{2:<15}{3:<27}{4:<6}{5:<6}{6}'.format('ลำดับที่',' ชื่อ','สกุล','อีเมล','เพศ','อายุ','ชั้นปี'))
    try:
        c.execute('''SELECT * FROM student''')
        conn.commit()
        result = c.fetchall()
        for x in result:
            print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<6}{5:<6}{6}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
def changdata():
    conn = sqlite3.connect(r"D:\Akaradech_Phython\newwork6.db")
    c = conn.cursor()
    c_id = input("กรุณากรอกลำดับที่ต้องการแก้ไข :")
    c_fn = input("กรุณากรอกชื่อใหม่ :")
    c_ln = input("กรุณากรอกนามสกุลใหม่ :")
    c_em = input("กรุณากรอก email ใหม่ :")
    c_se = input("กรุณากรอกเพศใหม่ :")
    c_ol = input("กรุณากรอกอายุใหม่ :")
    c_gr = input("กรุณากรอกระดับชั้นใหม่ :")
    try:
        data = (c_fn,c_ln,c_em,c_se,c_ol,c_gr,c_id)
        c.execute('''UPDATE student SET fname =?, lname =?, email =?, sex =?, old =?, grade =? WHERE id = ?''',data)
        conn.commit()
        c.close()
        print('แก้ไขข้อมูลเรียบร้อย\n')
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn :
            conn.close()
def deletedata():
    d_fn = input("กรุณากรอกลำดับที่ต้องการลบ :")
    conn = sqlite3.connect(r"D:\Akaradech_Phython\newwork6.db")
    c = conn.cursor()
    try:
        
        c.execute("DELETE FROM student WHERE id = ?",d_fn)
        conn.commit()
        c.close
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
while True:
    print("-"*5,"ระบบทะเบียนนักเรียน","-"*5,"\n"+"="*28)
    print(" เพิ่มนักเรียน [a]\n","แสดงข้อมูล [s]\n","แก้ไขข้อมูลนักเรียน [e]\n","ลบข้อมูลนักเรียน [d]\n","ออกจากโปรแกรม [x]\n")
    ch = input("กรุณาเลือกทำรายการ :")
    if ch == "a":
        inputdata()
    if ch == "s":
        presentdata()
    if ch == "e":
        changdata()
    if ch == "d":
        deletedata()
    if ch == "x":
        ex = input("ต้องการออกจากโปรแกรมหรือไม่ y/n :")
        if ex == "y":
            print("ออกจากโปรแกรมเรียบร้อย")
            break



