my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])    # Output: Jack
print(my_dict.get('age')) # Output: 26
# my_dict.get('address') -> None
# my_dict['address']     -> KeyError
my_dict['age'] = 27
print(my_dict['age'])   # 27

elements = input().split(" ")
bakery = {}  # bakery = dict()
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
print(bakery)

squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
   squares[key] *= 2
print(squares)  # {1: 2, 2: 8, 3: 18}
k = squares.keys()
v = squares.values()
print(k)  # dict_keys([1, 2, 3])
print(v)  # dict_values([2, 8, 18])

second_dict = my_dict.copy()  # {'name':'Jack', 'age': 27}
last = second_dict.popitem()  # 27 - premahva poslednia element
print(second_dict)  # {'name':'Jack'}
second_dict.clear()  # {}
name = my_dict.pop('name')  # Jack
print(my_dict)  # {'age': 27}

my_dict = {'Peter': 25, 'John': 20, 'Dan': 30}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)  # {'John': 20, 'Peter': 25, 'Dan': 30}
revers_dict = dict(reversed(sorted(my_dict.items(), key=lambda x: x[1])))
print(revers_dict)  # {'Dan': 30, 'Peter': 25, 'John': 20}

# reverse dict and reverse keys-values
legendary = {"silver": 6, "shards": 8, "hard": 5, "motes": 4}
result = {va: ke for ke, va in dict(reversed(list(legendary.items()))).items()}
print(result)
