letter1 = "A"
letter2 = "B"

def ML(runner):
    if runner == letter1:
        print(runner)
    else:
        print('NEE')
    return

input = input("Zeg iets: ")
for i in input:
    ML(i)

list = [0]
def counter(C1, C2, C3):
    count1 = C1
    count2 = C2
    count3 = C3
    def ML(count1, count2, count3):
        list.append(count1)
        return
    ML(count1, count2, count3)
    count1 += 1
    return(list)

counter(0 + list.pop(),0,0)
print(list)
