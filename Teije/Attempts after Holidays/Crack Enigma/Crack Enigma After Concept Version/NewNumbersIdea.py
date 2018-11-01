import numpy as np
numdict = {key:value for key, value in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26))}

dict = {}
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if i + j not in dict.keys() and j + i not in dict.keys():
            dict[i + j] = float(str(numdict[i]) +"."+ str(numdict[j]))
print(dict)
print(dict["AB"])
ar1 = np.array([dict["AB"], dict["CD"]])
ar2 = np.array([dict["EF"], dict["GH"]])
ar3 = np.flip(ar1, 0)
print(ar1)
print(ar2)
print(ar3)
print(ar1 - ar2)
print(ar3 - ar2)
def sigmoid(x):
    return(1 / (1 + np.exp(-x)))

print(sigmoid(25))
def analyse(io_array):
    for i in io_array:
        for j in io_array:
            pass
print(bin(2525))
analyse(ar1 - ar2)

def binaryconvert(num):
    total = 0
    num = str(num)
    count = -1
    for i in num:
        count += 1
    for i in num:
        total += int(i) * (2**count)
        count -= 1
    print(total)

binaryconvert(111111111111111)
print(bin(32767))
