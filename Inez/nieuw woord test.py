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
    elif ni > 26:
        ni -= 26
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

    ni = alphabet.find(i) - count_II
    i = alphabet[ni]
    print (i)

    count_I += 1
