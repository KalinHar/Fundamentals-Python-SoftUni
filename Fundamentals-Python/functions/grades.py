# grade = float(input())
#
#
# def grade_n(num):
#     if 2.00 <= num <= 2.99:
#         return "Fail"
#     elif 3.00 <= num <= 3.49:
#         return "Poor"
#     elif 3.50 <= num <= 4.49:
#         return "Good"
#     elif 4.50 <= num <= 5.49:
#         return "Very Good"
#     elif 5.50 <= num <= 6.00:
#         return "Excellent"
#
#
# print(grade_n(grade))
#
# operator = input()
# num_1 = int(input())
# num_2 = int(input())

#
# def solve(a, b, act):
#     result = None
#     if act == 'multiply':
#         result = a * b
#     elif act == 'divide':
#         result = int(a / b)
#     elif act == 'add':
#         result = a + b
#     elif act == 'subtract':
#         result = a - b
#     return result
#
#
# print(solve(num_1, num_2, operator))

w = int(input())
h = int(input())


def rect(a, b):
    return a * b


print(rect(w, h))
