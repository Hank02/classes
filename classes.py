class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end = " ")
        print()

class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Baang", "Baaang"])
    
    def count(self, number):
        for i in range(1, number + 1):
            print(i)
        print("Now combusting...")

class Band(Musician):
    roster = []
    
    def hire(self, new):
        roster.append(new)
    
    def fire(self, fired):
        if fired in roster:
            roster.remove(fired)

    def concert(self, roster):
        self.count(4)
        for each in roster:
            each.solo(5)

print("Guitarist:")
nigel = Guitarist()
nigel.solo(10)

print("Bassist:")
jon = Bassist()
jon.solo(8)

print("Drummer:")
mark = Drummer()
mark.solo(6)
mark.count(4)



