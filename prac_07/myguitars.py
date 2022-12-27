class MyGuitar:
    def __init__(self,name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year},{self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def main():
    guitar = []
    in_file = open("guitars.csv", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitars = MyGuitar(parts[0], int(parts[1]), float(parts[2]))
        guitar.append(guitars)
    in_file.close()

    for i in guitar:
        guitar.sort()
        print(i)




main()
