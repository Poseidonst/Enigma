alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_I_list = [i for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
reflector_B_list = [i for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]
rotor_II_list = [i for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotor_III_list = [i for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
alphabet_dict = {chr(65 + i) : i for i in range(26)}

rotor_I = {key : value for key, value in zip(alphabet_list, rotor_I_list)}
rotor_I_back = {key : value for key, value in zip(rotor_I_list, alphabet_list)}
rotor_II = {key : value for key, value in zip(alphabet_list, rotor_II_list)}
rotor_II_back = {key : value for key, value in zip(rotor_II_list, alphabet_list)}
rotor_III = {key : value for key, value in zip(alphabet_list, rotor_III_list)}
rotor_III_back = {key : value for key, value in zip(rotor_III_list, alphabet_list)}
reflector_B = {key : value for key, value in zip(alphabet_list, reflector_B_list)}

print (rotor_III)

def switch_rotor(rotor, places):
    keys, values = zip(*rotor.items())
    values = list(values)
    for i in range(0, places):
        values += [values.pop(0)]
    new_rotor = {key : value for key, value in zip(keys, values)}
    return (new_rotor)

def switch_rotor_back(rotor, places):
    keys, values = zip(*rotor.items())
    values = list(values)
    for i in range(0, places):
        values.insert(0, values[25])
    new_rotor = {key : value for key, value in zip(keys, values)}
    return (new_rotor)

def onerm(message, startI, startII, startIII):
    message = message.upper()
    count = startI
    codedlist = []
    for i in message:                                   #Message through rotorI
        new_rotor_I = switch_rotor(rotor_I, count)
        codedlist.append(new_rotor_I[i])
        count += 1

    print(codedlist)

    count2 = startII                                    #Message through rotorI
    count = startI
    coded2list = []
    for i in codedlist:
        if count == 17:
            count2 += 1
            if count2 > 25:
                count2 = count2 % 26
        new_rotor_II = switch_rotor(rotor_II, count2)
        if count > 25:
            count = count % 26
        alpha = int(alphabet_dict[i])
        coded2list.append(new_rotor_II[alphabet_list[alpha - count]])
        count += 1

    print (coded2list)

    count3 = startIII                                   #Message through rotorIII
    count2 = startII
    count = startI
    codedlist = []
    for i in coded2list:
        count += 1
        if count == 17:
            count2 += 1
            if count2 > 25:
                count2 = count2 % 26
        if count2 == 5:
            count3 += 1
            if count2 > 25:
                count3 = count3 % 26                        #Is possible to make more efficient!!!
        new_rotor_III = switch_rotor(rotor_III, count3)
        if count > 25:
            count = count % 26
        alpha = int(alphabet_dict[i])
        codedlist.append(new_rotor_III[alphabet_list[alpha - count2]])
        count += 1

    print (codedlist)

    count = startII
    coded2list = []
    for i in codedlist:
        if count > 25:
            count = count % 26
        alpha = int(alphabet_dict[i])
        coded2list.append(reflector_B[alphabet_list[alpha - count]])
        count += 1

    count = startI
    codedlist = []
    for i in coded2list:
        new_rotor_I_back = switch_rotor_back(rotor_I_back, count)
        if count > 25:
            count = count % 26
        beta = int(alphabet_dict[i]) + count
        if beta > 25:
            beta = beta % 26
        codedlist.append(new_rotor_I_back[alphabet_list[beta]])
        count += 1

    code = "".join(codedlist)
    return(code)


print(onerm("AAAAAAAAAAAAAAAAAAAAA", 14, 2, 0))
