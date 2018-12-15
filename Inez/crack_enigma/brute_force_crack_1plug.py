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

        rotor1.position = (rotor1.position + 1) % 26 #na elke letter die door de enigma gaat verschuift rotor1, 1 stap
        if rotor1.position == rotor1.rotortip:
            rotor2.position = (rotor2.position + 1) % 26 #als rotor1 de rotortip heeft bereikt verschuift rotor2 1 stap
        if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
            rotor3.position = (rotor3.position + 1) % 26 #als rotor2 verschuift en dan op zijn rotortip komt verschuift rotor3 1 stap

    return(output)

rotorI = RotorClass([alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"], [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9], 0, 17)
rotorII = RotorClass([alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"], [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18], 0, 5)
rotorIII = RotorClass([alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"], [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12], 0, 22)
reflectorB = ReflectorClass([alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"])
reflectorC = ReflectorClass([alphabet_dict[i] for i in "FVPJIAOYEDRZXWGCTKUQSBNMHL"])

#hier begint crack_enigma:
import numpy as np
import numba
from numba import jit


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#GW = "WETTERBERICHT" #MVAEDUWHFAVPD(0,0,0)
NEE = [ ]
JA = []
# input = input("Geef een letter: ")
listname = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FG', 'FH', 'FI', 'FJ', 'FK', 'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GH', 'GI', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'HI', 'HJ', 'HK', 'HL', 'HM', 'HN', 'HO', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY', 'HZ', 'IJ', 'IK', 'IL', 'IM', 'IN', 'IO', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IU', 'IV', 'IW', 'IX', 'IY', 'IZ', 'JK', 'JL', 'JM', 'JN', 'JO', 'JP', 'JQ', 'JR', 'JS', 'JT', 'JU', 'JV', 'JW', 'JX', 'JY', 'JZ', 'KL', 'KM', 'KN', 'KO', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX', 'KY', 'KZ', 'LM', 'LN', 'LO', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NO', 'NP', 'NQ', 'NR', 'NS', 'NT', 'NU', 'NV', 'NW', 'NX', 'NY', 'NZ', 'OP', 'OQ', 'OR', 'OS', 'OT', 'OU', 'OV', 'OW', 'OX', 'OY', 'OZ', 'PQ', 'PR', 'PS', 'PT', 'PU', 'PV', 'PW', 'PX', 'PY', 'PZ', 'QR', 'QS', 'QT', 'QU', 'QV', 'QW', 'QX', 'QY', 'QZ', 'RS', 'RT', 'RU', 'RV', 'RW', 'RX', 'RY', 'RZ', 'ST', 'SU', 'SV', 'SW', 'SX', 'SY', 'SZ', 'TU', 'TV', 'TW', 'TX', 'TY', 'TZ', 'UV', 'UW', 'UX', 'UY', 'UZ', 'VW', 'VX', 'VY', 'VZ', 'WX', 'WY', 'WZ', 'XY', 'XZ', 'YZ']


def crack_enigma(input, GW):
    %timeit crack_enigma(input,GW)
    for plug in listname:
        plugdiction = { plug[0] : plug[1],
                        plug[1] : plug[0]}
        #print(plugdiction)

        for i in input:
            Lijst_eerste = []
            if input.index(i) == 0:
                count1 = 0
                count2 = 0
                count3 = 0
                countertip = 25
                while count3 < 26:
                     count1 = count1 % 26
                     count2 = count2 % 26

                     if enigma(i, rotorI, rotorII, rotorIII, reflectorB, count1, count2, count3, plugdiction) == GW[0]:
                         Lijst_eerste.append(str(count1) + "," + str(count2) + "," + str(count3))
                         if count1 == countertip:
                             count2 += 1
                         elif count2 == countertip:
                             count3 += 1
                             count2 = 0
                         #print(count3)

                     else:
                         if count1 == countertip:
                             count2 += 1
                         elif count2 == countertip:
                             count3 += 1
                             count2 = 0
                     #print(count3)
                     count1 += 1
                WEL = []
                #print(Lijst_eerste)
                for n in Lijst_eerste:
                    #print(n)
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[1], rotorI, rotorII, rotorIII, reflectorB, (count1 + 1) % 26, count2, count3, plugdiction) == GW[1] or enigma(input[1], rotorI, rotorII, rotorIII, reflectorB, (count1 + 1) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[1]:
                         WEL.append(n)
                #print(WEL)
                WEL2 = []
                for n in WEL:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[2], rotorI, rotorII, rotorIII, reflectorB, (count1 + 2) % 26, count2, count3, plugdiction) == GW[2] or enigma(input[2], rotorI, rotorII, rotorIII, reflectorB, (count1 + 2) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[2]:
                         WEL2.append(n)
                #print(WEL2)

                WEL3 = []
                for n in WEL2:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[3], rotorI, rotorII, rotorIII, reflectorB, (count1 + 3) % 26, count2, count3, plugdiction) == GW[3] or enigma(input[3], rotorI, rotorII, rotorIII, reflectorB, (count1 + 3) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[3]:
                         WEL3.append(n)
                #print(WEL3)

                WEL4 = []
                for n in WEL3:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[4], rotorI, rotorII, rotorIII, reflectorB, (count1 + 4) % 26, count2, count3, plugdiction) == GW[4] or enigma(input[4], rotorI, rotorII, rotorIII, reflectorB, (count1 + 4) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[4]:
                         WEL4.append(n)

                WEL5 = []
                for n in WEL4:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[5], rotorI, rotorII, rotorIII, reflectorB, (count1 + 5) % 26, count2, count3, plugdiction) == GW[5] or enigma(input[5], rotorI, rotorII, rotorIII, reflectorB, (count1 + 5) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[5]:
                         WEL5.append(n)
                WEL6 = []
                for n in WEL5:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[6], rotorI, rotorII, rotorIII, reflectorB, (count1 + 6) % 26, count2, count3, plugdiction) == GW[6] or enigma(input[6], rotorI, rotorII, rotorIII, reflectorB, (count1 + 6) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[6]:
                         WEL6.append(n)
                WEL7 = []
                for n in WEL6:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[7], rotorI, rotorII, rotorIII, reflectorB, (count1 + 7) % 26, count2, count3, plugdiction) == GW[7] or enigma(input[7], rotorI, rotorII, rotorIII, reflectorB, (count1 + 7) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[7]:
                         WEL7.append(n)
                WEL8 = []
                for n in WEL7:
                    if n[1] == ",":
                        count1 = n[0]
                        if n[3] == ",":
                            count2 = n[2]
                            if len(n) == 5:
                                count3 = n[4]
                            else:
                                count3 = n[4:6]
                        elif n[4] == ",":
                            count2 = n[2:4]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]

                    elif n[2] == ",":
                        count1 = n[0:2]
                        if n[4] == ",":
                            count2 = n[3]
                            if len(n) == 6:
                                count3 = n[5]
                            else:
                                count3 = n[5:7]
                        elif n[5] == ",":
                            count2 = n[3:5]
                            if len(n) == 7:
                                count3 = n[6]
                            else:
                                count3 = n[6:8]
                    count1 = int(count1)
                    count2 = int(count2)
                    count3 = int(count3)
                    # print(count1)
                    # print(count2)
                    # print(count3)
                    if enigma(input[8], rotorI, rotorII, rotorIII, reflectorB, (count1 + 8) % 26, count2, count3, plugdiction) == GW[8] or enigma(input[8], rotorI, rotorII, rotorIII, reflectorB, (count1 + 8) % 26, (count2 + 1) % 26, count3, plugdiction) == GW[8]:
                         WEL8.append(n)
                if WEL8 != []:
                    print(WEL8)
                    print(plug)

print(crack_enigma("CQACPIPULSTMM", "WETTERBERICHT"))
