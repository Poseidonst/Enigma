def FileReader(filename):
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
    except:
        inputsent = filename.lower()

    return(inputsent)

def RatioCheck(filename):

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


if __name__ == "__main__":
    print(RatioCheck("TextInput.txt"))
