b = int(input("Choos Menu 1 or 2 :"))
if b == 1:
    s = int(input("Enter distand of way :"))
    print("Menu 1 เหมาจ่าย")
    if s <= 25:
        print("value = 25")
    elif s > 25:
        print("value = 55")
if b == 2:
    s = int(input("Enter distand of way :"))
    print("Menu 2 จ่ายเพิ่ม")
    if s <= 25:
        print("value = 25")
    elif s > 25: 
        print("value = 80") 