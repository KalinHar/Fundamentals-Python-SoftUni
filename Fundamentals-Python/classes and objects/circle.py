class Circle:
    __pi = 3.14

    def __init__(self, diameter, angle=0):
        self.radius = diameter / 2
        self.angle = angle

    def calc_circumference(self):
        return Circle.__pi * self.radius * 2

    def calc_area(self):
        return Circle.__pi * self.radius * self.radius

    def calc_sector(self):
        return (self.angle/360) * Circle.calc_area(self)


# diam = float(input())
# ang = int(input())
circle = Circle(10, 5)
print(f"{circle.calc_circumference():.2f}")
print(f"{circle.calc_area():.2f}")
print(f"{circle.calc_sector():.2f}")
