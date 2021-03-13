from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
eggs_price = float(input())
apron_price = float(input())

apron_price *= ceil(students * 1.2)
eggs_price *= students * 10
free_pack_flour = students // 5
flour_price *= (students - free_pack_flour)
total = apron_price + eggs_price + flour_price
if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    print((f"{total - budget:.2f}$ more needed."))
