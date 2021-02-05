print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
i = 1
x = []
p = 0
while(True):
    a = str(input("อาหารโปรดลำดับที่" +str(i)+ "ของคุณคือ "))
    if (a == "exit"):
        break
    x.append(a)
    i += 1
print("อาหารสุดโปรดของคุณมีดังนี้ " ,end="" )
while(True):
    print(str(p+1)+".",x[p]+" ",end="" )
    p += 1