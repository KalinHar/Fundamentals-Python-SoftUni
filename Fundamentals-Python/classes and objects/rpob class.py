
class Person:
    species = "human"
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
me = Person("Peter", "Johnson", 25)
print(me.first_name) # Peter
print(me.last_name)  # Johnson
me.age += 1
print(me.age)        # 26
print(me.species)  # "human"
print(me.get_full_name())  # Peter Johnson

class Party:
    def __init__(self):
        self.people = []
party = Party()
line = input()
while line != 'End':
    party.people.append(line)
    line = input()
print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')

