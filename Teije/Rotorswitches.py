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



print(switch_rotor_back(rotor_I_back, 1))
