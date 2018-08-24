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

    def reset(self):                    #Resets back to starting position
        places = 26 - self.position
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
        self.position = 0

def get_difference(rotor1, rotor2):
    difference = rotor2.position - rotor1.position
    return(difference)

def enigma():
    userinput = "AAAAA"              #str(input("Give a letter: ")).upper()
    userinputlist = [i for i in userinput]
    codedlist = []
    userrotor1 = 0
    userrotor2 = 1
    for i in userinputlist:
        rotorI.defswitch(userrotor1)
        rotorII.defswitch(userrotor2)
        i = alphabet_dict[i]
        diff = get_difference(rotorI, rotorII)
        i = rotorI.listname[i]
        i += diff
        i = rotorII.listname[i - rotorII.position]
        codedlist.append(alphabet_list[i])
        userrotor1 += 1
    for i in codedlist:
        print(i, end = "")


rotorI = RotorClass(rotor_I_numbers, "I", 0, 7)
rotorII = RotorClass(rotor_II_numbers, "II", 0, 8)
enigma()
