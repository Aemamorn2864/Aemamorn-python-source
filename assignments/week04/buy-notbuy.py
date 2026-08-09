# Assignment 2.2: โปรแกรมช่วยตัดสินใจเลือกซื้อสินค้าภายใต้งบประมาณรวม

prices = []

print("Enter prices of 6  items: ")

#รับราคาสินค้า
for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))

total = 0
bought_items = []

#ตรวจสอบสินค้า
for i in range(6):
    if total + prices[i] <= budget:
        total = total + prices[i]
        bought_items.append(prices[i])
        print(f"\nItem {i + 1} = {prices[i]} -> buy")
    else:
        print(f"\nItem {i + 1} =  {prices[i]} -> cannot buy")
    print(f"Current total = {total}")

print(f"\nBought items: {bought_items}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")