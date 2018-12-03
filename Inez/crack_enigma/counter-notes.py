
count1 = 0
count2 = 0
count3 = 0
alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

GW = "W" #gegeven woord

def test(woord):
    output = ""

    for i in woord:
        if i == GW:
            output += i

    return(output)

ah = test(alfa[count1])
print(ah)
while len(ah) == 0:
    try:
        ah = test(alfa[count1 + 1])
    except:
         print(ah)

zero = 0
