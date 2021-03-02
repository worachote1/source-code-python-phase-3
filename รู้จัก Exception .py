# รู้จัก Exception
# เมื่อเกิดข้อผิดพลาดขึ้นแล้ว ทําให้โปรแกรมหยุดทํางาน ต้องมีการใช้ Exception เพื่อบอกผู้ใช้งานว่าเค้าต้องทําอย่างไรให้ถูกต้อง ขณะที่โปรแกรมยังทํางานได้อยู่

# Exception

# number1=int(input("ป้อนตัวเลขที่ 1 :"))
# number2=int(input("ป้อนตัวเลขที่ 2 :"))
# result=number1/number2
# print(result)

# ** กุเพิ่งรู้ว่าวิธี comment # ให้ได้หลายๆบรรทัดคือ ลากคลุม แล้วกด crtl ค้างไว้ จากนั้นกด / (ที่อยู่ข้างๆshiftด้านขวา)

'''
โครงสร้าง try except

try :
    คําสั่งรันโปรแกรมปกติ
except :
    คําสั่งที่ทํางานตอนโปรแกรมมีข้อผิดพลาด(ตอนที่คําสั่งใน try มีข้อผิดพลาดนั่นแหละ)

'''
# ValueError => ค่าผิดพลาด
# ZEroDivisionError => หารด้วยส่วนเป็น ศูนย์ ไม่ได้
'''
try:
       number1 = int(input("ป้อนตัวเลข 1 :"))
       number2 = int(input("ป้อนตัวเลข 2 :"))
       result = number1/number2
       print(result)
except ValueError:
        print("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
except ZeroDivisionError:
        print("ห้ามหารด้วยเลขศูนย์นะครับ")
finally:  # ลอง run ดูก่อนว่าโปรแกรมของเราทํางานได้ไหม ถ้ามี error เกิดขึ้นให้แสดงผลออกมา แต่ส่วนใดทํางานได้อยู่ก็ให้ทํางานใน block ของ finally
        print("ทํางานต่อไป......")

# else: # คําสั่งใน else จะทํางานเมื่อไม่พบปัญหาในการ run โปรแกรม
#   print("จบโปรแกรมครับ")

'''

# try exception ทํางานร่วมกับ loop while
while True :
    try:
       name = input("ป้อนชื่อผู้ใช้ :")
       if name == "ก้อง":
            raise Exception("มีชื่อผู้ใช้นี้ในระบบแล้วครับ !! กรุณาใช้ชื่อใหม่")
       
       number1 = int(input("ป้อนตัวเลข 1 :"))
       number2 = int(input("ป้อนตัวเลข 2 :"))
       if number1 == 0 and number2 == 0 :
           break
        #กําหนดเหตุการณ์ให้โปรแกรมแสดงข้อผิดพลาดได้เอง โดยใช้ raise
       if number1 < 0 or number2 < 0 :
            raise Exception("ไม่สามารถป้อนค่าติดลบได้นะครับย")
       
       result = number1/number2
       print(result)
    except Exception as e :
        print(e)   
    except ValueError:
        print("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
    except ZeroDivisionError:
        print("ห้ามหารด้วยเลขศูนย์นะครับ")
    finally:  # ลอง run ดูก่อนว่าโปรแกรมของเราทํางานได้ไหม ถ้ามี error เกิดขึ้นให้แสดงผลออกมา แต่ส่วนใดทํางานได้อยู่ก็ให้ทํางานใน block ของ finally
        print("ทํางานต่อไป......")

        