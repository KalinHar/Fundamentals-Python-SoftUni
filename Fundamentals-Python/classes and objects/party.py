class Party:
    def __init__(self):
        self.people = []

    def invite(self, guest):
        self.people.append(guest)

    def names_of_guests(self):
        return ', '.join(self.people)

    def num_of_guests(self):
        return len(self.people)


result = []
while True:
    party = Party()
    line = input()
    if line == 'finish':
        break
    while line != 'End':
        party.invite(line)
        line = input()
    # print(f'Going: {party.names_of_guests()}')
    # print(f'Total: {party.num_of_guests()}')
    result.append(party)
for i, r in enumerate(result):
    print(f'Party - {i + 1}')
    print(f'Going: {r.names_of_guests()}')
    print(f'Total: {r.num_of_guests()}')


