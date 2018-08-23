alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_I_list = [i for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
reflector_B_list = [i for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]
alphabet_dict = {chr(65+i) : i for i in range(26)}
rotor_I = {key : value for key, value in zip(alphabet_list, rotor_I_list)}
rotor_I_back = {key : value for key, value in zip(rotor_I_list, alphabet_list)}
reflector_B = {key : value for key, value in zip(alphabet_list, reflector_B_list)}

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

def print_message_switch(message):
    counter = 0
    rotor_back = switch_rotor_back(rotor_I_back, counter)
    rotor = switch_rotor(rotor_I, counter)
    message = message.upper()
    message_list = list(message)
    iteration_list = [i for i in range(0, (len(message_list)))] #This way it stays on 1 line and doesn't add the next print to that line
    lenmin = int(len(message_list) - 1)
    for i in iteration_list:

        if message_list[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            checker1 = alphabet_dict[rotor[message_list[i]]] - counter

            while checker1 > 25 or checker1 < -26: #This way the indices will stay in range
                checker1 = 26 - abs(checker1)

            checker2 = alphabet_dict[reflector_B[alphabet_list[checker1]]] + counter

            while checker2 > 25 or checker2 < -26: #This way the indices will stay in range
                checker2 = 26 - abs(checker2)

            if i != lenmin:
                print((rotor_back[alphabet_list[checker2]]), end = "")
            else:
                print((rotor_back[alphabet_list[checker2]]))

        else:
            if i != lenmin:
                print(" ", end = "")
            else:
                print(" ")




        counter += 1
        rotor = switch_rotor(rotor_I,  counter)
        rotor_back = switch_rotor_back(rotor_I_back, counter)

print_message_switch("Hallohoegaathet?")
print_message_switch("ANYGDJPBUBNMZUE")
