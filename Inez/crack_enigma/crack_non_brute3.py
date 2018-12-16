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

#na de streep begint het cracking gedeelte
#======================================================================================================================================
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listname = ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ', 'EE', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FF', 'FG', 'FH', 'FI', 'FJ', 'FK', 'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GG', 'GH', 'GI', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'HH', 'HI', 'HJ', 'HK', 'HL', 'HM', 'HN', 'HO', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY', 'HZ', 'II', 'IJ', 'IK', 'IL', 'IM', 'IN', 'IO', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IU', 'IV', 'IW', 'IX', 'IY', 'IZ', 'JJ', 'JK', 'JL', 'JM', 'JN', 'JO', 'JP', 'JQ', 'JR', 'JS', 'JT', 'JU', 'JV', 'JW', 'JX', 'JY', 'JZ', 'KK', 'KL', 'KM', 'KN', 'KO', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX', 'KY', 'KZ', 'LL', 'LM', 'LN', 'LO', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NN', 'NO', 'NP', 'NQ', 'NR', 'NS', 'NT', 'NU', 'NV', 'NW', 'NX', 'NY', 'NZ', 'OO', 'OP', 'OQ', 'OR', 'OS', 'OT', 'OU', 'OV', 'OW', 'OX', 'OY', 'OZ', 'PP', 'PQ', 'PR', 'PS', 'PT', 'PU', 'PV', 'PW', 'PX', 'PY', 'PZ', 'QQ', 'QR', 'QS', 'QT', 'QU', 'QV', 'QW', 'QX', 'QY', 'QZ', 'RR', 'RS', 'RT', 'RU', 'RV', 'RW', 'RX', 'RY', 'RZ', 'SS', 'ST', 'SU', 'SV', 'SW', 'SX', 'SY', 'SZ', 'TT', 'TU', 'TV', 'TW', 'TX', 'TY', 'TZ', 'UU', 'UV', 'UW', 'UX', 'UY', 'UZ', 'VV', 'VW', 'VX', 'VY', 'VZ', 'WW', 'WX', 'WY', 'WZ', 'XX', 'XY', 'XZ', 'YY', 'YZ', 'ZZ']
def cracking_enigma(code, origineel, count1, count2, count3):
    accept_list = listname
    foutlijst = []
    foutlijst_enkel = []
    for i in alphabet:
        #eerste letter

        first_list = []
        plugdiction = {}

        first_guess = code[0] + i
        first_resultpair = enigma(first_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1, count2, count3, plugdiction) + origineel[0]
        first_list.append(first_guess)
        first_list.append(first_resultpair)

        plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                       first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0]}

        if code[1] in plugdiction: #W
            second_resultpair = enigma(code[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 1, count2, count3, plugdiction) + origineel[1] #count1 +=1
            if enigma(code[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 1, count2, count3, plugdiction) in plugdiction:

                foutlijst.append(second_resultpair)
                foutlijst.append(first_resultpair)
                foutlijst.append(first_guess)

            else: #W

                #print("wel_code[1]: plug + second result")
                plugdiction[second_resultpair[0]] = second_resultpair[1]
                plugdiction[second_resultpair[1]] = second_resultpair[0]

                #print(plugdiction)

                if code[2] in plugdiction: #WW

                    third_resultpair = enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                    if enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) in plugdiction:
                        #("fout: wel_code[1] > wel_code[2]")
                        foutlijst.append(second_resultpair)
                        foutlijst.append(first_resultpair)
                        foutlijst.append(first_guess)
                        foutlijst.append(third_resultpair)

                    else: #WW

                        plugdiction[third_resultpair[0]] = third_resultpair[1]
                        plugdiction[third_resultpair[1]] = third_resultpair[0]

                        if code[3] in plugdiction: #WWW
                            #print("JA")
                            fourth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                            if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:
                                #("fout: wel_code[1] > wel_code[2]")
                                foutlijst.append(second_resultpair)
                                foutlijst.append(first_resultpair)
                                foutlijst.append(first_guess)
                                foutlijst.append(third_resultpair)
                                foutlijst.append(fourth_resultpair)

                            else: #WWW

                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                if code[4] in plugdiction: #WWWW
                                    fifth_resultpair = enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) + origineel[4]
                                    if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) in plugdiction:
                                        #("fout: wel_code[1] > wel_code[2]")
                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)
                                        foutlijst.append(fifth_resultpair)

                                    else: #WWWW

                                        plugdiction[fifth_resultpair[0]] = fifth_resultpair[1]
                                        plugdiction[fifth_resultpair[1]] = fifth_resultpair[0]

                                        #..................................
                                else: #WWWN
                                    pass #safe
                        else: #WWN
                            pass #safe
                            for x in alphabet:
                                plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                               first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0],
                                               second_resultpair[0]:second_resultpair[1], second_resultpair[1]:second_resultpair[0]}

                                fourth_guess = code[2] + x
                                fourth_resultpair = enigma(fourth_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                                first_list.append(fourth_guess)
                                first_list.append(fourth_resultpair)

                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]
                                plugdiction[fourth_guess[0]] = fourth_guess[1]
                                plugdiction[fourth_guess[1]] = fourth_guess[0]
                                if code[4] in plugdiction: #WWNW
                                    fifth_resultpair = enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) + origineel[4]
                                    if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) in plugdiction:

                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(fourth_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)

                                    else: #WWNW

                                        plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                        plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                    #..................................

                                else: #WWNN
                                    pass #safe

                else: #WN
                    #("wel_code[1] > niet_code[2]")
                    for x in alphabet:
                        plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                       first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0],
                                       second_resultpair[0]:second_resultpair[1], second_resultpair[1]:second_resultpair[0]}
                        third_guess = code[1] + x
                        third_resultpair = enigma(third_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 1, count2, count3, plugdiction) + origineel[1]
                        first_list.append(third_guess)
                        first_list.append(third_resultpair)

                        plugdiction[third_resultpair[0]] = third_resultpair[1]
                        plugdiction[third_resultpair[1]] = third_resultpair[0]
                        plugdiction[third_guess[0]] = third_guess[1]
                        plugdiction[third_guess[1]] = third_guess[0]

                        if code[3] in plugdiction: #WNW

                            fourth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                            if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:
                                #print("fout: wel_code[1] > niet_code[2]")
                                foutlijst.append(third_resultpair)
                                foutlijst.append(first_resultpair)
                                foutlijst.append(first_guess)
                                foutlijst.append(third_guess)
                                foutlijst.append(third_resultpair)
                                foutlijst.append(fourth_resultpair)

                            else:
                                #WNW
                                plugdiction[third_resultpair[0]] = third_resultpair[1]
                                plugdiction[third_resultpair[1]] = third_resultpair[0]

                                if code[4] in plugdiction: #WNWW
                                    #print("JA")
                                    fifth_resultpair = enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) + origineel[4]
                                    if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) in plugdiction:
                                        #("fout: wel_code[1] > wel_code[2]")
                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(third_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)
                                        foutlijst.append(fifth_resultpair)

                                    else: #WNWW

                                        plugdiction[fifth_resultpair[0]] = fifth_resultpair[1]
                                        plugdiction[fifth_resultpair[1]] = fifth_resultpair[0]

                                        if code[5] in plugdiction: #WNWWW
                                            sixth_resultpair = enigma(code[5], rotorI, rotorII, rotorIII, reflectorB, count1 + 5, count2, count3, plugdiction) + origineel[5]
                                            if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 5, count2, count3, plugdiction) in plugdiction:
                                                #("fout: wel_code[1] > wel_code[2]")
                                                foutlijst.append(second_resultpair)
                                                foutlijst.append(first_resultpair)
                                                foutlijst.append(first_guess)
                                                foutlijst.append(third_guess)
                                                foutlijst.append(third_resultpair)
                                                foutlijst.append(fourth_resultpair)
                                                foutlijst.append(fifth_resultpair)
                                                foutlijst.append(sixth_resultpair)

                                            else:

                                                plugdiction[fifth_resultpair[0]] = fifth_resultpair[1]
                                                plugdiction[fifth_resultpair[1]] = fifth_resultpair[0]

                                                #..................................
                                        else: #WNWWN
                                            pass #safe
                                else: #WNWN
                                    pass #safe
                                    for x in alphabet:
                                        plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                                       first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0],
                                                       second_resultpair[0]:second_resultpair[1], second_resultpair[1]:second_resultpair[0],
                                                       third_resultpair[0]:third_resultpair[1], third_resultpair[1]:third_resultpair[0],}

                                        fifth_guess = code[3] + x
                                        fifth_resultpair = enigma(fifth_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                                        first_list.append(fifth_guess)
                                        first_list.append(fifth_resultpair)

                                        plugdiction[fifth_resultpair[0]] = fifth_resultpair[1]
                                        plugdiction[fifth_resultpair[1]] = fifth_resultpair[0]
                                        plugdiction[fifth_guess[0]] = fifth_guess[1]
                                        plugdiction[fifth_guess[1]] = fifth_guess[0]
                                        if code[4] in plugdiction: #WNNWW
                                            sixth_resultpair = enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) + origineel[4]
                                            if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) in plugdiction:

                                                foutlijst.append(second_resultpair)
                                                foutlijst.append(first_resultpair)
                                                foutlijst.append(third_guess)
                                                foutlijst.append(first_guess)
                                                foutlijst.append(third_resultpair)
                                                foutlijst.append(fifth_guess)
                                                foutlijst.append(fifth_resultpair)
                                                foutlijst.append(sixth_resultpair)

                                            else: #WWNWW

                                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                            #..................................
                                        else: #WNNN
                                            pass #safe
                        else: #WNN
                            pass #safe
                            for x in alphabet:
                                plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                               first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0],
                                               second_resultpair[0]:second_resultpair[1], second_resultpair[1]:second_resultpair[0],
                                               third_guess[0]:third_guess[1], third_guess[1]:third_guess[0],
                                               third_resultpair[0]:third_resultpair[1], third_resultpair[1]:third_resultpair[0]}

                                fourth_guess = code[2] + x
                                fourth_resultpair = enigma(fourth_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                                first_list.append(fourth_guess)
                                first_list.append(fourth_resultpair)

                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]
                                plugdiction[fourth_guess[0]] = fourth_guess[1]
                                plugdiction[fourth_guess[1]] = fourth_guess[0]
                                if code[3] in plugdiction: #WNNW
                                    fifth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                                    if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:

                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(fourth_guess)
                                        foutlijst.append(third_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)
                                        foutlijst.append(fifth_resultpair)

                                    else: #WNNW

                                        plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                        plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                    #..................................

                                else: #WNNN
                                    pass #safe


        else: #N
            for x in alphabet:
                plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                               first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0]}
                second_guess = code[1] + x
                second_resultpair = enigma(second_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 1, count2, count3, plugdiction) + origineel[1]
                first_list.append(second_guess)
                first_list.append(second_resultpair)
                plugdiction[second_resultpair[0]] = second_resultpair[1]
                plugdiction[second_resultpair[1]] = second_resultpair[0]
                plugdiction[second_guess[0]] = second_guess[1]
                plugdiction[second_guess[1]] = second_guess[0]

                if code[2] in plugdiction: #NW
                    third_resultpair = enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                    if enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) in plugdiction:
                        #("fout:niet_code[1] > wel_code[2]")
                        foutlijst.append(second_resultpair)
                        foutlijst.append(first_resultpair)
                        foutlijst.append(first_guess)
                        foutlijst.append(second_guess)
                        foutlijst.append(third_resultpair)

                    else:
                        #("niet_code[1] > wel_code[2]: plug + third result:")
                        plugdiction[third_resultpair[0]] = third_resultpair[1]
                        plugdiction[third_resultpair[1]] = third_resultpair[0]

                        if code[3] in plugdiction: #NWW
                            #print("JA")
                            fourth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                            if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:
                                #("fout: wel_code[1] > wel_code[2]")
                                foutlijst.append(second_resultpair)
                                foutlijst.append(first_resultpair)
                                foutlijst.append(first_guess)
                                foutlijst.append(second_guess)
                                foutlijst.append(third_resultpair)
                                foutlijst.append(fourth_resultpair)

                            else:

                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                if code[4] in plugdiction: #vijfde letter
                                    fifth_resultpair = enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) + origineel[4]
                                    if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) in plugdiction:
                                        #("fout: wel_code[1] > wel_code[2]")
                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(second_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)
                                        foutlijst.append(fifth_resultpair)

                                    else:

                                        plugdiction[fifth_resultpair[0]] = fifth_resultpair[1]
                                        plugdiction[fifth_resultpair[1]] = fifth_resultpair[0]

                                        #..................................
                        else: #NWN

                            for x in alphabet:
                                plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                               first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0],
                                               second_resultpair[0]:second_resultpair[1], second_resultpair[1]:second_resultpair[0],
                                               second_guess[0]:second_guess[1], second_guess[1]:second_guess[0],
                                               third_resultpair[0]:third_resultpair[1], third_resultpair[1]:third_resultpair[0]}

                                fourth_guess = code[2] + x
                                fourth_resultpair = enigma(fourth_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                                first_list.append(fourth_guess)
                                first_list.append(fourth_resultpair)

                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]
                                plugdiction[fourth_guess[0]] = fourth_guess[1]
                                plugdiction[fourth_guess[1]] = fourth_guess[0]
                                if code[3] in plugdiction: #WNNW
                                    fourth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                                    if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:

                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(fourth_guess)
                                        foutlijst.append(second_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)

                                    else: #WNNW

                                        plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                        plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                    #..................................
                else: #NN
                    for x in alphabet:

                        plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                       first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0]}
                        third_guess = code[2] + x
                        third_resultpair = enigma(third_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                        first_list.append(third_guess)
                        first_list.append(third_resultpair)

                        plugdiction[third_resultpair[0]] = third_resultpair[1]
                        plugdiction[third_resultpair[1]] = third_resultpair[0]
                        plugdiction[third_guess[0]] = third_guess[1]
                        plugdiction[third_guess[1]] = third_guess[0]
                        #("niet_code[1] > niet_code[2]: Plug + third guess en result")

                        if code[2] in plugdiction: #NNW

                            third_resultpair = enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                            if enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) in plugdiction:
                                #("fout: niet_code[1] > niet_code[2]")
                                foutlijst.append(second_resultpair)
                                foutlijst.append(first_resultpair)
                                foutlijst.append(first_guess)
                                foutlijst.append(second_guess)
                                foutlijst.append(third_guess)
                                foutlijst.append(third_resultpair)

                            else:

                                #("wel_code[1] > niet_code[2]: plug + third result:")
                                plugdiction[third_resultpair[0]] = third_resultpair[1]
                                plugdiction[third_resultpair[1]] = third_resultpair[0]

                                if code[3] in plugdiction: #NNWW
                                    #print("JA")
                                    fourth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                                    if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:
                                        #("fout: wel_code[1] > wel_code[2]")
                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(second_guess)
                                        foutlijst.append(third_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)

                                    else:

                                        plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                        plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                        if code[4] in plugdiction: #vijfde letter
                                            print(plugdiction)

                                            fifth_resultpair = enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) + origineel[4]
                                            if enigma(code[4], rotorI, rotorII, rotorIII, reflectorB, count1 + 4, count2, count3, plugdiction) in plugdiction:
                                                #("fout: wel_code[1] > wel_code[2]")
                                                foutlijst.append(second_resultpair)
                                                foutlijst.append(first_resultpair)
                                                foutlijst.append(first_guess)
                                                foutlijst.append(third_resultpair)
                                                foutlijst.append(fourth_resultpair)
                                                foutlijst.append(fifth_resultpair)

                                            else:

                                                plugdiction[fifth_resultpair[0]] = fifth_resultpair[1]
                                                plugdiction[fifth_resultpair[1]] = fifth_resultpair[0]

                                                #..................................
                                else: #NNWN
                                    pass #safe
                        else: #NNN
                            for x in alphabet:
                                plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                               first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0],
                                               second_resultpair[0]:second_resultpair[1], second_resultpair[1]:second_resultpair[0],
                                               second_guess[0]:second_guess[1], second_guess[1]:second_guess[0],
                                               third_guess[0]:third_guess[1], third_guess[1]:third_guess[0],
                                               third_resultpair[0]:third_resultpair[1], third_resultpair[1]:third_resultpair[0]}

                                fourth_guess = code[2] + x
                                fourth_resultpair = enigma(fourth_guess[1], rotorI, rotorII, rotorIII, reflectorB, count1 + 2, count2, count3, plugdiction) + origineel[2]
                                first_list.append(fourth_guess)
                                first_list.append(fourth_resultpair)

                                plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]
                                plugdiction[fourth_guess[0]] = fourth_guess[1]
                                plugdiction[fourth_guess[1]] = fourth_guess[0]
                                if code[3] in plugdiction: #WNNW
                                    fourth_resultpair = enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) + origineel[3]
                                    if enigma(code[3], rotorI, rotorII, rotorIII, reflectorB, count1 + 3, count2, count3, plugdiction) in plugdiction:

                                        foutlijst.append(second_resultpair)
                                        foutlijst.append(first_resultpair)
                                        foutlijst.append(first_guess)
                                        foutlijst.append(fourth_guess)
                                        foutlijst.append(second_guess)
                                        foutlijst.append(third_guess)
                                        foutlijst.append(third_resultpair)
                                        foutlijst.append(fourth_resultpair)

                                    else: #WNNW

                                        plugdiction[fourth_resultpair[0]] = fourth_resultpair[1]
                                        plugdiction[fourth_resultpair[1]] = fourth_resultpair[0]

                                    #..................................
                                else: #WNNN
                                    pass #safe


        for i in foutlijst:
            if i not in foutlijst_enkel:
                foutlijst_enkel.append(i)
        # print("F enkel:")
        print("fout_list: ")
        print(foutlijst_enkel)
        for x in foutlijst_enkel:
            for i in accept_list:
                if x==i:
                    accept_list.remove(i)
                elif x[::-1]==i:
                    accept_list.remove(i)

        #print(len(accept_list))
        #print(accept_list)
        reverse_accept_list = accept_list[::-1]
        #print(reverse_accept_list)

        # eind_lijst = []
        #
        # for p in reverse_accept_list:
        #     gekoppelde_letters = []
        #     for j in gekoppelde_letters:
        #         print(i)
        #
        #         if p[0] != j and p[1] != j:
        #             gekoppelde_letters.append(p[0])
        #             gekoppelde_letters.append(p[1])
        #             eind_lijst.append(i)
        #         print(gekoppelde_letters)
        #
        #         return
        #
        # print(eind_lijst)
foutlijst_uit = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabet:
    for j in alphabet:
        for k in alphabet:

            if alphabet.index(i) != 11 and alphabet.index(i) != 12 and alphabet.index(i) != 13 and alphabet.index(i) != 14 and alphabet.index(i) != 15 and alphabet.index(i) != 16:
                print(i)
                # print(j)
                # print(k)
                merp = (enigma("WETTERBERICHT", rotorI, rotorII, rotorIII, reflectorB, alphabet.index(i), alphabet.index(j), 0, plugdiction))
                print(cracking_enigma( merp ,"WETTERBERICHT", alphabet.index(i), alphabet.index(j), 0))
                for x in cracking_enigma( merp ,"WETTERBERICHT", alphabet.index(i), alphabet.index(j), 0):
                    foutlijst_uit.append(x)
print(foutlijst_uit)
