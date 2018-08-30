list_rotor_I = [i for i in "ekmflgdqvzntowyhxuspaibrcj"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

count_I = 6
if count_I < 0:
    count_I += 26
elif count_I > 26:
    count_I -= 26

count_II = 27
if count_II < 0:
    count_II += 26
elif count_II > 26:
    count_II -= 26

count_III = 5
if count_III < 0:
    count_III += 26
elif count_III > 26:
    count_III -= 26

heen_rotorI = "g"

num_enter_rotorI = alphabet.find(heen_rotorI) + count_I
print (alphabet.find(heen_rotorI))
print (num_enter_rotorI)
if num_enter_rotorI < 0:
    num_enter_rotorI += 26
elif num_enter_rotorI > 26:
    num_enter_rotorI -= 26

rotor_I_in = alphabet[num_enter_rotorI]

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

rotor_I_uit = alphabet[alphabet.find(rotor_I[rotor_I_in]) - count_I]

num_rotII_in = alphabet.find(rotor_I_uit) - count_II
heen_rotorII = alphabet[num_rotII_in]
print (heen_rotorII)

count_I += 1

num_enter_rotorII = num_rotII_in + count_II
print (alphabet[num_enter_rotorII])
print (num_enter_rotorII)
if num_enter_rotorII < 0:
    num_enter_rotorII += 26
elif num_enter_rotorII > 26:
    num_enter_rotorII -= 26

rotor_II_in = alphabet[num_enter_rotorII]

rotor_II ={"a":"a",
           "b":"j",
           "c":"d",
           "d":"k",
           "e":"s",
           "f":"i",
           "g":"r",
           "h":"u",
           "i":"x",
           "j":"b",
           "k":"l",
           "l":"h",
           "m":"w",
           "n":"t",
           "o":"m",
           "p":"c",
           "q":"q",
           "r":"g",
           "s":"z",
           "t":"n",
           "u":"p",
           "v":"y",
           "w":"f",
           "x":"v",
           "y":"o",
           "z":"e" }

rotor_II_uit = alphabet[alphabet.find(rotor_II[rotor_II_in]) - count_II]

num_rotIII_in = alphabet.find(rotor_II_uit) - count_III
heen_rotorIII = alphabet[num_rotIII_in]
print (heen_rotorIII)

num_enter_rotorIII = num_rotIII_in + count_III
print (alphabet[num_enter_rotorIII])
print (num_enter_rotorIII)
if num_enter_rotorIII < 0:
    num_enter_rotorIII += 26
elif num_enter_rotorIII > 26:
    num_enter_rotorIII -= 26

rotor_III_in = alphabet[num_enter_rotorIII]

rotor_III ={"a":"b",
           "b":"d",
           "c":"f",
           "d":"h",
           "e":"j",
           "f":"l",
           "g":"c",
           "h":"p",
           "i":"r",
           "j":"t",
           "k":"x",
           "l":"v",
           "m":"z",
           "n":"n",
           "o":"y",
           "p":"e",
           "q":"i",
           "r":"w",
           "s":"g",
           "t":"a",
           "u":"k",
           "v":"m",
           "w":"u",
           "x":"s",
           "y":"q",
           "z":"o" }
rotor_III_uit = alphabet[alphabet.find(rotor_III[rotor_III_in]) - count_III]

num_ref_in = alphabet.find(rotor_III_uit) - count_III
heen_ref = alphabet[num_ref_in]
print (heen_ref)

#als Count_I 17 is (dus van Q naar R springt) count_II += 1
