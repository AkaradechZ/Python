goods = [0,0,0,0,0]
sinkha = []
raka = [10,17,15,7,20]
i = 0
def showgoods():
    print("1.Milk  Price  10 Bath")
    print("2.Coke  Price  17 Bath")
    print("3.Fanta price  15 Bath")
    print("4.Water Price   7 Bath")
    print("5.Coco  Price  20 Bath")
def choosgoods():
    while True:
        a = input("เลือกหมายเลขสินค้าใส่ตระกร้า :")
        if a == '1':
            sinkha.append("Milk")
        elif a == '2':
            sinkha.append("Coke")
        elif a == '3':
            sinkha.append("Fanta")
        elif a == '4':
            sinkha.append("Water")
        elif a == '5':
            sinkha.append("Coco")
        elif a == 'exit':
            break

def present():
    for i in sinkha:
        if i == "Milk":
            goods[0]+=1
        elif i == "Coke":
            goods[1]+=1
        elif i == "Fanta":
            goods[2]+=1
        elif i == "Water":
            goods[3]+=1
        elif i == "Coco":
            goods[4]+=1
    rgoods = goods[0]+goods[1]+goods[2]+goods[3]+goods[4]
    rakarum = goods[0]*10 + goods[1]*17 + goods[2]*15 + goods[3]*7 + goods[4]*20
    print("")
    print("{0:_<10}{1}{0:_<10}".format("","สินค้าที่คุณได้เลือกมามีดังนี้"))
    print("{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}".format("","สินค้า","จำนวน","ราคา"))
    print("{0:_<38}".format(""))
    if goods[0]!=0:
        print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","Milk",str(goods[0]),str(goods[0]*10)))
    if goods[1]!=0:
        print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","Coke",str(goods[1]),str(goods[1]*17)))
    if goods[2]!=0:
        print("{0:.<6}{1}{0:.<5}{2}{0:.<9}{3}{0:.<10}".format("","Fanta",str(goods[2]),str(goods[2]*10)))
    if goods[3]!=0:
        print("{0:.<6}{1}{0:.<5}{2}{0:.<9}{3}{0:.<10}".format("","Water",str(goods[3]),str(goods[3]*10)))
    if goods[4]!=0:
        print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","Coco",str(goods[4]),str(goods[4]*17)))
    print("{0:_<38}".format(""))
    print("{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}".format("","Total",str(rgoods),str(rakarum)))

def Exit():
    print("Exit Program")
while True:
    print("     โปรแกรมร้านค้าออนไลน์     ")
    print("----------------------------")
    print("1.แสดงสินค้า\n2.หยิบสินค้าเข้าตระกร้า\n3.แสดงสินค้าที่เลือก\n4.ปิดโปรแกรม\n")
    b = int(input("กรุณาเลือกรายการ :"))
    if b == 1:
        showgoods()
    elif b == 2:
        choosgoods()
    elif b == 3:
        present()
    elif b == 4:
        Exit()
        break




