class Superheroe:
    def __init__(self, name, year, house, bio):
        self.name = name       
        self.year = year
        self.house = house
        self.bio = bio         

    def __str__(self):
        return f"{self.name} ({self.house}, {self.year})"

def by_name(item):
    return item.name