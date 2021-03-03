#โปรแกรมบัญชีธนาคาร

# data ของลูกค้า เก็บเป็น Dictionary
account={"นายA":5000,"นายB":0}

def getBalance():
    print("มีเงินคงเหลือในบัญชี :",account)

def deposit(money):
    if money < 0 :
        raise Exception("เงินฝากต้องมากกว่า 0 เท่านั่น !!")
    
    print("ฝากเงินเข้าบัญชี A :",money)
    account["นายA"] += money

def withdraw(money):
    if money < 0 :
        raise Exception("เงินที่่ถอนต้องมากกว่า 0 เท่านั้น !!" )
    if money >= account["นายA"]:
        raise Exception("ไม่สามารถถอนเงินได้ เนื่องจากเงินฝากของท่านน้อยกว่าเงินที่ต้องการถอน")
    print("ถอนเงินจากบัญชี A :",money)
    account["นายA"] -= money

def transfer(money):
    if money < 0 :
        raise Exception("เงินที่่โอนต้องมากกว่า 0 เท่านั้น !!" )
    if money >= account["นายA"]:
        raise Exception("ไม่สามารถโอนเงินได้ เนื่องจากยอดเงินในบัญชีของท่านไม่พอ") #เพราะมีเงินฝากน้อยกว่าเงินที่จะโอน
    print("ทําการโอนเงินไปที่บัญชี B :",money)
    account["นายB"] += money
    account["นายA"] -= money



try:
    #withdraw(-500)
    getBalance()
    transfer(1000000)
    getBalance()

except Exception as e:
    print(e)    #ได้ output คือ เงินที่ถอนต้องมากกว่า 0 เท่านั้น !!