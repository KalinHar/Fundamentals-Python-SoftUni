n = int(input())
balance = True
bracket = ''
for i in range(n):
    text = input()
    if text == '(' or text == ')':
        bracket += text
    if len(bracket) == 2:
        if balance and bracket == '()':
            bracket = ''
        else:
            balance = False
        bracket = ''
if balance:
    print('BALANCED')
else:
    print('UNBALANCED')
