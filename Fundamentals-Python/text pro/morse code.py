
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..'}

inv_dict = {v: k for k, v in MORSE_CODE_DICT.items()}

words = input().split(" | ")
result = ""
for w in words:
    w = w.split()
    word =""
    for s in w:
        word += inv_dict[s]
    result += word + ' '
print(result)
