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

def DictionConvert(list):
    diction = {}
    for i in list:
        diction[i[0]] = i[1]
        diction[i[1]] = i[0]
    return(diction)

def CrackLoop(guess, message, pos1, pos2, pos3):
    length = len(message)
    plugdict = {}
    currentlist = []
    checkstring = ""
    counter = 0
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        itemnumber = 0
        firstadd = guess[itemnumber] + i
        for item in firstadd:
            if item in checkstring:
                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                    break
        else:
            currentlist.append(firstadd)
            plugdict = DictionConvert(currentlist)
            checkstring += firstadd

            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
            secondadd = first + message[itemnumber]

            for item in secondadd:
                if item in checkstring:
                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                        break
            else:
                currentlist.append(secondadd)
                plugdict = DictionConvert(currentlist)
                checkstring += secondadd
                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 1:

                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        itemnumber = 1
                        firstadd = guess[itemnumber] + i
                        for item in firstadd:
                            if item in checkstring:
                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                    break
                        else:
                            currentlist.append(firstadd)
                            plugdict = DictionConvert(currentlist)
                            checkstring += firstadd

                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                            secondadd = first + message[itemnumber]
                            for item in secondadd:
                                if item in checkstring:
                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                        break
                            else:
                                currentlist.append(secondadd)
                                plugdict = DictionConvert(currentlist)
                                checkstring += secondadd
                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 2:

                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                        itemnumber = 2
                                        firstadd = guess[itemnumber] + i
                                        for item in firstadd:
                                            if item in checkstring:
                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                    break
                                        else:
                                            currentlist.append(firstadd)
                                            plugdict = DictionConvert(currentlist)
                                            checkstring += firstadd

                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                            secondadd = first + message[itemnumber]
                                            for item in secondadd:
                                                if item in checkstring:
                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                        break
                                            else:
                                                currentlist.append(secondadd)
                                                plugdict = DictionConvert(currentlist)
                                                checkstring += secondadd
                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 3:
                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                        itemnumber = 3
                                                        firstadd = guess[itemnumber] + i
                                                        for item in firstadd:
                                                            if item in checkstring:
                                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                                    break
                                                        else:
                                                            currentlist.append(firstadd)
                                                            plugdict = DictionConvert(currentlist)
                                                            checkstring += firstadd

                                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                                            secondadd = first + message[itemnumber]
                                                            for item in secondadd:
                                                                if item in checkstring:
                                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                                        break
                                                            else:
                                                                currentlist.append(secondadd)
                                                                plugdict = DictionConvert(currentlist)
                                                                checkstring += secondadd
                                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 4:
                                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                        itemnumber = 4
                                                                        firstadd = guess[itemnumber] + i
                                                                        for item in firstadd:
                                                                            if item in checkstring:
                                                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                                                    break
                                                                        else:
                                                                            currentlist.append(firstadd)
                                                                            plugdict = DictionConvert(currentlist)
                                                                            checkstring += firstadd

                                                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                                                            secondadd = first + message[itemnumber]
                                                                            for item in secondadd:
                                                                                if item in checkstring:
                                                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                                                        break
                                                                            else:
                                                                                currentlist.append(secondadd)
                                                                                plugdict = DictionConvert(currentlist)
                                                                                checkstring += secondadd
                                                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 5:
                                                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                                        itemnumber = 5
                                                                                        firstadd = guess[itemnumber] + i
                                                                                        for item in firstadd:
                                                                                            if item in checkstring:
                                                                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                                                                    break
                                                                                        else:
                                                                                            currentlist.append(firstadd)
                                                                                            plugdict = DictionConvert(currentlist)
                                                                                            checkstring += firstadd

                                                                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                                                                            secondadd = first + message[itemnumber]
                                                                                            for item in secondadd:
                                                                                                if item in checkstring:
                                                                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                                                                        break
                                                                                            else:
                                                                                                currentlist.append(secondadd)
                                                                                                plugdict = DictionConvert(currentlist)
                                                                                                checkstring += secondadd
                                                                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 6:
                                                                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                                                        itemnumber = 6
                                                                                                        firstadd = guess[itemnumber] + i
                                                                                                        for item in firstadd:
                                                                                                            if item in checkstring:
                                                                                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                                                                                    break
                                                                                                        else:
                                                                                                            currentlist.append(firstadd)
                                                                                                            plugdict = DictionConvert(currentlist)
                                                                                                            checkstring += firstadd

                                                                                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                                                                                            secondadd = first + message[itemnumber]
                                                                                                            for item in secondadd:
                                                                                                                if item in checkstring:
                                                                                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                                                                                        break
                                                                                                            else:
                                                                                                                currentlist.append(secondadd)
                                                                                                                plugdict = DictionConvert(currentlist)
                                                                                                                checkstring += secondadd
                                                                                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 7:
                                                                                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                                                                        itemnumber = 7
                                                                                                                        firstadd = guess[itemnumber] + i
                                                                                                                        for item in firstadd:
                                                                                                                            if item in checkstring:
                                                                                                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                                                                                                    break
                                                                                                                        else:
                                                                                                                            currentlist.append(firstadd)
                                                                                                                            plugdict = DictionConvert(currentlist)
                                                                                                                            checkstring += firstadd

                                                                                                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                                                                                                            secondadd = first + message[itemnumber]
                                                                                                                            for item in secondadd:
                                                                                                                                if item in checkstring:
                                                                                                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                                                                                                        break
                                                                                                                            else:
                                                                                                                                currentlist.append(secondadd)
                                                                                                                                plugdict = DictionConvert(currentlist)
                                                                                                                                checkstring += secondadd
                                                                                                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 8:
                                                                                                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                                                                                        itemnumber = 8
                                                                                                                                        firstadd = guess[itemnumber] + i
                                                                                                                                        for item in firstadd:
                                                                                                                                            if item in checkstring:
                                                                                                                                                if not firstadd in currentlist and not firstadd[::-1] in currentlist:
                                                                                                                                                    break
                                                                                                                                        else:
                                                                                                                                            currentlist.append(firstadd)
                                                                                                                                            plugdict = DictionConvert(currentlist)
                                                                                                                                            checkstring += firstadd

                                                                                                                                            first = enigmaOne(guess[itemnumber], rotorI, rotorII, rotorIII, reflectorB, pos1 + itemnumber, pos2, pos3, plugdict)
                                                                                                                                            secondadd = first + message[itemnumber]
                                                                                                                                            for item in secondadd:
                                                                                                                                                if item in checkstring:
                                                                                                                                                    if not secondadd in currentlist and not secondadd[::-1] in currentlist:
                                                                                                                                                        break
                                                                                                                                            else:
                                                                                                                                                currentlist.append(secondadd)
                                                                                                                                                plugdict = DictionConvert(currentlist)
                                                                                                                                                checkstring += secondadd
                                                                                                                                                if enigma(guess[0:itemnumber + 1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) == message[0:itemnumber + 1] and length > 9:
                                                                                                                                                    listname = [i for i in currentlist if not i[0] == i[1]]
                                                                                                                                                    listname2 = []
                                                                                                                                                    for i in listname:
                                                                                                                                                        if i not in listname2 and i[::-1] not in listname2:
                                                                                                                                                            listname2.append(i)
                                                                                                                                                    print(listname2)
                                                                                                                                                    counter += 1



                                                                                                                                        itemnumber = 8
                                                                                                                                        currentlist = currentlist[:2*itemnumber]
                                                                                                                                        checkstring = checkstring[:4*itemnumber]
                                                                                                                                        plugdict = {}



                                                                                                                        itemnumber = 7
                                                                                                                        currentlist = currentlist[:2*itemnumber]
                                                                                                                        checkstring = checkstring[:4*itemnumber]
                                                                                                                        plugdict = {}



                                                                                                        itemnumber = 6
                                                                                                        currentlist = currentlist[:2*itemnumber]
                                                                                                        checkstring = checkstring[:4*itemnumber]
                                                                                                        plugdict = {}


                                                                                        itemnumber = 5
                                                                                        currentlist = currentlist[:2*itemnumber]
                                                                                        checkstring = checkstring[:4*itemnumber]
                                                                                        plugdict = {}


                                                                        itemnumber = 4
                                                                        currentlist = currentlist[:2*itemnumber]
                                                                        checkstring = checkstring[:4*itemnumber]
                                                                        plugdict = {}

                                                        itemnumber = 3
                                                        currentlist = currentlist[:2*itemnumber]
                                                        checkstring = checkstring[:4*itemnumber]
                                                        plugdict = {}

                                        itemnumber = 2
                                        currentlist = currentlist[:2*itemnumber]
                                        checkstring = checkstring[:4*itemnumber]
                                        plugdict = {}

                        itemnumber = 1
                        currentlist = currentlist[:2*itemnumber]
                        checkstring = checkstring[:4*itemnumber]
                        plugdict = {}


        itemnumber = 0
        currentlist = currentlist[:2*itemnumber]
        checkstring = checkstring[:4*itemnumber]
        plugdict = {}

    # print(counter)



def CrackEnigma(message, guess):

    length = len(message)
    message = message.upper()
    guess = guess.upper()
    plugdict = {}
    blacklist = []
    currentlist = []
    checkstring = ""
    firstadd = ""
    counter = 0

    CrackLoop(guess, message, 0, 0, 0)

    # for i in range(26):
    #     for j in range(26):
    #         for k in range(26):
    #             CrackLoop(guess, message, plugdict,currentlist, checkstring, i, j, k)
    #             counter += 1
    #             print(counter)




if __name__ == "__main__":
    print(enigma("HALLO", rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, DictionConvert(['AB', 'DC', 'RH', 'KU', 'BA'])))
    print(enigma("HALLOHOEGAATHET", rotorI, rotorII, rotorIII, reflectorB, 1, 0, 0, DictionConvert(['TC', 'XF', 'ED', 'IK', 'JV', 'CT', 'NS'])))
    CrackEnigma("IWONZ", "HALLO")
    # listname = ["AA", "BB", "AA", "CC", "DA", "BA", "AB", "DA"]
    # print(listname)
    # listname = [i for i in listname if i[0] != i[1] and i[::-1] in listname]
    # print(listname)
