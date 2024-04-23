class Competitor:

    """Competitor: contains points and color"""

    points= ""
    color = ""

    def __init__(self, ask_color1, ask_color2):
        self.ask_color1 = input("Give me color: ")
        self.ask_color2 = input("Give me color: ")

first = Competitor()
first.points = 0
first.color = ask_color1
print(f'Competitor {first.color} has {first.points} points!')

second = Competitor()
second.points = 0
second.color = ask_color2
print(f'Competitor {second.color} has {second.points} points!')

print([first].__doc__)