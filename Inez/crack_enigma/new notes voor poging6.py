l = ['0,0,0', '0,1,2', '1,0,0']
l0 = []
for q in l:
    q = str(q)
    print(q)
    print(q[-1])
    if q[-1] == 0:
        l0.append(q)
    
print(l0)
