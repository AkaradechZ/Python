word = {}
def insertword():
    a = input("กรุณากรอกคำศัพท์ : ")
    b = input("ชนิดคำศัพท์(n. , v. , adj. , :) : ")
    c = input("กรุณากรอกความหมาย : ")
    word[a] = b,c
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว")

def presentword():
    print("---------------------------")
    print("      คำศัพท์ทีมีทั้งหมด       ")
    print("---------------------------")
    print("คำศัพท์  ประเภท  ความหมาย")
    for key in word:
        print("{1}{0:<6}{2}".format(key,".",word[key]))

def deleteword():
    da = input("กรุณากรอกคำศัพท์ที่ต้องการลบ : ")
    yn = input("ต้องการลบ"+da+"ใช่หรือไม่ y/n : ")
    if yn == 'y':
        del word[da]
        print("ลบ"+da+"เรียบร้อยแล้ว")

def closeprogram():
    ch2 = input("ต้องการที่จะออกจากโปรแกรมใช่หรือไม่ y/n : ")
    if ch2 == "y":
        print("ออกจากโปรแกรมเรียบร้อยแล้ว")

while True:
    print("พจนานุกรม")
    print("1) เพิ่มคำศัพท์ \n2) แสดงคำศัพท์ \n3) ลบคำศัพท์ \n4) ออกจากโปรแกรม")
    choice = input("เลือกรายการที่ต้องการ : ")
    if choice == '1':
        insertword()
    elif choice == '2':
        presentword()
    elif choice == '3':
        deleteword()
    elif choice == '4':
         closeprogram()
         break
