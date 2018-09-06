def DependLength(inputsent, listname, countlist):
    for i in range(0, len(inputsent) - 2):
        p = inputsent[i:i + 3]
        if p not in listname:
            listname.append(p)
            countlist.append(1)
        else:
            countlist[listname.index(p)] += 1

def Organise(listname, countlist, diction):
    for i in range(0, len(listname)):
        p = max(countlist)
        index = countlist.index(p)
        diction[listname[index]] = p
        countlist.pop(index)
        listname.pop(index)

def OnlySpace(inputsent):
    inputlist = []
    for i in inputsent:
        if i == " ":
            inputlist.append(i)
        elif i.isalpha():
            inputlist.append(i)

    inputsent = "".join(inputlist)
    return(inputsent)

def Triplet(filename):

    try:
        with open(filename, "r") as reader:
            inputsent = reader.read().lower()
    except:
        inputsent = filename.lower()

    inputsent = OnlySpace(inputsent)

    inputlist = inputsent.split(" ")

    listwords = []
    listamount = []
    dictionwords = {}

    for i in inputlist:
        if len(i) > 2:
            DependLength(i, listwords, listamount)


    Organise(listwords, listamount, dictionwords)

    firsthundred = {k: dictionwords[k] for k in list(dictionwords)[:100]}

    for i in firsthundred.items():
        print(i)


if __name__ == "__main__":
    # Triplet("NederlandseWoordenlijst.txt")
