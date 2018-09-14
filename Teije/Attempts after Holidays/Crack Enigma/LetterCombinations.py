# mainlist = []
#
# for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         if (i + j) not in mainlist and (j + i) not in mainlist:
#             mainlist.append(i + j)
#
# print(mainlist)
#
# while mainlist:
#     var = mainlist[0]
#     var1 = mainlist.index(var)
#     mainlist.pop(var1)
#     print(mainlist)

contain2 = "AB CD EF GH IJ"
contain2list = contain2.split(" ")
contain2 = "".join(contain2list)
print(contain2)
topcount = 0
count = 0
var2 = "".join(set(contain2))
for p in var2:
    for q in contain2:
        if p == q:
            count += 1
    if count > 1:
        topcount += 1
    count = 0
if topcount == 0:
    print(contain2)
