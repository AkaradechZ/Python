a = int(input("จำนวนนักเรียน : "))
i = b1 = b2 = b3 = b4 = b5 = b6 = 0
while(i < a):
    b = int(input("กรุณากรอกคะแนน : "))
    if 0 <= b <=49 :
        b1 += 1
    elif 50 <= b <= 59:
        b2 += 1
    elif 60 <= b <= 69:
        b3 += 1
    elif 70 <= b <= 79:
        b4 += 1
    elif 80 <= b <= 89:
        b5 += 1
    elif 90 <= b <= 100:
        b6 += 1
    i += 1
print("90-100 : ","*"*b6)
print("80-89 : ","*"*b5)
print("70-79 : ","*"*b4)
print("60-69 : ","*"*b3)
print("50-59 : ","*"*b2)
print("0-49 : ","*"*b1)
