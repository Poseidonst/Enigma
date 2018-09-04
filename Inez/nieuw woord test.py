count_I = int(input("Instelling rotorI: "))
if count_I < 0:
    count_I += 26
elif count_I > 26:
    count_I -= 26

count_II = int(input("Instelling rotorII: "))
if count_II < 0:
    count_II += 26
elif count_II > 26:
    count_II -= 26

count_III = int(input("Instelling rotorIII: "))
if count_III < 0:
    count_III += 26
elif count_III > 26:
    count_III -= 26

alphabet = "abcdefghijklmnopqrstuvwxyz"
woord = input("Insert tekst: ")
for i in woord:
    ni = alphabet.find(i) + count_I
    if ni < 0:
        ni += 26
    elif ni > 25:
        ni -= 26
        print (ni)
        i = alphabet[ni]

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

        i = alphabet[alphabet.find(rotor_I[i]) - count_I]
        # print (i)
        ni = alphabet.find(i) - count_II
        i = alphabet[ni]
        # print (i)
        ni = ni + count_II
        print (ni)
        i = alphabet[ni]
        # print (i)

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

        i = alphabet[alphabet.find(rotor_II[i]) - count_II]
        # print (i)
        ni = alphabet.find(i) - count_III
        i = alphabet[ni]
        # print (i)
        ni = ni + count_III
        print (ni)
        i = alphabet[ni]
        # print (i)
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
        i = alphabet[alphabet.find(rotor_III[i]) - count_III]
        # print (i)
        ni = alphabet.find(i) - count_III
        i = alphabet[ni]
        # print (i)
        print (ni)
        #als Count_I 17 is (dus van Q naar R springt) count_II += 1
        dictionary_B = { "a":"y",
                         "b":"r",
                         "c":"u",
                         "d":"h",
                         "e":"q",
                         "f":"s",
                         "g":"l",
                         "h":"d",
                         "i":"p",
                         "j":"x",
                         "k":"n",
                         "l":"g",
                         "m":"o",
                         "n":"k",
                         "o":"m",
                         "p":"i",
                         "q":"e",
                         "r":"b",
                         "s":"f",
                         "t":"z",
                         "u":"c",
                         "v":"w",
                         "w": "v",
                         "x": "j",
                         "y": "a",
                         "z": "t"}

        i = alphabet[alphabet.find(dictionary_B[i])]
        print (ni)
        #terug Rotor III
        ni = alphabet.find(i) + count_III
        i = alphabet[ni]
        terug_III = {val:key for (key, val) in rotor_III.items()}
        i = alphabet[alphabet.find(terug_III[i]) - count_III]

        print(ni)
        #terug Rotor II
        ni = alphabet.find(i) + count_II
        i = alphabet[ni]
        terug_II = {val:key for (key, val) in rotor_II.items()}
        i = alphabet[alphabet.find(terug_II[i]) - count_II]
        print (ni)
        #terug Rotor I
        ni = alphabet.find(i) + count_I
        i = alphabet[ni]
        print (ni)
        terug_I = {val:key for (key, val) in rotor_I.items()}
        i = alphabet[(alphabet.find(terug_I[i]) - count_I)]
        print (ni)
        print (i)
        count_I += 1
