#the only things you need to change to adapt to new years should be freshman and freshmanhouses
freshmanhouses = {"Zane": "Pforzheimer", "Amari": "Pforzheimer", "Timi": "Pforzheimer", "Simon": "Mather"}
freshman = ["Simon", "Amari", "Timi", "Zane"]

class player:
    def __init__(self, name):
        self.name = name
        self.guesses = {}
        self.score = 0

    def guess(self, freshman, house):
        self.guesses[freshman] = house

    def saveguesses(self, guesses):
        for i in range(len(freshman)):
            self.guess(freshman[i], house(guesses[i + 3]))

    def getscore(self):
        allquad = True
        for freshman, house in self.guesses.items():
            realhouse = freshmanhouses[freshman]
            if house not in quad:
                allquad = False
            if house == realhouse:
                self.score += 4
            for neighborhood in houseNeighborhoods:
                if (realhouse in neighborhood) and (house in neighborhood) and (realhouse != house):
                    self.score += 1
        if allquad == True:
            self.score += 1

def house(string):
    for neighborhood in houseNeighborhoods:
        for house in neighborhood:
            if house in string:
                return house
    return "uh oh"

quad = ["Pforzheimer", "Currier", "Cabot"]
riverwest = ["Eliot", "Winthrop", "Kirkland"]
square = ["Adams", "Quincy", "Lowell"]
rivereast = ["Dunster", "Leverett", "Mather"]
houseNeighborhoods = [quad, riverwest, square, rivereast]