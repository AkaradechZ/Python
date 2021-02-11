class pigpan:
    def __init__(self,mini,smini,normal,snormal,big,sbig):
        self.mini = mini
        self.normal = normal
        self.big = big
        self.smini = smini
        self.snormal = snormal
        self.sbig = sbig
    def present(self):
        print("-"*10,"สินค้ามีดังนี้"+"-"*10)
        print("1.",self.mini+"ราคา",self.smini+"บาท \n"+"2.",self.normal+"ราคา",self.snormal+"บาท \n"+"3.",self.big+"ราคา",self.sbig+"บาท \n")
x = pigpan("mini","59","normal","79","big","129")
#x.present()
class newpigpan(pigpan):
    def __init__(self,mini,smini,normal,snormal,big,sbig,new,snew):
        super().__init__(mini,smini,normal,snormal,big,sbig)
        self.new = new
        self.snew = snew
    def present2(self):
        print("-"*10,"สินค้ามีดังนี้"+"-"*10)
        print("1.",self.mini+"ราคา",self.smini+"บาท \n"+"2.",self.normal+"ราคา",self.snormal+"บาท \n"+"3.",self.big+"ราคา",self.sbig+"บาท \n"+"4.",self.new+"ราคา",self.snew+"บาท")
while True:
    print("*"*10,"เดชหมูกระทะ"+"*"*10)
    print("แสดงรายการสินค้า [a] \n"+"เพิ่มรายการสินค้า [b] \n"+"ออกจากระบบ [x] \n")
    menu = input("กรุณาเลือกคำสั่ง :")
    if menu == "a":
        x.present
    elif menu == "b":
        n = input(str("กรอกสินค้า :"))
        sn = input(str("ราคา : "))
        con = input(str("ต้องการเพิ่มสินค้าหรือไม่ y/n :"))
        if con == "y":
            x = newpigpan("mini","59","normal","79","big","129",n,sn)
            x.present2()
        elif con == "n":
            print ("Exit")
    elif menu == "x":
        con2 = input(str("ต้องการออกจากระบบหรือไม่ y/n :"))
        if con2 == "y":
            print("ออกจากระบบเรียบร้อยแล้ว")
            break

import os
name_list = ['ข้าวกะเพรากุ้ง','แฮมเบอร์เกอร์','ก่วยจั๊บ','สปาเกตตี้']
price_list = [60,90,40,70]
class market :
    def list_def(self):
        for x in range(0,len(name_list)):
            print(x+1,name_list[x],price_list[x],'บาท')
    def choose(self):
        print('*********ก้องเกียรติตามสั่ง*********')
        print('\tแสดงรายการสินค้า[a]\n\tเพิ่มรายการสินค้า[s]\n\tออกจากระบบ[x]')
    def input_choise(self):
        global choise
        choise = input('กรุณาเลือกคำสั่ง :\t')
    def add_list(self):
        while True:
            print('เพิ่มรายการสินค้า หากต้องการ กรอก exit')
            add_name = input('เพิ่มชื่อสินค้า :')
            if add_name == 'exit':
                break
            else : 
                add_price = input('เพิ่มราคาสินค้า :')
                name_list.append(add_name)
                price_list.append(add_price)
            add = input ('ต้องการเพิ่มสินค้าอีกหรือไม่ [y/n] :')
            if add == 'n' :
                break
            elif add == 'y' :
                os.system('cls')

while True:
    x = market()
    x.choose()
    x.input_choise()
    if choise == 'a' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        x.list_def()
    if choise == 's' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        x.add_list()
    if choise == 'x' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        close = input('ต้องการปิดโปรแกรมหรือไม่ [y/n] : ')
        if close == 'n' :
            os.system('cls')
        if close == 'y' :
            os.system('cls')
            print('ปิดโปรแกรม')
            break