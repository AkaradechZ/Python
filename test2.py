'''import os
choice = 0
filename = ''

def menu():
    global choice
    print("Menu\n 1.Open Calculater\n 2.Open notepad\n 3.Exit")
    choice = input("Select Menu : ")

def opennotepad():
    filename = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\ notepad.exe'
    print('Memorandum writing %s' %filename)
    os.sytem(filename)

def opencalculater():
    filename = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\ notepad.exe' 
    print('Calculater Number %s' %filename
    os.sytem(filename)

while True:
    menu()
    if choice == '1':
        opencalculater()
    elif choice == '2':
        opennotepad()
    else:
        break'''
'''
def Introduce(arg1,arg2 = 'com',arg3 = 'ed',arg4 = 'kku'):
    print("Hello, I am"+arg1+","+arg2+" "+arg3+" "+arg4)

Introduce("Python")
Introduce(arg1 = "Python")
Introduce(arg1 = "Python",arg3 = "Sci")
Introduce("Python",arg4 = "CMU")
'''
import datetime
date = datetime.datetime.now()
d1 = date.strftime("%d %B %Y,%H : %M : %S",date)
print(d1)