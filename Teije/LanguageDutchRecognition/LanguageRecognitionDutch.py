inputlist = []

with open("TextInputDocs.txt", "r") as j:
    inputlist.append(j.read())

input = "".join(inputlist)

def RatioCheck(inputsent):

    inputsent = inputsent.lower()
    inputsentlist = inputsent.split(" ")
    inputsent = "".join(inputsentlist)

    klinkercount = 0
    medeklinkercount = 0

    for i in inputsent:
        if i.islower():
            if i in "aeoui":
                klinkercount += 1
            else:
                medeklinkercount += 1

    print("The klinker/mederklinker ratio from textfile")
    print(klinkercount / medeklinkercount)



if __name__ == "__main__":
    RatioCheck(input)
