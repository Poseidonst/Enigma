l = ['0,0,0', '0,1,2', '1,0,0']
l0 = []
for q in l:
    q = str(q)
    print(q)
    print(q[-1])
    if q[-1] == 0:
        l0.append(q)

print(l0)

listname = []
alfalist = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

for i in range(0, 26):
    for j in alfalist[i:]:
        listname.append(alfalist[i] + j)
for n in listname:
    if n[0] == n[1]:
        listname.remove(n)

print(listname)
