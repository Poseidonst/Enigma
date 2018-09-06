def FileReader(filename):
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
    except:
        inputsent = filename.lower()

    return(inputsent)

def CheckCommComb(inputsent):                       #The program can take any list it wants to check for the combinations, and thus this can also be used for 2 letter combination or 4 letter combinations
    count = 0
    common = "ing ver sch ter ste tie cht der ers ere aar ren eid nde ngs and ten ent ens eri erk rij oor ati hei gen est end eli ele rin ken sta ond lin den str aan nge eer nst ker len tel ach nte lij ege raa ijk enb erb ant gel del ena ier erd ede pro eve uit aal men lan wer per env ist aat erv eld art nin cha ger era tra sti iek ven tin rst eno eni pen din eke erg uur roe rde enk eel ite ert lie rie sto ont het een die dat wie wat hoe"
    commonlist = common.split(" ")                  #Makes a list of the most common triplets and some 3 letter common words like "het, wat, wie, hoe, een"

    inputsent = FileReader(inputsent)

    inputlist = inputsent.split(" ")                #Removes spaces from the input sentence
    inputsent = "".join(inputlist)

    for i in commonlist:                            #Iterates through all the common triplets
        if i in inputsent.lower():                  #If triplet is in the inputsent it will continue
            count += inputsent.lower().count(i)     #In this parts it then counts how many times the triplet is in the text and adds the amount to a counter

    outcome = count/len(inputsent)                  #Here is the total count devided by the length of the message
    return(outcome)                                 #Outcome is usually for Dutch a constant as it devides by the length of the message


print(CheckCommComb("TextInput.txt"))
