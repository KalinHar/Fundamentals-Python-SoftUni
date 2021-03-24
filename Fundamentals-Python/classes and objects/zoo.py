class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, ame):
        if species == 'mammal':
            self.mammals.append(ame)
        elif species == 'fish':
            self.fishes.append(ame)
        elif species == 'bird':
            self.birds.append(ame)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    specs, name = input().split(' ')
    zoo.add_animal(specs, name)

info = input()
print(zoo.get_info(info))
