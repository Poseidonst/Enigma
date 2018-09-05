def RatioCheck(*args):
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

    print("De Klinker/Medeklinker verhouding in '%s' is %s" %(*args, klcount/medklcount))

if __name__ == "__main__":
    RatioCheck("TextInputDocs.txt")
