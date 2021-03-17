import re

tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    left_side = ticket[:10]
    right_side = ticket[10:]
    imp = r"\$\$\$\$\$\$+|\^\^\^\^\^\^+|@@@@@@+|######+"
    # win = r"[\^]{6,10}|[\$]{6,10}|[\@]{6,10}|[\#]{6,10}"
    # jackpot = r"[\^]{20}|[\$]{20}|[\@]{20}|[\#]{20}"
    left = re.findall(imp, left_side)
    right = re.findall(imp, right_side)
    if left and right:
        if left[0] in right[0] or right[0] in left[0]:
            jack = ""
            if len(left[0]) == len(right[0]) == 10:
                jack += " Jackpot!"
            if len(left[0]) > len(right[0]):
                length = len(right[0])
            else:
                length = len(left[0])
            print(f'ticket "{ticket}" - {length}{left[0][0]}{jack}')
            continue
    print(f'ticket "{ticket}" - no match')

