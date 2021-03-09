x=min(3,4,5,-10,30,40)
print(x)

y=max(3,4,5,-10,30,40)
print(y)

p=pow(5,2) # 5 ยกกําลัง 2

# อยากหาค่า root ต้อง import จาก โมดูล ที่ชื่อ math

import math

result=math.sqrt(25) # หารากที่ 2 ของ 25
print(result)


# การปัดเศษลงใช้ floor ส่วนการปัดเศษขึ้นใช้ ceil

score = 80.4

print("ปัดเลข 80.4 ลงได้ = ",math.floor(score))
print("ปัดเลข 80.4 ขึ้นได้ = ",math.ceil(score))
