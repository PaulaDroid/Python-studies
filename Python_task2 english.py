class Competitor:
    points = 0
    color = 0

    def situation(self, points, color):
        points = 0
        color = "blue"
        print(f"I'm {color} and I have {points} points!")

    def score(self, points):
        points += points

first = Competitor()
first.color = "blue"
first.score(1)
first.situation("0", "blue")
