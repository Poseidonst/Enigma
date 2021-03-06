import multiprocessing

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

emptydict = {}

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

def enigmaOne(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3, plugdict):

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

    i = alphabet_dict[i]

    i = rotor1list[(i + pos1) % 26]

    i = rotor2list[(i + diff1) % 26]

    i = rotor3list[(i + diff2) % 26]

    i = reflector[(i - pos3) % 26]

    i = rotor3revlist[(i + pos3) % 26]

    i = rotor2revlist[(i - diff2) % 26]

    i = rotor1revlist[(i - diff1) % 26]

    i = alphabet_list[(i - pos1) % 26]

    return(i)

rotorI = RotorClass([alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"], [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9], 0, 17)
rotorII = RotorClass([alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"], [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18], 0, 5)
rotorIII = RotorClass([alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"], [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12], 0, 22)
reflectorB = ReflectorClass([alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"])
reflectorC = ReflectorClass([alphabet_dict[i] for i in "FVPJIAOYEDRZXWGCTKUQSBNMHL"])


#------------------------------------- Het kraken van de enigmamachine begint hieronder ---------------------------------------------------#

"""
Rotator is een functie die buiten de enigma functie de rotors kan laten draaien.
Dit is vooral belangrijk voor later gebruik in het programma.
"""

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

"""
DictionConvert is een functie die een lijst van schakelbordinstellingen om kan zetten in een bruikbare dictionary.
"""

def DictionConvert(list):
    diction = {}
    for i in list:
        diction[i[0]] = i[1]
        diction[i[1]] = i[0]
    return(diction)

"""

"""

def analyse(input1, input2):
    state = True
    inputstr1 = ""
    output = []

    for i in input1:
        inputstr1 += i

    for i in input2:
        if i not in input1 and i[::-1] not in input1:
            if i[0] in inputstr1 or i[1] in inputstr1:
                state = False
                break

    if state:
        for i in input1 + input2:
            if i not in output and i[::-1] not in output:
                output.append(i)

    return(state, output)


"""
takeSecond is voor het begrijpen van het kraken van de enigma niet erg relevant.
"""
def takeSecond(elem):
    return elem[1]


"""

"""
def loop(end_list, msg, ciph, c1, c2, c3, start_pos):
    if len(end_list) == 12:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0]:
                                                    input5 = outcome[1]
                                                    for o in end_list[6]:
                                                        outcome = analyse(input5, o)
                                                        if outcome[0]:
                                                            input6 = outcome[1]
                                                            for p in end_list[7]:
                                                                outcome = analyse(input6, p)
                                                                if outcome[0]:
                                                                    input7 = outcome[1]
                                                                    for q in end_list[8]:
                                                                        outcome = analyse(input7, q)
                                                                        if outcome[0]:
                                                                            input8 = outcome[1]
                                                                            for r in end_list[9]:
                                                                                outcome = analyse(input8, r)
                                                                                if outcome[0]:
                                                                                    input9 = outcome[1]
                                                                                    for s in end_list[10]:
                                                                                        outcome = analyse(input9, s)
                                                                                        if outcome[0]:
                                                                                            input10 = outcome[1]
                                                                                            for t in end_list[11]:
                                                                                                outcome = analyse(input10, t)
                                                                                                if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                                                                    print(outcome[1], start_pos)
    if len(end_list) == 11:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0]:
                                                    input5 = outcome[1]
                                                    for o in end_list[6]:
                                                        outcome = analyse(input5, o)
                                                        if outcome[0]:
                                                            input6 = outcome[1]
                                                            for p in end_list[7]:
                                                                outcome = analyse(input6, p)
                                                                if outcome[0]:
                                                                    input7 = outcome[1]
                                                                    for q in end_list[8]:
                                                                        outcome = analyse(input7, q)
                                                                        if outcome[0]:
                                                                            input8 = outcome[1]
                                                                            for r in end_list[9]:
                                                                                outcome = analyse(input8, r)
                                                                                if outcome[0]:
                                                                                    input9 = outcome[1]
                                                                                    for s in end_list[10]:
                                                                                        outcome = analyse(input9, s)
                                                                                        if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                                                            print(outcome[1], start_pos)
    if len(end_list) == 10:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0]:
                                                    input5 = outcome[1]
                                                    for o in end_list[6]:
                                                        outcome = analyse(input5, o)
                                                        if outcome[0]:
                                                            input6 = outcome[1]
                                                            for p in end_list[7]:
                                                                outcome = analyse(input6, p)
                                                                if outcome[0]:
                                                                    input7 = outcome[1]
                                                                    for q in end_list[8]:
                                                                        outcome = analyse(input7, q)
                                                                        if outcome[0]:
                                                                            input8 = outcome[1]
                                                                            for r in end_list[9]:
                                                                                outcome = analyse(input8, r)
                                                                                if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                                                    print(outcome[1], start_pos)
    if len(end_list) == 9:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0]:
                                                    input5 = outcome[1]
                                                    for o in end_list[6]:
                                                        outcome = analyse(input5, o)
                                                        if outcome[0]:
                                                            input6 = outcome[1]
                                                            for p in end_list[7]:
                                                                outcome = analyse(input6, p)
                                                                if outcome[0]:
                                                                    input7 = outcome[1]
                                                                    for q in end_list[8]:
                                                                        outcome = analyse(input7, q)
                                                                        if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                                            print(outcome[1], start_pos)
    if len(end_list) == 8:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0]:
                                                    input5 = outcome[1]
                                                    for o in end_list[6]:
                                                        outcome = analyse(input5, o)
                                                        if outcome[0]:
                                                            input6 = outcome[1]
                                                            for p in end_list[7]:
                                                                outcome = analyse(input6, p)
                                                                if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                                    print(outcome[1], start_pos)

    if len(end_list) == 7:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0]:
                                                    input5 = outcome[1]
                                                    for o in end_list[6]:
                                                        outcome = analyse(input5, o)
                                                        if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                            print(outcome[1], start_pos)
    if len(end_list) == 6:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0]:
                                            input4 = outcome[1]
                                            for n in end_list[5]:
                                                outcome = analyse(input4, n)
                                                if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                                    print(outcome[1], start_pos)
    if len(end_list) == 5:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0]:
                                    input3 = outcome[1]
                                    for m in end_list[4]:
                                        outcome = analyse(input3, m)
                                        if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                            print(outcome[1], start_pos)
    if len(end_list) == 4:
        for i in end_list[0]:
            for j in end_list[1]:
                outcome = analyse(i, j)
                if outcome[0]:
                    input1 = outcome[1]
                    for k in end_list[2]:
                        outcome = analyse(input1, k)
                        if outcome[0]:
                            input2 = outcome[1]
                            for l in end_list[3]:
                                outcome = analyse(input2, l)
                                if outcome[0] and enigma(msg, rotorI, rotorII, rotorIII, reflectorB,c1, c2, c3, DictionConvert(outcome[1])) == ciph:
                                    print(outcome[1], start_pos)
    if len(end_list) <= 3:
        print("The message is too short, we cannot decipher this", len(end_list))



"""
Crackloop gebruikt via de functie Loop() verschillende loops om te onderzoeken of er bepaalde schakelbord schakelingen mogelijk zijn
zodat de text zal worden gecodeerd als de guess (meestal "WETTERBERICHT")
"""
def CrackLoop(msg, ciph, v1, v2, toplist, savedlist, enigma_list):
    for c1 in range(v1, v2):
        for c2 in range(26):
            for c3 in range(26):
                start_pos = [c1, c2, c3]
                pos_list = []
                for i in range(len(toplist)):
                    temp_list = []
                    for j in range(len(toplist[i])):

                        var = toplist[i][j][1]
                        var1, var2, var3 = Rotator(start_pos[0], start_pos[1], start_pos[2], var)
                        temp_list.append([var1, var2, var3])
                    pos_list.append(temp_list)

                end_list = []
                for k in range(len(toplist)):
                    templist2 = []
                    counter = 0
                    for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        templist = []
                        var = savedlist[k] + j
                        templist.append(var)
                        for i in range(len(toplist[k])):
                            templist.append(toplist[k][i][0]+enigma_list[pos_list[k][i][0]][pos_list[k][i][1]][pos_list[k][i][2]][counter])
                        counter += 1

                        newstr = ""
                        newlist = []
                        bool = True
                        for l in templist:
                            if (l in newlist or l[::-1] in newlist) or (l[0] not in newstr and l[1] not in newstr):
                                newstr += l[0]
                                newstr += l[1]
                                newlist.append(l)
                            else:
                                bool = False
                        if bool:
                            templist2.append(templist)
                    end_list.append(templist2)

                loop(end_list, msg, ciph, start_pos[0],start_pos[1],start_pos[2], start_pos)
        print("Done")


def Crack(msg, ciph):
    """
    In het stuk code hieronder worden het originele bericht en het versleutelde bericht achter elkaar geplakt 
    en wordt gekeken per letter hoevaak deze erin voorkomt.
    """
    msg = msg.upper()
    ciph = ciph.upper()
    msgciph = msg + ciph
    msgciphlist = []
    for i in range(len(msg)):
        msgciphlist.append([msg[i] + ciph[i], i])

    countdict = {}
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        var = msgciph.count(i)
        if var > 0:
            countdict[i] = var
    print(countdict) #vw
    countlist = [i for i in countdict.items()]
    countlist.sort(key=takeSecond, reverse=True)
    final_list = []
    for i in countlist:
        temp_list = []
        for j in msgciphlist:
            if i[0] in j[0]:
                temp_list.append(j)
        final_list.append(temp_list)

    """
    Het programma maakt een lijst met alle versleutelingen. Als het originele stukje tekst bijvoorbeeld "HOI" is en de versleutelde code "BFM"
    zouden de versleutelingen HB, OF en IM zijn. De lijst met versleutelingen is georganiseerd op hoevaak letters in de code voorkomen,
    als R het vaakst in de code voorkomt zal de lijst beginnen met alle versleutelingen waarin een R voorkomt, vervolgens doe je de letter die
    op R na het vaakst voorkomt, etc.
    """
    msgciphlist = []
    msgciphlist.append(final_list[0])
    checklist = []
    for i in final_list[0]:
        checklist.append(i)
    final_list.remove(final_list[0])
    for i in final_list:
        temp_list = []
        for j in i:
            if j not in checklist:
                checklist.append(j)
                temp_list.append(j)
        if temp_list:
            msgciphlist.append(temp_list)


    """
    Maakt 26x26x26 matrix (enigma_list) met door de enigma versleutelde letters A t/m Z. enigma_list[1][0][10] zal vervolgens
    die lijst geven voor rotorinstelling 1, 0, 10.
    """
    enigma_list = []
    for i in range(26):
        temp2_list = []
        for j in range(26):
            temp1_list = []
            for k in range(26):
                temp_list = []
                temp1_list.append(temp_list)
            temp2_list.append(temp1_list)
        enigma_list.append(temp2_list)

    jj = -1
    kk = -1
    for ii in range(17576):
        ii = ii % 26
        if ii == 0:
            jj = (jj + 1) % 26
            if jj == 0:
                kk = (kk + 1) % 26
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            var = enigmaOne(l, rotorI, rotorII, rotorIII, reflectorB, ii, jj, kk, emptydict)
            enigma_list[ii][jj][kk].append(var)

    """
    Het volgende stuk maakt een lijst waarin per letter (bijvoorbeeld de R) de letter die de enigma machine als output zou geven
    wordt gekoppeld aan de voorgaande letters in deze lijst.
    """
    savedlist = []
    toplist = []
    counterdict = {i : 0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    error = 0
    length = len(msgciphlist)
    masterlist = []
    for q in range(len(countlist)):
        masterlist.append(countlist[q][0])
        print(masterlist) #vw

    cnt = -1
    for q in range(length):
        test_list = msgciphlist[q]
        print(test_list) #vw
        bool = True
        test_list = msgciphlist[q]

        print(test_list) #vw
        print(" ") #vw
        print(masterlist)
        while bool:
            cnt += 1
            if len(test_list) > 1:
                if masterlist[cnt] in test_list[0][0] and masterlist[cnt] in test_list[1][0]:
                    bool = False
            if len(test_list) == 1:
                if masterlist[cnt] in test_list[0][0]:
                    bool = False
        for i in test_list:
            if i[0][0] == masterlist[cnt]:
                i[0] = i[0][1]
            else:
                i[0] = i[0][0]
        toplist.append(test_list)
        savedlist.append(masterlist[cnt])
    
    """
    Het volgende stuk start verschillende processen die tegelijkertijd verschillende rotorposities zullen langsgaan met een gegeven lijst
    Hiermee wordt uiteindelijk gekeken of bepaalde instellingen mogelijk zijn.
    """

    process1 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 0, 3, toplist, savedlist, enigma_list))
    process2 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 3, 6, toplist, savedlist, enigma_list))
    process3 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 6, 9, toplist, savedlist, enigma_list))
    process4 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 9, 12, toplist, savedlist, enigma_list))
    process5 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 12, 15, toplist, savedlist, enigma_list))
    process6 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 15, 18, toplist, savedlist, enigma_list))
    process7 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 18, 21, toplist, savedlist, enigma_list))
    process8 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 21, 24, toplist, savedlist, enigma_list))
    process9 = multiprocessing.Process(target=CrackLoop, args=(msg.upper(), ciph.upper(), 24, 26, toplist, savedlist, enigma_list))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()

#=====================================================================================================================
if __name__ == "__main__":
    #Crack("WETTERBERICHT", enigma("WETTERBERICHT", rotorI, rotorII, rotorIII, reflectorB, 1, 9, 10, DictionConvert(["AB","CD","EF","GH","IJ","KL","MN","OP","QR","ST","UV","WX","YZ"])))
    """
    De regel hieronder zorgt ervoor dat het programma de mogelijke rotorinstellingen en schakelbordinstellingen print waarvoor
    het oorspronkelijke bericht ("WETTERBERICHT" in dit voorbeeld) wordt versleuteld als het stukje testcode ("GGNGONFXCVZLX" in dit voorbeeld).
    """
    Crack("WETTERBERICHT", "GGNGONFXCVZLX")
