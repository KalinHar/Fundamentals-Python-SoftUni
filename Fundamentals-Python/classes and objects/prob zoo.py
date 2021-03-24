class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []  # TODO: create 3 lists (mammals, fishes, birds)
        self.fishes = []
        self.birds = []
    def add_animal(self, species, ame):
        if species == 'mammals':  # TODO: add the name to the given species
            zoo.mammals.append(ame)
        elif species == 'fishes':
            zoo.fishes.append(ame)
        elif species == 'birds':
            zoo.birds.append(ame)
    def get_info(self, species):
        if species == 'mammals':
            kind = zoo.mammals
        elif species == 'fishes':
            kind = zoo.fishes
        elif species == 'birds':
            kind = zoo.birds
        print(f'In {zoo.name} have {len(kind)} {species} of {total_animals} animals.') # TODO: create the resulting string and return it
        print(f'{species}: {"; ".join(kind)}')
zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
total_animals = 0
for i in range(count):
    line = input().split(' ')  # Read the input
    zoo.add_animal(line[0], line[1])  # Add the new animal
    total_animals += 1  # Update the total_animals variable
info = input()
zoo.get_info(info)
