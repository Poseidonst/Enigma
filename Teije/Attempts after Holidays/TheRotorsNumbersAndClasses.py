alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_II_list = [i for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
alphabet_dict = {chr(65+i) : i for i in range(26)}
rotor_I_numbers = [alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
rotor_II_numbers = [alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotor_III_numbers = [alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
def make_letters():
    rotor = []
    for i in rotor_I_numbers:
        rotor.append(alphabet_list[i])
    print(rotor)
    print(rotor[alphabet_dict["A"]])

def switch_rotor(rotor, position):
    for i in range(0, position):
        rotor += [rotor.pop(0)]
    return (rotor)


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

rotor_I = RotorClass(rotor_I_numbers, "I", 1, 7)

#print(rotor_I.listname)
#print(rotor_I.name)
#print(rotor_I.switch(1))
print(rotor_I.position)
print(rotor_I.defswitch(1))
print(rotor_I.position)
print(rotor_I.defswitch(1))
print(rotor_I.position)
rotor_I.reset()
print(rotor_I.position)
print(rotor_I.defswitch(1))
print(rotor_I.position)
#print(rotor_I.get_position())
