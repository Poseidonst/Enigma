def FileReader(filename):
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
    except:
        inputsent = filename.lower()

    return(inputsent)

def CheckMedklink(filename):
    inputsent = FileReader(filename)                            #Reads all the items from a file or string and stores it in inputsent

    splitlist = inputsent.split(" ")                            #Removes spaces from the sentence
    inputsent = "".join(splitlist)

    counter = 0                                                 #Counter variable which counts the amount of medeklinker streaks more than 6
    streak = 0                                                  #Counter variable which counts the streak of medeklinkers in a part of the text

    for i in inputsent:                                         #Iterates through each letter of the message
        if i.isalpha():                                         #Checks if the letter is indeed a letter and not a space or punctuation e.g.
            if i in "aeoui":                                    #If the letter is a klinker it sets the streak counter to 0
                streak = 0
            else:                                               #If the letter is a medeklinker it adds 1 to the streak counter
                streak += 1
        if streak > 6:                                          #If the streak counter is greater than 6 it will add 1 to the counter
            counter += 1

    ratio = counter/len(inputsent)                              #The counter is devided by the amount of letters in the text, this way the length of the text doesn't matter for the output
    return(ratio)




if __name__ == "__main__":
    print(CheckMedklink("TextInputDocs.txt"))
