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

plugdiction = {}

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

        #rotor1.position = (rotor1.position + 1) % 26 #na elke letter die door de enigma gaat verschuift rotor1, 1 stap
        #if rotor1.position == rotor1.rotortip:
            #rotor2.position = (rotor2.position + 1) % 26 #als rotor1 de rotortip heeft bereikt verschuift rotor2 1 stap
        #if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
            #rotor3.position = (rotor3.position + 1) % 26 #als rotor2 verschuift en dan op zijn rotortip komt verschuift rotor3 1 stap

    return(output)

rotorI = RotorClass([alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"], [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9], 0, 17)
rotorII = RotorClass([alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"], [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18], 0, 5)
rotorIII = RotorClass([alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"], [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12], 0, 22)
reflectorB = ReflectorClass([alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"])
reflectorC = ReflectorClass([alphabet_dict[i] for i in "FVPJIAOYEDRZXWGCTKUQSBNMHL"])
#de dictionaries voor de rotors en reflector waar i doorheen gaat; de volgorde wordt ligt niet vast.

test = enigma("B", rotorI, rotorII, rotorIII, reflectorB, 1, 2, 3, plugdiction)

l0 = []
GW = "WETTERBERICHT" #MVAEDUWHFAVPD(0,0,0)
NEE = [ ]
JA = []
input = input("Geef een letter: ")
for i in input:
    woord = i
    n = ""
    l = []
    GL = GW[input.index(i)]
    print(GL)
    count1 = 0
    count2 = 0
    count3 = 0
    countertip = 25

    while count3 < 26:
        count1 = count1 % 26
        count2 = count2 % 26
        count3 = count3 % 26
        if enigma(woord, rotorI, rotorII, rotorIII, reflectorB, count1, count2, count3, plugdiction) != GL:
            NEE.append("nee" + str(count1) + " " + enigma(woord, rotorI, rotorII, rotorIII, reflectorB, count1, count2, count3, plugdiction))
            if count1 == countertip:
                count2 += 1
            elif count2 == countertip:
                count3 += 1
            count1 += 1
        else:
            l0.append("(" + str(count1) + "," + str(count2) + "," + str(count3) + ")" )
            if count3 == 0:
                l0.append("(" + str(count1) + "," + str(count2) + "," + str(count3) + ")" )
                l0.append(count1, count2, count3)
            elif count1 == countertip:
                count2 += 1
            elif count2 == countertip:
                count3 += 1
            count1 += 1

    #n = n + i
    l = n.split(")(")

    if len(l) > 4:
        first = l[0]
        Nfirst = first[1:len(first):]
        l.remove(first)
        last = l[-1]
        Nlast = last[0:len(last)-1:]
        l.remove(last)
        l.append(Nlast)
        l.append(Nfirst)

    print(l0)
    #print(woord)
    print(l)


    #print(len(n))
    #for x in range(0, len(n) / 9):
        #l.append(n[x:x + 8:1])
        #print(l)


#meerdere letters woord: if (count1, count2, count3) van letter 1 == (count1-1, count2, count3) van letter2 (of (count1-1, count2-2, count3))





print(enigma(woord, rotorI, rotorII, rotorIII, reflectorB, 3, 0, 0, plugdiction))
