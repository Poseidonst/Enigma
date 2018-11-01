import multiprocessing
import time

alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_dict = {chr(65+i) : i for i in range(26)}

class ReflectorClass(object): #definieert de reflector

    def __init__(self, listname):
        self.listname = listname

class RotorClass(object): #definieert de rotor

    def __init__(self, listname, revlistname, position, rotortip):  #rotortip is een variabele van het punt waarop de volgende rotor een slag meedraait.
        self.listname = listname
        self.revlistname = revlistname
        self.position = position
        self.rotortip = rotortip

plugdiction = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B",
               "C" : "F", "F" : "C",
               "D" : "G", "G" : "D",
               "E" : "H", "H" : "E",}

plugdiction2 = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B",
               "C" : "F", "F" : "C",
               "D" : "G", "G" : "D",
               "E" : "H", "H" : "E",
               "I" : "N", "N" : "I",
               "J" : "O", "O" : "J",
               "K" : "P", "P" : "K",
               "L" : "Q", "Q" : "L",
               "M" : "R", "R" : "M",}

plugdiction3 = {"A" : "O", "O" : "A",
               "B" : "P", "P" : "B",
               "C" : "Q", "Q" : "C",
               "D" : "R", "R" : "D",
               "E" : "S", "S" : "E",
               "I" : "T", "T" : "I",
               "J" : "U", "U" : "J",
               "K" : "V", "V" : "K",
               "L" : "W", "W" : "L",
               "M" : "X", "X" : "M",}
emptydict = {}

def enigma(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3, plugdictionary):
#userinput is de te coderen tekst; rotor1, rotor2 en rotor3 bepalen de volgorde van de rotors; rotorsetting bepaalt per rotor op welke positie hij start; plugdictionary is het plugboard.
    plugdict = plugdictionary

    output = "" #hierin komt de gecodeerde tekst te staan

    rotor1.position = rotorsetting1 % 26
    rotor2.position = rotorsetting2 % 26
    rotor3.position = rotorsetting3 % 26
    #de "% 26" deelt de rotorsetting door 26 en geeft wat er nog over is, zo blijven de getallen tussen 0 en 25 zodat de getallen in het bereik van de dictionaries vallen

    rotor1list = rotor1.listname
    rotor2list = rotor2.listname
    rotor3list = rotor3.listname

    rotor1revlist = rotor1.revlistname
    rotor2revlist = rotor2.revlistname
    rotor3revlist = rotor3.revlistname

    reflector = reflector.listname

    for i in userinput.upper(): #definieert de posities van de rotors
        pos1 = rotor1.position
        pos2 = rotor2.position
        pos3 = rotor3.position

        diff1 = pos2 - pos1
        diff2 = pos3 - pos2
        #als de rotors ten opzichte van elkaar gedraaid staan komt er een ander resultaat uit dan bij beginstand, diff zorgt binnen onze functie voor dit verschil

        try:
            i = plugdict[i]
        except:
            pass

        i = alphabet_dict[i]

        i = rotor1list[(i + pos1) % 26] #i gaat door rotor1 lijst

        i = rotor2list[(i + diff1) % 26]#i gaat door rotor2 lijst

        i = rotor3list[(i + diff2) % 26]#i gaat door rotor3 lijst

        i = reflector[(i - pos3) % 26]#i gaat door de reflector

        i = rotor3revlist[(i + pos3) % 26]#i gaat terug door rotor3 lijst

        i = rotor2revlist[(i - diff2) % 26]#i gaat terug door rotor2 lijst

        i = rotor1revlist[(i - diff1) % 26]#i gaat terug door rotor1 lijst

        i = alphabet_list[(i - pos1) % 26]
        #pos1 en diff1 compenseren bij de rotors en reflectoren de draaiing

        try:
            i = plugdict[i]
        except:
            pass

        output += i

        rotor1.position = (rotor1.position + 1) % 26 #na elke letter die door de enigma gaat verschuift rotor1, 1 stap
        if rotor1.position == rotor1.rotortip:
            rotor2.position = (rotor2.position + 1) % 26 #als rotor1 de rotortip heeft bereikt verschuift rotor2 1 stap
        if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
            rotor3.position = (rotor3.position + 1) % 26 #als rotor2 verschuift en dan op zijn rotortip komt verschuift rotor3 1 stap

    return(output)

def enigmaOne(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3, plugdict):

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
#de dictionaries voor de rotors en reflector waar i doorheen gaat; de volgorde wordt ligt niet vast.

#-----------------------------------------------------------------------------------------------------------#
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

def analyse(input1, input2, output):
    input1 = list(set(input1))
    state = True
    inputstr1 = ""
    inputstr2 = ""

    for i in input1:
        inputstr1 += i

    for i in input2:
        inputstr2 += i

    for i in inputstr1:
        if i in inputstr2:
            for i in input1:
                for j in inputstr2:
                    if j in i:
                        if i not in input2 and i[::-1] not in input2:
                            state = False
                            break
            break

    if state:
        output.clear()

        for i in input1 + input2:
            if i not in output and i[::-1] not in output:
                output.append(i)

    return(state)

def freq(message, cipher):
    outputdict = {}
    for i in message + cipher:
        if i not in outputdict:
            outputdict[i] = 1
        else:
            outputdict[i] += 1

    outputlist = []
    maximum = max(outputdict.values())
    for i in outputdict.items():
        if i[1] == maximum:
            outputlist.append(i[0])
    if maximum > 1:
        for i in outputdict.items():
            if i[1] == maximum - 1:
                outputlist.append(i[0])
    if maximum > 2:
        for i in outputdict.items():
            if i[1] == maximum - 2:
                outputlist.append(i[0])
    if maximum > 3:
        for i in outputdict.items():
            if i[1] == maximum - 3:
                outputlist.append(i[0])
    if maximum > 4:
        for i in outputdict.items():
            if i[1] == maximum - 4:
                outputlist.append(i[0])
    if maximum > 5:
        for i in outputdict.items():
            if i[1] == maximum - 5:
                outputlist.append(i[0])
    if maximum > 6:
        for i in outputdict.items():
            if i[1] == maximum - 6:
                outputlist.append(i[0])

    defoutputlist = []
    for output in outputlist:
        for i in range(len(message)):
            if message[i] == output and i not in defoutputlist:
                defoutputlist.append(i)
            elif cipher[i] == output and i not in defoutputlist:
                defoutputlist.append(i)
    return(defoutputlist)

def Crack(message, cipher, st1, st2, st3):
    cracklist = []
    blacklist = []
    for j in range(0, len(message)):
        outlist = []
        msg = message[j]
        ciph = cipher[j]
        pos = Rotator(st1, st2, st3, j)

        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            msgi = msg + i
            var = enigmaOne(i, rotorI, rotorII, rotorIII, reflectorB, pos[0], pos[1], pos[2], emptydict)
            ciphvar = ciph + var
            if ((ciph not in msgi and var not in msgi and msg not in ciphvar and i not in ciphvar) or ciphvar == msgi or ciphvar[::-1] == msgi) and ciphvar not in blacklist and ciphvar[::-1] not in blacklist and msgi not in blacklist and msgi[::-1] not in blacklist:
                outlist.append([msgi, ciphvar])
            else:
                blacklist.append(msgi)
                blacklist.append(ciphvar)

        cracklist.append(outlist)

    cracklist2 = []
    frequencelist = freq(message, cipher)

    for i in frequencelist:
        cracklist2.append(cracklist[i])

    cracklist = cracklist2[::1]
    definput = []
    output = []

    for i in cracklist[0]:
        for j in cracklist[1]:
            if analyse(i, j, output):
                input = output[::1]
                for k in cracklist[2]:
                    if analyse(input, k, output):
                        input1 = output[::1]
                        for l in cracklist[3]:
                            if analyse(input1, l, output):
                                input2 = output[::1]
                                for m in cracklist[4]:
                                    if analyse(input2, m, output):
                                        input3 = output[::1]
                                        for n in cracklist[5]:
                                            if analyse(input3, n, output):
                                                input4 = output[::1]
                                                for o in cracklist[6]:
                                                    if analyse(input4, o, output):
                                                        input5 = output[::1]
                                                        for p in cracklist[7]:
                                                            if analyse(input5, p, output):
                                                                input6 = output[::1]
                                                                for q in cracklist[8]:
                                                                    if analyse(input6, q, output):
                                                                        input7 = output[::1]
                                                                        for r in cracklist[9]:
                                                                            if analyse(input7, r, output):
                                                                                input8 = output[::1]
                                                                                for s in cracklist[10]:
                                                                                    if analyse(input8, s, output):
                                                                                        input9 = output[::1]
                                                                                        for t in cracklist[11]:
                                                                                            if analyse(input9, t, output):
                                                                                                input10 = output[::1]
                                                                                                for u in cracklist[12]:
                                                                                                    if analyse(input10, u, output):
                                                                                                        definput = output[::1]
    return(definput)

def CrackLoop(message, cipher, fr, to):
    for i in range(fr, to):
        for j in range(26):
            for k in range(26):
                input = Crack(message, cipher, i, j, k)
                if input:
                    print(input)
                    print(i, j, k)

def CrackMulti(message, cipher):
    process1 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 0, 3))
    process2 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 3, 6))
    process3 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 6, 9))
    process4 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 9, 12))
    process5 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 12, 15))
    process6 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 15, 18))
    process7 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 18, 21))
    process8 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 21, 24))
    process9 = multiprocessing.Process(target=CrackLoop, args=(message.upper(), cipher.upper(), 24, 26))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()



if __name__ == "__main__":
    #print(enigma("WETTERBERICHT", rotorI, rotorII, rotorIII, reflectorB, 12,10,10, plugdiction2))
    CrackMulti("WETTERBERICHT", "RRUKYCXHVWJND")
    # print(freq("WETTERBERICHT", "SCXBJPJADCMOM"))
    # CrackLoop("WETTERBERICHT", "TWDCOAUUOOEDF")
    # Crack("WETTERBERICHT", "RRUKYCXHVWJND", 0, 0, 0)
    # Crack("WETTERBERICHT", "MMUPYUXHCZOID", 0, 0, 0)
    # for i in range(26):
    #     for j in range(26):
    #         for k in range(26):
    #             Crack("WETTERBERICHT", "SCXBJPJADCMOM", i, j, k)
    #             print(i, j, k)
                # print(time.time() - start)
    # print(analyse(['EM', 'RH', "EM"], ['EM', 'RH'], []))
