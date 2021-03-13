import re
n = int(input())
pattern = r"@#+[A-Z]\B[a-z0-9A-Z]{4,}\B[A-Z]+@#+"
for _ in range(n):
    barcode = input()
    result = re.findall(pattern, barcode)
    if not result:
        print("Invalid barcode")
        continue
    prod_group = ""
    for s in result[0]:
        if s.isdigit():
            prod_group += s
    if not prod_group:
        prod_group = "00"
    print(f"Product group: {prod_group}")
