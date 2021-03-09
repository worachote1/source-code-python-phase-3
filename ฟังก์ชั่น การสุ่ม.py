# สุ่มค่าตัวเลขและตัวอักษร โดยเรียกใช้ โมดูล ที่ชื่อว่า random
import random

for i in range(14):
   # x=random.random() #สุ่มในช่วง 0.0 - 1.0
    x = random.randrange(1,10) #สุ่มเป้นเลขจํานวนเต็มในชช่วง 1 - 10
    print(x)
