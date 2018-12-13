alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GW = "WETTERBERICHT" #MVAEDUWHFAVPD(0,0,0)
NEE = [ ]
JA = []
koppels = []
koppels_enkel = []
twee_loop = []
input = input("Geef een letter: ")
counter = 0
while counter < len(input):
    koppels.append(input[counter] + GW[counter])
    # if alphabet.index(input[counter]) < alphabet.index(GW[counter]):
    #     koppels.append(input[counter] + GW[counter])
    # else:
    #     koppels.append(GW[counter] + input[counter])
    counter += 1
print(koppels)
for i in koppels: #JTOPUNAJUQNBE
    if i not in koppels_enkel and i[::-1] not in koppels_enkel:
        koppels_enkel.append(i)
    else:
        twee_loop.append(i + " " + i[::-1])

print(twee_loop)
print(koppels_enkel)
