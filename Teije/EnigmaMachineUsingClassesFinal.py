alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_II_list = [i for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
alphabet_dict = {chr(65+i) : i for i in range(26)}
rotor_I_numbers = [alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
rotorI_reversed_numbers = [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9]
rotor_II_numbers = [alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotorII_reversed_numbers = [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18]
rotor_III_numbers = [alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
rotorIII_reversed_numbers = [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12]
reflector_B_numbers = [alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]
reflector_B_reverse = []

def reverser(listname):
    reversed = []
    for i in alphabet_list:
        for j in listname:
            if i == alphabet_list[j]:
                reversed.append(listname.index(j))
    return(reversed)

class RotorClass(object):

    def __init__(self, listname, revlistname, name, position, rotortip):  #rotortip is a variable at which place the rotor let's the next rotor turn
        self.listname = listname
        self.name = name
        self.position = position
        self.rotortip = rotortip
        self.revlistname = revlistname

    def __repr__(self):
        return(str(self.listname))

    def switch(self, places):           #Switches and goes back to starting position immediately
        new_rotor = []
        while places < 0:               #This way it works with negative numbers as well
            places = places + 26
        while places > 26:
            places = places - 26
        new_rotor = self.listname[places:]
        for i in range(0, places):
            new_rotor.append(self.listname[i])
        return (new_rotor)

    def defswitch(self, places):
        while places < 0:               #This way it works with negative numbers as well
            places = places + 26
        while places > 26:
            places = places - 26       #Switches and stays at that position
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
            self.revlistname += [self.revlistname.pop(0)]
            self.position += 1
            if self.position == 27:
                self.position = 1
        return (self.listname)

    def switch1(self):
        self.listname += [self.listname.pop(0)]
        self.revlistname += [self.revlistname.pop(0)]
        self.position += 1
        if self.position == 27:
            self.position = 1
        return (self.listname)

    def reset(self):                    #Resets back to starting position
        places = 26 - self.position
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
            self.revlistname += [self.revlistname.pop(0)]
        self.position = 0

def get_difference(rotor1, rotor2):
    difference = rotor2.position - rotor1.position
    return(difference)

def switch_rotors(rotor1, rotor2, rotor3):
    rotor1.switch1()
    if rotor1.position == rotor1.rotortip:
        rotor2.switch1()
    if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
        rotor3.switch1()

def enigma(userinput, rotor1, rotor2, rotor3, rotorsetting1, rotorsetting2, rotorsetting3):             #userinput is the text to code, rotorsetting1 is the rotorposition of first rotor, and rotorsetting2 for the second rotor
    userinputlist = [i for i in userinput]
    codedlist = []
    rotor1.defswitch(rotorsetting1)
    rotor2.defswitch(rotorsetting2)
    rotor3.defswitch(rotorsetting3)
    for i in userinputlist:

        i = alphabet_dict[i]                                #From touchpress through rotor 1
        i = rotor1.listname[i]

        diff = get_difference(rotor1, rotor2)               #From rotor1 through rotor2
        i += diff
        i = rotor2.listname[i - rotor2.position]

        diff = get_difference(rotor2, rotor3)               #From rotor2 through rotor3
        i += diff
        i = rotor3.listname[i - rotor3.position]

        i = reflectorB.listname[i - rotor3.position]        #From rotor3 through reflector

        i = rotor3.revlistname[i]                           #From reflector back through rotor 3

        diff = get_difference(rotor3, rotor2)               #From rotor 3 back through rotor 2
        i += diff
        i = rotor2.revlistname[i - rotor2.position]

        diff = get_difference(rotor2, rotor1)               #From rotor 2 back through rotor 1
        i += diff
        i = rotor1.revlistname[i - rotor1.position]

        i = i - rotor1.position                             #From rotor 1 back through the output

        codedlist.append(alphabet_list[i])
        switch_rotors(rotor1, rotor2, rotor3)

    rotor1.reset()
    rotor2.reset()
    rotor3.reset()
    return("".join(codedlist))

rotorI = RotorClass(rotor_I_numbers, rotorI_reversed_numbers, "I", 0, 1)
rotorII = RotorClass(rotor_II_numbers, rotorII_reversed_numbers, "II", 0, 1)
rotorIII = RotorClass(rotor_III_numbers, rotorIII_reversed_numbers, "III", 0, 9)
reflectorB = RotorClass(reflector_B_numbers, reflector_B_reverse, "B", 0, 0)


print(enigma("A" * 100, rotorI, rotorII, rotorIII, 10, 12, 24))
print(enigma("HZFXJOOFEISSPJDZCHITMLGPBHXKPCVSJZIZWHBIMCTZPIDERUCVBPMURUIDVCYZDRQYUSKBNJSBEYQZFJGEPNJOVBIXBFEFUZDC", rotorI, rotorII, rotorIII, 10, 12, 24))
