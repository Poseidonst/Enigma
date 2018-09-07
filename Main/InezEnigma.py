def Enigma(cnt1, cnt2, cnt3, tekst):
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
               "z":"j"}

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

    switch_1 = 0
    switch_2 = 0
    rotor1 = "I"
    rotor2 = "II"
    rotor3 = "III"

    count_I = int(cnt1)
    if count_I < 0:
        count_I += 26
    elif count_I > 25:
        count_I -= 26

    count_II = int(cnt2)
    if count_II < 0:
        count_II += 26
    elif count_II > 25:
        count_II -= 26

    count_III = int(cnt3)
    if count_III < 0:
        count_III += 26
    elif count_III > 25:
        count_III -= 26
    output = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    woord = str(tekst)
    woord = woord.lower()
    for i in woord:
        ni = alphabet.find(i) + count_I
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]

        if rotor1 == "I":
            rotor1 = rotor_I
            switch_1 += 17
        elif rotor1 == "II":
            rotor1 = rotor_II
            switch_1 += 5
        elif rotor1 == "III":
            rotor1 = rotor_III
            switch_1 += 22

        ni = alphabet.find(rotor1[i]) - count_I
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]
        ni = ni + count_II
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]

        if rotor2 == "I":
            rotor2 = rotor_I
            switch_2 += 17
        elif rotor2 == "II":
            rotor2 = rotor_II
            switch_2 = 5
        elif rotor2 == "III":
            rotor2 = rotor_III
            switch_2 = 22

        i = alphabet[alphabet.find(rotor2[i]) - count_II]
        ni = alphabet.find(i)
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]
        ni = ni + count_III
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]


        if rotor3 == "I":
            rotor3 = rotor_I
            switch_3 = 17
        elif rotor3 == "II":
            rotor3 = rotor_II
            switch_3 = 5
        elif rotor3 == "III":
            rotor3 = rotor_III
            switch_3 = 22

        i = alphabet[alphabet.find(rotor3[i]) - count_III]
        ni = alphabet.find(i)
        if ni < 0:
            ni += 26
        elif ni > 25:
            ni -= 26
        i = alphabet[ni]

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

        ni = alphabet.find(i) + count_III
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]
        terug_III = {val:key for (key, val) in rotor3.items()}
        i = alphabet[alphabet.find(terug_III[i]) - count_III]
        #terug Rotor II
        ni = alphabet.find(i) + count_II
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]
        terug_II = {val:key for (key, val) in rotor2.items()}
        i = alphabet[alphabet.find(terug_II[i]) - count_II]
        #terug Rotor I
        ni = alphabet.find(i) + count_I
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]
        terug_I = {val:key for (key, val) in rotor1.items()}
        ni = alphabet.find(terug_I[i]) - count_I
        while ni < 0:
            ni += 26
        while ni > 25:
            ni -= 26
        i = alphabet[ni]

        output += str(i)

        count_I += 1
        for n in range(0, 10):
            if count_I == switch_1 + n * 26:
                count_II += 1
        if count_II == switch_2 + n * 26 and count_I == switch_1 + n * 26:
            count_III += 1

    print(output, end="")

if __name__ == "__main__":
    Enigma(0, 0, 0, "A" * 10000)
