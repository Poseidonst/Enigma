def FileReader(filename):
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
    except:
        inputsent = filename.lower()

    return(inputsent)

def CheckCommComb(inputsent):
    count = 0
    common = "ing eer sch ere oor ren erd ter ste aar voo aan ges est cht ger pro bes eid ten der ken hei pla per eri den end len pre bel gen tie eld ele isc nde ber and gro ers gep esc ent bed ede oed pen lin vol sti lĳk tig tel ens roe ver bek ort loe ist ard gev tte nen ati gra eve ker pol rin ier ete gel raa art loo lan lle sse bev roo eke ond gew kke rie nne par tis ach nge ant sen ast dig laa ans ang blo"
    commonlist = common.split(" ")

    inputsent = FileReader(inputsent)
    inputlist = inputsent.split(" ")
    inputsent = "".join(inputlist)

    for i in commonlist:
        if i in inputsent.lower():
            count += inputsent.lower().count(i)

    outcome = count/len(inputsent)


print(CheckCommComb("TextInputDocs.txt"))
