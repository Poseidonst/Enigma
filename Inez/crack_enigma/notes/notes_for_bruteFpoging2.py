input = input("Geef een letter: ")
GW = "WETTERBERICHT"

listname = []
alfalist = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
for i in range(0, 26):
    for j in alfalist[i:]:
        listname.append(alfalist[i] + j)
for n in listname:
    if n[0] == n[1]:
        listname.remove(n)

print(listname)

for plug1 in listname:
    print(plug1)
    for plug2 in listname:
        if plug1[0] != plug2[0] and plug1[0] != plug2[1] and plug1[1] != plug2[0] and plug1[1] != plug2[1]:
            plugdiction = { plug1[0] : plug1[1], plug1[1] : plug1[0],
                            plug2[0] : plug2[1], plug2[1] : plug2[0]}
            print(plugdiction)
