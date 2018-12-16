listname = []
alfalist = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
for i in range(0, 26):
    for j in alfalist[i:]:
        listname.append(alfalist[i] + j)
print(listname)
for n in listname:
    if n[0] == n[1]:
        listname.remove(n)

print(listname)
