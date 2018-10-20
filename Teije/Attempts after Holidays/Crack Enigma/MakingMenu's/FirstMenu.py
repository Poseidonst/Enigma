#I want to link MMUPYUXHCZOID to WETTERBERICHT
text = "WETTERBERICHT"
cipher = "MMUPYUXHCZOID"
matrix = []
occurance = []
totaldict = {}
input = []
for i in range(len(text)):
    input.append(text[i])
    input.append(cipher[i])
    input.append(i)
    matrix.append(input)
    input = []
    if text[i] not in occurance:
        occurance.append(text[i])
    if cipher[i] not in occurance:
        occurance.append(cipher[i])

for i in occurance:
    totaldict[i] = []
    for j in matrix:
        print(str(j) + i)
        if i in j:
            totaldict[i].append[j]
print(totaldict)
