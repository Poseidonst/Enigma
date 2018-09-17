listname = []
alfalist = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

for i in range(0, 26):
    for j in alfalist[i:]:
        listname.append(alfalist[i] + j)

print(listname)
