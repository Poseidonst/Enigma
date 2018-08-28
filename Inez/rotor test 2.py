list_rotor_I = [i for i in "ekmflgdqvzntowyhxuspaibrcj"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

count_I = 28
if count_I < 0:
    count_I += 26
elif count_I > 26:
    count_I -= 26

count_II = 1
if count_II < 0:
    count_II += 26
elif count_II > 26:
    count_II -= 26

heen_enter_rotorI = "a"
nummer_enter_rotorI = alphabet.find(heen_enter_rotorI) + count_I
if nummer_enter_rotorI < 0:
    nummer_enter_rotorI += 26
elif nummer_enter_rotorI > 26:
    nummer_enter_rotorI -= 26

rotor_I_in = alphabet[nummer_enter_rotorI]

rotor_I ={ "a":"e",
           "b":"k",
           "c":"m",
           "d":"f",
           "e":"l",
           "f":"g",
           "g":"d",
           "h":"q",
           "i":"v",
           "j":"z",
           "k":"n",
           "l":"t",
           "m":"o",
           "n":"w",
           "o":"y",
           "p":"h",
           "q":"x",
           "r":"u",
           "s":"s",
           "t":"p",
           "u":"a",
           "v":"i",
           "w":"b",
           "x":"r",
           "y":"c",
           "z":"j" }

for key in rotor_I:
    if rotor_I_in == key:
        rotor_I_uit = rotor_I[key]
        print (rotor_I_uit)

num_rotII_in = alphabet.find(rotor_I_uit) - count_II
rotor_II_in = alphabet[num_rotII_in]
print (rotor_II_in)
count_I += 1
