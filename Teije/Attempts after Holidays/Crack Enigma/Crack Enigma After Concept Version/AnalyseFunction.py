import time
import multiprocessing
def analyse(input1, input2, output):
    start = time.time()
    state2 = True
    state = False
    input1list = []
    input2list = []

    for i in input1:
        for j in i:
            if j not in input1list:
                input1list.append(j)

    for i in input2:
        for j in i:
            if j not in input2list:
                input2list.append(j)

    for i in input1list:
        if i in input2list:
            break
    else:
        state = True

    if not state:
        for i in input1:
            for j in input2list:
                if j in i:
                    if i not in input2 and i[::-1] not in input2:
                        state2 = False
        if state2:
            state = True

    if state:
        for i in range(len(output)):
            output.pop(0)

        for i in input1 + input2:
            if i not in output and i[::-1] not in output:
                output.append(i)
    # print(time.time() - start)
    return(state)

def analyse1(input1, input2, output):
    input1 = list(set(input1))
    state = True
    inputstr1 = ""
    inputstr2 = ""

    for i in input1:
        inputstr1 += i

    for i in input2:
        inputstr2 += i

    for i in inputstr1:
        if i in inputstr2:
            for i in input1:
                for j in inputstr2:
                    if j in i:
                        if i not in input2 and i[::-1] not in input2:
                            state = False
                            break
            break

    if state:
        for i in range(len(output)):
            output.pop(0)
        input = input1 + input2
        for i in input:
            if i not in output and i[::-1] not in output:
                output.append(i)
    return(state)

if __name__ == "__main__":
    # print(analyse(['EM', 'RH', "EM"], ['EM', 'RH'], []))
    start = time.time()
    for i in range(100000):
        analyse1(['EK', 'WB', 'EK', 'OM', 'EK', 'UZ'],['CA', 'EK'], [])
    print(time.time() - start)
    print(analyse(['EK', 'WL', 'EK', 'OM', 'EK', 'UZ'],['CA', 'EK'], []))
    print(analyse1(['EK', 'WB', 'EK', 'OM', 'EK', 'UZ'],['CA', 'EK'], []))
    print(["AB"] + ["AC"])
    alfa = ["AB", "CD", "EF"]
    print(alfa)
    alfa.clear()
    print(alfa)
