
alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GW = "F" #gegeven woord

def test(woord):
    output = ""
    for i in woord:
        if i == GW:
            output += i

    return(output)

meh = 0

while test(alfa[meh]) != GW:
    meh = meh + 1
    print("nee" + str(meh))
else:
    meh = meh + 1
    print(meh)
