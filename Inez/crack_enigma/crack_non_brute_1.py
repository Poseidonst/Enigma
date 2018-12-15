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

def cracking_enigma(code, origineel):
    foutlijst = []
    for i in alphabet:
        #eerste letter
        first_list = []
        plugdiction = {}

        first_guess = code[0] + i
        first_resultpair = enigma(first_guess[1], rotorI, rotorII, rotorIII, reflectorB, 0, 0, 0, plugdiction) + origineel[0]
        first_list.append(first_guess)
        first_list.append(first_resultpair)
        #print(first_list)
        plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                       first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0]}
        print("First guess + result:")
        print(plugdiction)


        if code[1] in plugdiction: #tweede letter
            #print("JA")
            second_resultpair = enigma(code[1], rotorI, rotorII, rotorIII, reflectorB, 1, 0, 0, plugdiction) + origineel[1]
            if enigma(code[1], rotorI, rotorII, rotorIII, reflectorB, 1, 0, 0, plugdiction) in plugdiction:
                print("fout: wel_code[1]:")
                foutlijst.append(second_resultpair)
                foutlijst.append(first_resultpair)
                foutlijst.append(first_guess)
                print(foutlijst)
            else:
                print(second_resultpair)
                print("wel_code[1]: plug + second result")
                plugdiction[second_resultpair[0]] = second_resultpair[1]
                plugdiction[second_resultpair[1]] = second_resultpair[0]

                print(plugdiction)



                if code[2] in plugdiction: #derde letter
                    #print("JA")
                    third_resultpair = enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, 2, 0, 0, plugdiction) + origineel[2]
                    if enigma(code[2], rotorI, rotorII, rotorIII, reflectorB, 2, 0, 0, plugdiction) in plugdiction:
                        print("fout: wel_code[1] > wel_code[2]")
                        foutlijst.append(second_resultpair)
                        foutlijst.append(first_resultpair)
                        foutlijst.append(first_guess)
                        foutlijst.append(third_guess)
                        print(foutlijst)
                        #print("AY")

                    else:
                        #print("NAY")
                        print(third_resultpair)
                        print("wel_code[1] > wel_code[2]: plug + third result:")
                        plugdiction[third_resultpair[0]] = third_resultpair[1]
                        plugdiction[third_resultpair[1]] = third_resultpair[0]

                        print(plugdiction)
                        #..................................
                else: #code[2] niet in plug
                    print("wel_code[1] > niet_code[2]")
                    for x in alphabet:
                        plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                                       first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0]}
                        second_guess = code[1] + x
                        second_resultpair = enigma(second_guess[1], rotorI, rotorII, rotorIII, reflectorB, 1, 0, 0, plugdiction) + origineel[1]
                        first_list.append(second_guess)
                        first_list.append(second_resultpair)
                        #print(first_list)
                        plugdiction[second_resultpair[0]] = second_resultpair[1]
                        plugdiction[second_resultpair[1]] = second_resultpair[0]
                        plugdiction[second_guess[0]] = second_guess[1]
                        plugdiction[second_guess[1]] = second_guess[0]
                        print("Plug + second guess en result")
                        print(plugdiction)
                        #................


        else: #tweede letter, code[1] niet in plug
            #print("NEE")
            print("niet_code[1]:")
            for x in alphabet:
                plugdiction = {first_guess[0]:first_guess[1], first_guess[1]:first_guess[0],
                               first_resultpair[0]:first_resultpair[1], first_resultpair[1]:first_resultpair[0]}
                second_guess = code[1] + x
                second_resultpair = enigma(second_guess[1], rotorI, rotorII, rotorIII, reflectorB, 1, 0, 0, plugdiction) + origineel[1]
                first_list.append(second_guess)
                first_list.append(second_resultpair)
                #print(first_list)
                plugdiction[second_resultpair[0]] = second_resultpair[1]
                plugdiction[second_resultpair[1]] = second_resultpair[0]
                plugdiction[second_guess[0]] = second_guess[1]
                plugdiction[second_guess[1]] = second_guess[0]
                print("Plug + second guess en result")
                print(plugdiction)


print(cracking_enigma("MPACLUWTFAUPD" ,"WETTERBERICHT"))
