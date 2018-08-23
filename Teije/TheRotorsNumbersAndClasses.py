alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_dict = {chr(65+i) : i for i in range(26)}
rotor_I_numbers = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor_I_numbers_backup = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor_II_numbers = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

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

    def __init__(self, listname, backup, name, counter):
        self.listname = listname
        self.backup = backup
        self.name = name
        self.counter = counter

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
            self.counter += 1
            if self.counter == 27:
                self.counter = 1
        return (self.listname)

    def reset(self):                    #Resets back to starting position
        places = 26 - self.counter
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
        self.counter = 0


rotor_I = RotorClass(rotor_I_numbers, rotor_I_numbers_backup, "I", 0)

#print(rotor_I.listname)
#print(rotor_I.name)
#print(rotor_I.switch(1))
print(rotor_I.counter)
print(rotor_I.defswitch(-52))
print(rotor_I.counter)
print(rotor_I.defswitch(1))
print(rotor_I.counter)
rotor_I.reset()
print(rotor_I.counter)
print(rotor_I.defswitch(1))
print(rotor_I.counter)
#print(rotor_I.get_position())
