alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_dict = {chr(65+i) : i for i in range(26)}

class ReflectorClass(object):

    def __init__(self, listname):
        self.listname = listname

class RotorClass(object):

    def __init__(self, listname, revlistname, position, rotortip):
        self.listname = listname
        self.revlistname = revlistname
        self.position = position
        self.rotortip = rotortip

plugdiction = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B",
               "J" : "P", "P" : "J",
               "M" : "L", "L" : "M",
               "Q" : "V", "V" : "Q",}

emptydict = {}

testdict = {"T" : "M", "M" : "T",
            "O" : "B", "B" : "O",
            "C" : "N", "N" : "C",
            "W" : "Q", "Q" : "W",}

def enigma(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3, plugdictionary):

    plugdict = plugdictionary

    output = ""

    rotor1.position = rotorsetting1 % 26
    rotor2.position = rotorsetting2 % 26
    rotor3.position = rotorsetting3 % 26

    rotor1list = rotor1.listname
    rotor2list = rotor2.listname
    rotor3list = rotor3.listname

    rotor1revlist = rotor1.revlistname
    rotor2revlist = rotor2.revlistname
    rotor3revlist = rotor3.revlistname

    reflector = reflector.listname

    for i in userinput.upper():
        pos1 = rotor1.position
        pos2 = rotor2.position
        pos3 = rotor3.position

        diff1 = pos2 - pos1
        diff2 = pos3 - pos2


        try:
            i = plugdict[i]
        except:
            pass

        i = alphabet_dict[i]

        i = rotor1list[(i + pos1) % 26]

        i = rotor2list[(i + diff1) % 26]

        i = rotor3list[(i + diff2) % 26]

        i = reflector[(i - pos3) % 26]

        i = rotor3revlist[(i + pos3) % 26]

        i = rotor2revlist[(i - diff2) % 26]

        i = rotor1revlist[(i - diff1) % 26]

        i = alphabet_list[(i - pos1) % 26]


        try:
            i = plugdict[i]
        except:
            pass

        output += i

        rotor1.position = (rotor1.position + 1) % 26
        if rotor1.position == rotor1.rotortip:
            rotor2.position = (rotor2.position + 1) % 26
        if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
            rotor3.position = (rotor3.position + 1) % 26

    return(output)

def enigmaOne(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3, plugdictionary):

    plugdict = plugdictionary

    output = ""

    rotor1.position = rotorsetting1 % 26
    rotor2.position = rotorsetting2 % 26
    rotor3.position = rotorsetting3 % 26


    rotor1list = rotor1.listname
    rotor2list = rotor2.listname
    rotor3list = rotor3.listname

    rotor1revlist = rotor1.revlistname
    rotor2revlist = rotor2.revlistname
    rotor3revlist = rotor3.revlistname

    reflector = reflector.listname

    pos1 = rotor1.position
    pos2 = rotor2.position
    pos3 = rotor3.position

    diff1 = pos2 - pos1
    diff2 = pos3 - pos2

    i = userinput.upper()

    try:
        i = plugdict[i]
    except:
        pass

    i = alphabet_dict[i]

    i = rotor1list[(i + pos1) % 26]

    i = rotor2list[(i + diff1) % 26]

    i = rotor3list[(i + diff2) % 26]

    i = reflector[(i - pos3) % 26]

    i = rotor3revlist[(i + pos3) % 26]

    i = rotor2revlist[(i - diff2) % 26]

    i = rotor1revlist[(i - diff1) % 26]

    i = alphabet_list[(i - pos1) % 26]


    # try:
    #     i = plugdict[i]
    # except:
    #     pass

    output += i

    return(output)

rotorI = RotorClass([alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"], [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9], 0, 17)
rotorII = RotorClass([alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"], [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18], 0, 5)
rotorIII = RotorClass([alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"], [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12], 0, 22)
reflectorB = ReflectorClass([alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"])
reflectorC = ReflectorClass([alphabet_dict[i] for i in "FVPJIAOYEDRZXWGCTKUQSBNMHL"])

#================================================================================#
def Rotator(pos1, pos2, pos3, amount):
    counter = 0
    while counter != amount:
        pos1 = (pos1 + 1) % 26
        if pos1 == rotorI.rotortip:
            pos2 = (pos2 + 1) % 26
        if pos1 == rotorI.rotortip and pos2 == rotorII.rotortip:
            pos3 = (pos3 + 1) % 26
        counter += 1
    outputlist = [pos1, pos2, pos3]
    return(outputlist)

def DictionConvert(list):
    diction = {}
    for i in list:
        diction[i[0]] = i[1]
        diction[i[1]] = i[0]
    return(diction)

def CrackLoop(guess, message, pos1, pos2, pos3):
    pass



def CrackEnigma(message, guess):
    total = message + guess
    countdict = {}
    countlist = []
    impdict = {}
    currentlist = []
    checkstring = ""
    blacklist = []
    for i in total:
        if not i in countdict:
            countdict[i] = 1
        else:
            countdict[i] += 1
    countlist = list(countdict.values())
    maximum = max(countlist)
    frequent = list(countdict.keys())[countlist.index(maximum)]
    for i in range(len(message)):
        if message[i] == frequent:
            impdict[i] = (message[i] + guess[i])
        if guess[i] == frequent:
            impdict[i] = (guess[i] + message[i])

    valuelist = list(impdict.keys())
    print(valuelist)

    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        currentlist.append(frequent + i)
        checkstring += frequent + i
        plugdict = DictionConvert(currentlist)
        add = enigmaOne(frequent, rotorI, rotorII, rotorIII, reflectorB, valuelist[0], 0, 0, plugdict) + impdict[valuelist[0]][1]
        if add not in currentlist and add[::-1] not in currentlist and (add[0] in checkstring or add[1] in checkstring):
            pass
        else:
            currentlist.append(add)
            checkstring += add
            add = enigmaOne(frequent, rotorI, rotorII, rotorIII, reflectorB, valuelist[1], 0, 0, plugdict) + impdict[valuelist[1]][1]
            if add not in currentlist and add[::-1] not in currentlist and (add[0] in checkstring or add[1] in checkstring):
                pass
            else:
                currentlist.append(add)
                checkstring += add
                add = enigmaOne(frequent, rotorI, rotorII, rotorIII, reflectorB, valuelist[2], 0, 0, plugdict) + impdict[valuelist[2]][1]
                if add not in currentlist and add[::-1] not in currentlist and (add[0] in checkstring or add[1] in checkstring):
                    pass
                else:
                    currentlist.append(add)
                    checkstring += add
                    add = enigmaOne(frequent, rotorI, rotorII, rotorIII, reflectorB, valuelist[3], 0, 0, plugdict) + impdict[valuelist[3]][1]
                    if add not in currentlist and add[::-1] not in currentlist and (add[0] in checkstring or add[1] in checkstring):
                        pass
                    else:
                        currentlist.append(add)
                        checkstring += add
                        print(currentlist)
        currentlist = []
        checkstring = ""
        plugdict = {}







if __name__ == "__main__":
    print(enigma("WETTERBERICHT", rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, DictionConvert(['AB', 'DC', 'RH', 'KU'])))
    CrackEnigma("MVBECUIRWBMYC", "WETTERBERICHT")
