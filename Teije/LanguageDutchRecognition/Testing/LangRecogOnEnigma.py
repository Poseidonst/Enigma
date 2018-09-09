alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_dict = {chr(65+i) : i for i in range(26)}

rotor_I_list = [alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
rotorI_reversed_list = [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9]

rotor_II_list = [alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotorII_reversed_list = [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18]

rotor_III_list = [alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
rotorIII_reversed_list = [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12]

reflector_B_list = [alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]

def reverser(listname):                             #Function that can be used to make the reversed rotor of any rotor you want.
    reversed = []
    for i in alphabet_list:
        for j in listname:
            if i == alphabet_list[j]:
                reversed.append(listname.index(j))
    return(reversed)

class ReflectorClass(object):

    def __init__(self, listname, name):
        self.listname = listname
        self.name = name

class RotorClass(object):

    def __init__(self, listname, revlistname, name, position, rotortip):  #rotortip is a variable at which place the rotor let's the next rotor turn
        self.listname = listname
        self.name = name
        self.position = position
        self.rotortip = rotortip
        self.revlistname = revlistname

    def defswitch(self, places):
        while places < 0:               #This way it works with negative list as well
            places = places + 26
        while places > 26:
            places = places - 26       #Switches and stays at that position
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
            self.revlistname += [self.revlistname.pop(0)]
            self.position += 1
            if self.position == 27:
                self.position = 1
        return (self.listname)

    def switch1(self):
        self.listname += [self.listname.pop(0)]
        self.revlistname += [self.revlistname.pop(0)]
        self.position += 1
        if self.position == 27:
            self.position = 1
        return (self.listname)

    def reset(self):                    #Resets back to starting position
        places = 26 - self.position
        for i in range(0, places):
            self.listname += [self.listname.pop(0)]
            self.revlistname += [self.revlistname.pop(0)]
        self.position = 0

def get_difference(rotor1, rotor2):
    difference = rotor2.position - rotor1.position
    return(difference)

def switch_rotors(rotor1, rotor2, rotor3):
    rotor1.switch1()
    if rotor1.position == rotor1.rotortip:
        rotor2.switch1()
    if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
        rotor3.switch1()

plugdiction = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B"}

def plugboard(input, plugdict):
    if input in plugdict:
        output = plugdict[input]
    else:
        output = input
    return(output)

def enigma(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3):             #userinput is the text to code, rotorsetting1 is the rotorposition of first rotor, and rotorsetting2 for the second rotor

    userinputlist = [i.upper() for i in userinput]
    codedlist = []

    rotor1.defswitch(rotorsetting1)
    rotor2.defswitch(rotorsetting2)
    rotor3.defswitch(rotorsetting3)

    for i in userinputlist:

        i = plugboard(i, plugdiction)                       #Through plugboard

        i = alphabet_dict[i]                                #From touchpress through rotor 1
        i = rotor1.listname[i]

        diff = get_difference(rotor1, rotor2)               #From rotor1 through rotor2
        i += diff
        i = rotor2.listname[i - rotor2.position]

        diff = get_difference(rotor2, rotor3)               #From rotor2 through rotor3
        i += diff
        i = rotor3.listname[i - rotor3.position]

        i = reflector.listname[i - rotor3.position]        #From rotor3 through reflector

        i = rotor3.revlistname[i]                           #From reflector back through rotor 3

        diff = get_difference(rotor3, rotor2)               #From rotor 3 back through rotor 2
        i += diff
        i = rotor2.revlistname[i - rotor2.position]

        diff = get_difference(rotor2, rotor1)               #From rotor 2 back through rotor 1
        i += diff
        i = rotor1.revlistname[i - rotor1.position]

        i = i - rotor1.position                             #From rotor 1 back through the output

        i = alphabet_list[i]                                #Through plugboard
        i = plugboard(i, plugdiction)

        codedlist.append(i)
        switch_rotors(rotor1, rotor2, rotor3)

    rotor1.reset()
    rotor2.reset()
    rotor3.reset()

    return("".join(codedlist))

rotorI = RotorClass(rotor_I_list, rotorI_reversed_list, "Rotor I", 0, 17)
rotorII = RotorClass(rotor_II_list, rotorII_reversed_list, "Rotor II", 0, 5)
rotorIII = RotorClass(rotor_III_list, rotorIII_reversed_list, "Rotor III", 0, 22)
reflectorB = ReflectorClass(reflector_B_list, "B")
def LangRecog(input):

    def FileReader(filename):
        try:
            with open(filename, "r") as reader:
                inputsent = reader.read()
        except:
            inputsent = filename.lower()

        return(inputsent)

    def RatioKlinkCheck(filename):

        inputsent = FileReader(filename)                    #Reads from the file and stores it in inputsent
        klcount = 0                                         #Variable that counts the amount of klinkers
        medklcount = 0                                      #Variable that counts the amount of medeklinkers

        for i in inputsent:                                 #Iterates through each item in the inputsent
            if i.isalpha():                                 #Checks if item is a letter
                if i in "aeoui":                            #If item is a klinker it adds one to the klinkercount
                    klcount += 1
                else:                                       #Else it must be a medeklinker and adds one to the medeklinkercount
                    medklcount += 1
        try:
            ratio = klcount / medklcount                    #Calculates the ratio between klinkers and medeklinkers which is unique for each language
        except:
            ratio = 0
        return(ratio)

    def CheckMedklink(filename):
        inputsent = FileReader(filename)                    #Reads all the items from a file or string and stores it in inputsent

        splitlist = inputsent.split(" ")                    #Removes spaces from the sentence
        inputsent = "".join(splitlist)

        counter = 0                                         #Counter variable which counts the amount of medeklinker streaks more than 6
        streak = 0                                          #Counter variable which counts the streak of medeklinkers in a part of the text

        for i in inputsent:                                 #Iterates through each letter of the message
            if i.isalpha():                                 #Checks if the letter is indeed a letter and not a space or punctuation e.g.
                if i in "aeoui":                            #If the letter is a klinker it sets the streak counter to 0
                    streak = 0
                else:                                       #If the letter is a medeklinker it adds 1 to the streak counter
                    streak += 1
            if streak > 6:                                  #If the streak counter is greater than 6 it will add 1 to the counter
                counter += 1

        ratio = counter/len(inputsent)                      #The counter is devided by the amount of letters in the text, this way the length of the text doesn't matter for the output
        return(ratio)

    def CheckCommComb(inputsent):                           #The program can take any list it wants to check for the combinations, and thus this can also be used for 2 letter combination or 4 letter combinations
        count = 0
        common = "ing ver sch ter ste tie cht der ers ere aar ren eid nde ngs and ten ent ens eri erk rij oor ati hei gen est end eli ele rin ken sta ond lin den str aan nge eer nst ker len tel ach nte lij ege raa ijk enb erb ant gel del ena ier erd ede pro eve uit aal men lan wer per env ist aat erv eld art nin cha ger era tra sti iek ven tin rst eno eni pen din eke erg uur roe rde enk eel ite ert lie rie sto ont het een die dat wie wat hoe"
        commonlist = common.split(" ")                      #Makes a list of the most common triplets and some 3 letter common words like "het, wat, wie, hoe, een"

        inputsent = FileReader(inputsent)

        inputlist = inputsent.split(" ")                    #Removes spaces from the input sentence
        inputsent = "".join(inputlist)

        for i in commonlist:                                #Iterates through all the common triplets
            if i in inputsent.lower():                      #If triplet is in the inputsent it will continue
                count += inputsent.lower().count(i)         #In this parts it then counts how many times the triplet is in the text and adds the amount to a counter

        outcome = count/len(inputsent)                      #Here is the total count devided by the length of the message
        return(outcome)                                     #Outcome is usually for Dutch a constant as it devides by the length of the message

#=====================================================================#

    points = 0

    input = FileReader(input)
    inputlist = []
    for i in input:
        if i.isalpha():
            inputlist.append(i)
    input = "".join(inputlist)                              #Converts the initial input into a more common format

    check1 = RatioKlinkCheck(input)
    check2 = CheckCommComb(input)
    check3 = CheckMedklink(input)

    if 0.4 <= check1 < 0.5:
        points += 10
    elif 0.4 <= check1 < 0.5:
        points += 20
    elif 0.5 <= check1 < 0.6:
        points += 30
    elif 0.6 <= check1 < 0.7:
        points += 40
    elif 0.7 <= check1 < 0.9:
        points += 30
    elif 0.9 <= check1 < 1.5:
        points += 10

    if 0.0 <= check2 < 0.2:
        points += 20
    elif 0.2 <= check2 < 0.5:
        points += 30

    if check3 < 0.01:
        points += 30
    elif check3 < 0.1:
        points += 10

    return(points)

if __name__ == "__main__":
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                outcome = enigma("hoegaathetmetjoumetmijgaathetgoed", rotorI, rotorII, rotorIII, reflectorB, i, j, k)
                if LangRecog(outcome) > 60:
                    print(LangRecog(outcome))
                    print(outcome)
    print(enigma("InhetRomeinseRijkhadmentweevolkstribunendiedebelangenvanhetvolkbijdesenaatvoorlegden", rotorI, rotorII, rotorIII, reflectorB, 19, 5, 12))
