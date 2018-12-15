
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
    counter += 1
print(koppels)
for i in koppels: #JTOPUNAJUQNBE
    if i not in koppels_enkel and i[::-1] not in koppels_enkel:
        koppels_enkel.append(i)

    else:
        twee_loop.append(i + " " + i[::-1])

print(twee_loop)
print(koppels_enkel)

zelfde = []

for n in input:

    setjes_count = 0
    while setjes_count < 13:
        if n == GW[setjes_count] or n == input[setjes_count]:
            zelfde.append(n)
        setjes_count += 1
print(zelfde)
