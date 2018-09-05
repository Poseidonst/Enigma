def RatioCheck(*args):
    points = 0
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
    except:
        inputsent = str(args).lower()

    klcount = 0
    medklcount = 0

    for i in inputsent:
        if i.islower():
            if i in "aeoui":
                klcount += 1
            else:
                medklcount += 1

    ratio = klcount / medklcount

    if 0.4 <= ratio < 0.5:
        points += 5
    elif 0.5 <= ratio < 0.6:
        points += 10
    elif 0.6 <= ratio < 0.7:
        points += 30
    elif 0.7 <= ratio < 0.8:
        points += 20
    elif 0.8 <= ratio < 1:
        points += 5
    else:
        points = 0

    return(points)

def CheckMedklink(*args):
    points = 0
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
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
    totalpoints = RatioCheck("OVRQBEPSBLDUIFKNDWSODHRWPAXCUWYOFUHNDJVJRJIBTZADLHJ") + CheckMedklink("OVRQBEPSBLDUIFKNDWSODHRWPAXCUWYOFUHNDJVJRJIBTZADLHJ")
    print(totalpoints)
