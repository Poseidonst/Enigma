alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_II_list = [i for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
alphabet_dict = {chr(65+i) : i for i in range(26)}
rotor_I_numbers = [alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
rotor_II_numbers = [alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotor_III_numbers = [alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]


class RotorClass(object):

    def __init__(self, listname, name, position, rotortip):  #rotortip is a variable at which place the rotor let's the next rotor turn
        self.listname = listname
        self.name = name
        self.position = position
        self.rotortip = rotortip

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
            self.position += 1
            if self.position == 27:
                self.position = 1
        return (self.listname)

    def switch1(self):
        self.listname += [self.listname.pop(0)]
        self.position += 1
        if self.position == 27:
            self.position = 1
        return (self.listname)

    def reset(self):                    #Resets back to starting position
        places = 26 - self.position
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
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


def rotor1_set(rotor1, rotor2, inputlist, manipulate_list):
    codedlist = []
    for i in inputlist:
        i = alphabet_dict[i]                            #Turns letter into number
        diff = get_difference(rotor1, rotor2)           #Gets the difference between two rotors and where they are relative to eachother
        i = rotor1.listname[i]                          #Makes variable i go through rotor1
        i += diff                                       #Adds the difference to i so it goes at the good spot through rotor2
        i = rotor2.listname[i - rotor2.position]        #i goes through rotor2
        manipulate_list.append(alphabet_list[i])        #Makes a list of all the new outcomes
        rotor1.switch1()                                #Rotor1 switches to next position
        if rotor1.position == rotor1.rotortip:          #If the position of rotor1 is at the turnover-point rotor2 will go to the next position
            rotor2.switch1()

def firstrotor_set(rotor1, rotor2, rotor3, inputlist, manipulate_list):
    for i in inputlist:
        i = alphabet_dict[i]
        diff = get_difference(rotor1, rotor2)
        i = rotor1.listname[i]
        i += diff
        i = i - rotor2.position
        manipulate_list.append(alphabet_list[i])
        switch_rotors(rotor1, rotor2, rotor3)

def secondrotor_set(rotor1, rotor2, rotor3, inputlist, manipulate_list):
    for i in inputlist:
        i = alphabet_dict[i]
        i = rotor2.listname[i]
        diff = get_difference(rotor2, rotor3)
        i += diff
        i = i - rotor3.position
        manipulate_list.append(alphabet_list[i])
        switch_rotors(rotor1, rotor2, rotor3)

def enigma(userinput, rotor1, rotor2, rotor3, rotorsetting1, rotorsetting2, rotorsetting3):             #userinput is the text to code, rotorsetting1 is the rotorposition of first rotor, and rotorsetting2 for the second rotor
    userinputlist = [i for i in userinput]
    codedlist = []
    rotor1.defswitch(rotorsetting1)
    rotor2.defswitch(rotorsetting2)
    rotor3.defswitch(rotorsetting3)
    for i in userinputlist:

        i = alphabet_dict[i]
        i = rotor1.listname[i]

        diff = get_difference(rotor1, rotor2)
        i += diff
        i = rotor2.listname[i - rotor2.position]

        diff = get_difference(rotor2, rotor3)
        i += diff
        i = rotor2.listname[i - rotor3.position]




        codedlist.append(alphabet_list[i])
        switch_rotors(rotor1, rotor2, rotor3)


    return("".join(codedlist))

rotorI = RotorClass(rotor_I_numbers, "I", 0, 1)
rotorII = RotorClass(rotor_II_numbers, "II", 0, 2)
rotorIII = RotorClass(rotor_III_numbers, "III", 0, 9)

print(enigma("A" * 10000000, rotorI, rotorII, rotorIII, 0, 0, 0))
