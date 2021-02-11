import os
drinklist = ["coke","fanta","soda","water"]
drinkprice = [17,15,12,7]
class drink :
    def present(self):
        for i in range(0,len(drinklist)):
            print(i+1,drinklist[i],drinkprice[i],'บาท')
    def main(self):
        global ch
        print("*"*10,"เดชเครื่องดื่ม"+"*"*10)
        print("แสดงรายการสินค้า[a]\n"+"เพิ่มรายการสินค้า[s]\n"+"ออกจากระบบ[x]")
        ch = input('กรุณาเลือกคำสั่ง :')
    def addgoods(self):
        while True:
            print('เพิ่มรายการสินค้า หากต้องการ กรอก exit')
            n = input('เพิ่มชื่อสินค้า :')
            if n == 'exit':
                break
            else : 
                pn = input('เพิ่มราคาสินค้า :')
                drinklist.append(n)
                drinkprice.append(pn)
            add = input ('ต้องการเพิ่มสินค้าอีกหรือไม่ [y/n] :')
            if add == 'n' :
                break
            elif add == 'y' :
                os.system('cls')

while True:
    x = drink()
    x.main()
    if ch == 'a' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',ch)
        x.present()
    if ch == 's' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',ch)
        x.addgoods()
    if ch == 'x' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',ch)
        ex = input('ต้องการปิดโปรแกรมหรือไม่ [y/n] : ')
        if ex == 'n' :
            os.system('cls')
        if ex == 'y' :
            os.system('cls')
            print('ปิดโปรแกรม')
            break

