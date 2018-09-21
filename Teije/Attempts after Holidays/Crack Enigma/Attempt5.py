allcombs = ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ', 'EE', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FF', 'FG', 'FH', 'FI', 'FJ', 'FK', 'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GG', 'GH', 'GI', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'HH', 'HI', 'HJ', 'HK', 'HL', 'HM', 'HN', 'HO', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY', 'HZ', 'II', 'IJ', 'IK', 'IL', 'IM', 'IN', 'IO', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IU', 'IV', 'IW', 'IX', 'IY', 'IZ', 'JJ', 'JK', 'JL', 'JM', 'JN', 'JO', 'JP', 'JQ', 'JR', 'JS', 'JT', 'JU', 'JV', 'JW', 'JX', 'JY', 'JZ', 'KK', 'KL', 'KM', 'KN', 'KO', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX', 'KY', 'KZ', 'LL', 'LM', 'LN', 'LO', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NN', 'NO', 'NP', 'NQ', 'NR', 'NS', 'NT', 'NU', 'NV', 'NW', 'NX', 'NY', 'NZ', 'OO', 'OP', 'OQ', 'OR', 'OS', 'OT', 'OU', 'OV', 'OW', 'OX', 'OY', 'OZ', 'PP', 'PQ', 'PR', 'PS', 'PT', 'PU', 'PV', 'PW', 'PX', 'PY', 'PZ', 'QQ', 'QR', 'QS', 'QT', 'QU', 'QV', 'QW', 'QX', 'QY', 'QZ', 'RR', 'RS', 'RT', 'RU', 'RV', 'RW', 'RX', 'RY', 'RZ', 'SS', 'ST', 'SU', 'SV', 'SW', 'SX', 'SY', 'SZ', 'TT', 'TU', 'TV', 'TW', 'TX', 'TY', 'TZ', 'UU', 'UV', 'UW', 'UX', 'UY', 'UZ', 'VV', 'VW', 'VX', 'VY', 'VZ', 'WW', 'WX', 'WY', 'WZ', 'XX', 'XY', 'XZ', 'YY', 'YZ', 'ZZ']

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

def crackenigma(message, guess):

    whitelist = []
    blacklist = []
    currentlist = []
    plugdict = {}
    checker = ""
    turn = 0
    alfa = True

    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        turn = 0
        alfa = True
        while alfa:

            comb = guess[turn] + i

            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                alfa = False
                break
            checker += comb
            currentlist.append(comb)
            plugdict = DictionConvert(currentlist)
            comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdict) + message[turn]

            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                alfa = False
                break
            checker += comb
            currentlist.append(comb)

            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                turn = 1
                alfa = True
                while alfa:

                    comb = guess[turn] + i

                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                        alfa = False
                        break
                    checker += comb
                    currentlist.append(comb)
                    plugdict = DictionConvert(currentlist)
                    comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 1, 0, 0, plugdict) + message[turn]

                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                        alfa = False
                        break
                    checker += comb
                    currentlist.append(comb)
                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        turn = 2
                        alfa = True
                        while alfa:

                            comb = guess[turn] + i

                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                alfa = False
                                break
                            checker += comb
                            currentlist.append(comb)
                            plugdict = DictionConvert(currentlist)
                            comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 2, 0, 0, plugdict) + message[turn]

                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                alfa = False
                                break
                            checker += comb
                            currentlist.append(comb)
                            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                turn = 3
                                alfa = True
                                while alfa:

                                    comb = guess[turn] + i

                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                        alfa = False
                                        break
                                    checker += comb
                                    currentlist.append(comb)
                                    plugdict = DictionConvert(currentlist)
                                    comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 3, 0, 0, plugdict) + message[turn]

                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                        alfa = False
                                        break
                                    checker += comb
                                    currentlist.append(comb)
                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                        turn = 4
                                        alfa = True
                                        while alfa:

                                            comb = guess[turn] + i

                                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                alfa = False
                                                break
                                            checker += comb
                                            currentlist.append(comb)
                                            plugdict = DictionConvert(currentlist)
                                            comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 4, 0, 0, plugdict) + message[turn]

                                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                alfa = False
                                                break
                                            checker += comb
                                            currentlist.append(comb)
                                            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                turn = 5
                                                alfa = True
                                                while alfa:

                                                    comb = guess[turn] + i

                                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                        alfa = False
                                                        break
                                                    checker += comb
                                                    currentlist.append(comb)
                                                    plugdict = DictionConvert(currentlist)
                                                    comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 5, 0, 0, plugdict) + message[turn]

                                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                        alfa = False
                                                        break
                                                    checker += comb
                                                    currentlist.append(comb)
                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                        turn = 6
                                                        alfa = True
                                                        while alfa:

                                                            comb = guess[turn] + i

                                                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                alfa = False
                                                                break
                                                            checker += comb
                                                            currentlist.append(comb)
                                                            plugdict = DictionConvert(currentlist)
                                                            comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 6, 0, 0, plugdict) + message[turn]

                                                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                alfa = False
                                                                break
                                                            checker += comb
                                                            currentlist.append(comb)
                                                            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                turn = 7
                                                                alfa = True
                                                                while alfa:

                                                                    comb = guess[turn] + i

                                                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                        alfa = False
                                                                        break
                                                                    checker += comb
                                                                    currentlist.append(comb)
                                                                    plugdict = DictionConvert(currentlist)
                                                                    comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 7, 0, 0, plugdict) + message[turn]

                                                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                        alfa = False
                                                                        break
                                                                    checker += comb
                                                                    currentlist.append(comb)
                                                                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                        turn = 8
                                                                        alfa = True
                                                                        while alfa:

                                                                            comb = guess[turn] + i

                                                                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                                alfa = False
                                                                                break
                                                                            checker += comb
                                                                            currentlist.append(comb)
                                                                            plugdict = DictionConvert(currentlist)
                                                                            comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 8, 0, 0, plugdict) + message[turn]

                                                                            if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                                alfa = False
                                                                                break
                                                                            checker += comb
                                                                            currentlist.append(comb)
                                                                            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                                                                turn = 9
                                                                                alfa = True
                                                                                while alfa:

                                                                                    comb = guess[turn] + i

                                                                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                                        alfa = False
                                                                                        break
                                                                                    checker += comb
                                                                                    currentlist.append(comb)
                                                                                    plugdict = DictionConvert(currentlist)
                                                                                    comb = enigmaOne(guess[turn], rotorI, rotorII, rotorIII, reflectorB, 9, 0, 0, plugdict) + message[turn]

                                                                                    if not comb in currentlist and not comb[::-1] in currentlist and (comb[0] in checker or comb[1] in checker):
                                                                                        alfa = False
                                                                                        break
                                                                                    checker += comb
                                                                                    currentlist.append(comb)
                                                                                    print(currentlist)
                                                                                    whitelist.append(currentlist)
                                                                                    alfa = False
                                                                                    break

                                                                                turn = 9
                                                                                plugdict = {}
                                                                                currentlist = currentlist[:(turn * 2)]
                                                                                checker = checker[:(turn * 4)]

                                                                        turn = 8
                                                                        plugdict = {}
                                                                        currentlist = currentlist[:(turn * 2)]
                                                                        checker = checker[:(turn * 4)]

                                                                turn = 7
                                                                plugdict = {}
                                                                currentlist = currentlist[:(turn * 2)]
                                                                checker = checker[:(turn * 4)]


                                                        turn = 6
                                                        plugdict = {}
                                                        currentlist = currentlist[:(turn * 2)]
                                                        checker = checker[:(turn * 4)]

                                                turn = 5
                                                plugdict = {}
                                                currentlist = currentlist[:(turn * 2)]
                                                checker = checker[:(turn * 4)]

                                        turn = 4
                                        plugdict = {}
                                        currentlist = currentlist[:(turn * 2)]
                                        checker = checker[:(turn * 4)]

                                turn = 3
                                plugdict = {}
                                currentlist = currentlist[:(turn * 2)]
                                checker = checker[:(turn * 4)]

                        turn = 2
                        plugdict = {}
                        currentlist = currentlist[:(turn * 2)]
                        checker = checker[:(turn * 4)]

                turn = 1
                plugdict = {}
                currentlist = currentlist[:(turn * 2)]
                checker = checker[:(turn * 4)]


        turn = 0
        plugdict = {}
        currentlist = []
        checker = ""

    newlist = []
    countlist = []
    sortedlist = []
    for i in whitelist:
        for j in i:
            if not j in newlist:
                newlist.append(j)
                countlist.append(1)
            else:
                countlist[newlist.index(j)] += 1

    for i in countlist:
        maximum = max(countlist)
        index = countlist.index(maximum)
        print(newlist[index], maximum)
        countlist.pop(index)
        newlist.pop(index)

    for i in countlist:
        print(newlist[0], i)
        countlist.pop(0)
        newlist.pop(0)


if __name__ == "__main__":
    print(enigma("WETTERBERICHT", rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, DictionConvert(["AB", "CD", "EF", "IJ", "KL", "MN", "OP", "QR", "ST"])))
    print(enigma("WETTERBERICHT", rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, DictionConvert(['WW', 'MN', 'EF', 'AB', 'TS', 'RQ', 'TS', 'DC', 'EF', 'KL', 'RQ', 'VV', 'BA', 'IJ', 'EF', 'NM', 'RQ', 'YY', 'IJ', 'VV'])))
    crackenigma("NBQCLVJMYVNOH", "WETTERBERICHT")
