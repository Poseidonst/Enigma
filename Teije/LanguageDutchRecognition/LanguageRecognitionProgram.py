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
        ratio = klcount / medklcount                        #Calculates the ratio between klinkers and medeklinkers which is unique for each language
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
    print(LangRecog("InhetRomeinseRijkhadmentweevolkstribunendiedebelangenvanhetvolkbijdesenaatvoorlegden"))
