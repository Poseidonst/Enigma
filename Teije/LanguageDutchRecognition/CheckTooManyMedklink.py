def CheckMedklink(*args):
    points = 0
    try:
        inputlist = []
        with open((*args), "r") as reader:
            inputlist.append(reader.read())

        inputsent = "".join(inputlist).lower()
    except:
        inputsent = str(args).lower()

    splitlist = inputsent.split(" ")
    inputsent = "".join(splitlist)

    counter = 0
    streak = 0

    for i in inputsent:
        if i.islower():
            if i in "aeoui":
                streak = 0
            else:
                streak += 1
        if streak > 6:
            counter += 1

    ratio = counter/len(inputsent)

    if ratio < 0.01:
        points += 30
    else:
        points += 0

    return(points)




if __name__ == "__main__":
    print(CheckMedklink("TextInputDocs.txt"))
