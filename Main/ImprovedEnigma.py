alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_dict = {chr(65+i) : i for i in range(26)}

class ReflectorClass(object):

    def __init__(self, listname, name):
        self.listname = listname
        self.name = name

class RotorClass(object):

    def __init__(self, listname, revlistname, name, position, rotortip):  #rotortip is a variable at which place the rotor let's the next rotor turn
        self.listname = listname
        self.name = name
        self.position = position
        self.rotortip = rotortip
        self.revlistname = revlistname

    def DefRotate(self, number):
        self.position = number
        while self.position < 0:
            self.position += 26
        while self.position > 25:
            self.position -= 26

    def Rotate(self):
        self.position += 1
        if self.position == 26:
            self.position = 0

def switch_rotors(rotor1, rotor2, rotor3):
    rotor1.Rotate()
    if rotor1.position == rotor1.rotortip:
        rotor2.Rotate()
    if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
        rotor3.Rotate()

plugdiction = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B"}


def plugboard(input, plugdict):
    if input in plugdict:
        output = plugdict[input]
    else:
        output = input
    return(output)

def enigma(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3):             #userinput is the text to code, rotorsetting1 is the rotorposition of first rotor, and rotorsetting2 for the second rotor

    userinputlist = [i for i in userinput]
    codedlist = []

    rotor1.DefRotate(rotorsetting1)
    rotor2.DefRotate(rotorsetting2)
    rotor3.DefRotate(rotorsetting3)

    rotor1list = rotor1.listname
    rotor2list = rotor2.listname
    rotor3list = rotor3.listname

    rotor1revlist = rotor1.revlistname
    rotor2revlist = rotor2.revlistname
    rotor3revlist = rotor3.revlistname

    reflector = reflector.listname

    for i in userinputlist:
        pos1 = rotor1.position
        pos2 = rotor2.position
        pos3 = rotor3.position

        diff1 = pos2 - pos1
        diff2 = pos3 - pos2

        i = plugboard(i, plugdiction)

        i = alphabet_dict[i]
        i += pos1
        i = i % 26
        i = rotor1list[i]

        i += diff1
        i = i % 26
        i = rotor2list[i]

        i += diff2
        i = i % 26
        i = rotor3list[i]

        i -= pos3
        i = i % 26
        i = reflector[i]

        i += pos3
        i = i % 26
        i = rotor3revlist[i]

        i -= diff2
        i = i % 26
        i = rotor2revlist[i]

        i -= diff1
        i = i % 26
        i = rotor1revlist[i]

        i -= pos1
        i = alphabet_list[i]

        i = plugboard(i, plugdiction)

        codedlist.append(i)
        switch_rotors(rotor1, rotor2, rotor3)

    return("".join(codedlist))

rotorI = RotorClass([alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"], [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9], "Rotor I", 0, 17)
rotorII = RotorClass([alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"], [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18], "Rotor II", 0, 5)
rotorIII = RotorClass([alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"], [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12], "Rotor III", 0, 22)
reflectorB = ReflectorClass([alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"], "B")

if __name__ == "__main__":
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                enigma("A" * 100, rotorI, rotorII, rotorIII, reflectorB, i, j, k)
