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

def enigmaOne(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3):

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

    i = alphabet_dict[i]

    i = rotor1list[(i + pos1) % 26]

    i = rotor2list[(i + diff1) % 26]

    i = rotor3list[(i + diff2) % 26]

    i = reflector[(i - pos3) % 26]

    i = rotor3revlist[(i + pos3) % 26]

    i = rotor2revlist[(i - diff2) % 26]

    i = rotor1revlist[(i - diff1) % 26]

    i = alphabet_list[(i - pos1) % 26]

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

def GetMax(dictionary):
    maximum = 0
    maximumletters = []
    maximumletter = ""
    for i in dictionary.keys():
        if dictionary[i] >= maximum:
            if maximumletters and dictionary[maximumletters[0]] != dictionary[i]:
                maximumletters = []
            maximumletter = i
            maximum = dictionary[i]
            maximumletters.append(i)
    return(maximumletters)

def Frequency(word, cipher):
    total = word.upper() + cipher.upper()
    countdict = {}
    for i in total:
        if i not in countdict:
            countdict[i] = 1
        else:
            countdict[i] += 1
    return(GetMax(countdict))

def Analyse(inputlist):
    counter = {}
    for i in inputlist:
        for j in i:
            if j not in counter and j[::-1] not in counter:
                counter[j] = 1
            elif j in counter:
                counter[j] += 1
            elif j[::-1] in counter:
                counter[j[::-1]] += 1

    return(counter)

def Crack(word, cipher):
    word, cipher = word.upper(), cipher.upper()
    frequentlist = Frequency(word, cipher)
    first = frequentlist[0]
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        input = ""
        dictlist = [first + i]
        choicelist = [first + i]
        for j in range(len(word)):
            rotlist = Rotator(0, 0, 0, j)
            input = word[j]
            input1 = cipher[j]
            enigmadict = DictionConvert(dictlist)

            input = enigmaOne(input, rotorI, rotorII, rotorIII, reflectorB, rotlist[0], rotlist[1], rotlist[2])
            input1 = enigmaOne(input1, rotorI, rotorII, rotorIII, reflectorB, rotlist[0], rotlist[1], rotlist[2])
            choicelist.append([input + cipher[j], input1 + word[j]])
        counter = Analyse(choicelist)
        print(counter)

def CrackTest(word, cipher, num1, num2, num3):
    word, cipher = word.upper(), cipher.upper()
    frequentlist = Frequency(word, cipher)
    first = frequentlist[0]
    input = ""
    dictlist = []
    choicelist = []
    for j in range(len(word)):
        rotlist = Rotator(num1, num2, num3, j)
        input = word[j]
        input1 = cipher[j]
        enigmadict = DictionConvert(dictlist)

        input = enigmaOne(input, rotorI, rotorII, rotorIII, reflectorB, rotlist[0], rotlist[1], rotlist[2])
        input1 = enigmaOne(input1, rotorI, rotorII, rotorIII, reflectorB, rotlist[0], rotlist[1], rotlist[2])
        choicelist.append([input + cipher[j], input1 + word[j]])
    counter = Analyse(choicelist)

    testcount = 0
    for i in counter.values():
        if i > 1:
            testcount += i - 1
    return(testcount)

def BruteForce():
    counterdict = {}
    for i in range(26):
        for j in range(26):
            for k in range(26):
                value = CrackTest("WETTERBERICHT", "AYKZCODIAHZUL", i, j, k)
                string = str(i)+" " + str(j)+" " + str(k)
                if value not in counterdict:
                    counterdict[value] = [string]
                else:
                    counterdict[value].append(string)

    countlist = counterdict.keys()
    maximum = max(countlist)
    print(counterdict[maximum])
    print(counterdict[maximum - 1])

if __name__ == "__main__":
    # print(Crack("WETTERBERICHT", "MMUPYUXHCZOID"))
    # print(enigmaOne("B", rotorI, rotorII, rotorIII, reflectorB, 2, 0, 0))
    # print(CrackTest("WETTERBERICHT", "MMUPYUXHCZOID", 0, 0, 0))
    # print(CrackTest("WETTERBERICHT", "TPPDKEFWXANMB", 1, 0, 0))

    BruteForce()
