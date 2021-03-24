class Town:
    def __init__(self, name):
        self.name = name

    def set_latitude(self,latitude):
        self.lat = ''
        for i in latitude:
            if i == chr(92):
                self.lat += ' '
            else:
                self.lat += i

    def set_longitude(self, longitude):
        self.long = ''
        for i in longitude:
            if i == chr(92):
                self.long += ' '
            else:
                self.long += i

    def __repr__(self):
        return f'Town: {self.name} | Latitude: {self.lat} | Longitude: {self.long}'


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
