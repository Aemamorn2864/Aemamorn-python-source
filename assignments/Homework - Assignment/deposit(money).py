# Assignment-3

balance = 1000.0


def deposit(money):
    """รับจำนวนเงินฝากและคืนยอดเงินคงเหลือใหม่"""
    if money <= 0:
        raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    return balance + money


try:
    money = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
    new_balance = deposit(money)
except ValueError as e:
    print(f"เกิดข้อผิดพลาด: {e}")
else:
    print(f"ฝากเงินสำเร็จ")
    print(f"ยอดเงินคงเหลือ: {new_balance:.2f} บาท")
finally:
    print("สิ้นสุดรายการฝากเงิน")