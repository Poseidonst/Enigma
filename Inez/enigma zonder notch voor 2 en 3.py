count_I = int(input("Instelling rotorI: "))
if count_I < 0:
    count_I += 26
elif count_I > 25:
    count_I -= 26

count_II = int(input("Instelling rotorII: "))
if count_II < 0:
    count_II += 26
elif count_II > 25:
    count_II -= 26

count_III = int(input("Instelling rotorIII: "))
if count_III < 0:
    count_III += 26
elif count_III > 25:
    count_III -= 26
output = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
woord = input("Insert tekst: ")
for i in woord:
    ni = alphabet.find(i) + count_I
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    i = alphabet[ni]
    print("rotor_I in: " + i)
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
    ni = alphabet.find(rotor_I[i]) - count_I
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    # i = alphabet[ni]
    # ni = alphabet.find(i) - count_II
    # while ni < 0:
    #     ni += 26
    # while ni > 25:
    #     ni -= 26
    i = alphabet[ni]
    ni = ni + count_II
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    i = alphabet[ni]
    print("rotor_II in: " + i)
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
    print ("rotor_III in: " + i)
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
    ni = alphabet.find(i)
    if ni < 0:
        ni += 26
    elif ni > 25:
        ni -= 26
    i = alphabet[ni]
    print("ref in: " + i)
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
    print("ref uit: " + i)
    #terug Rotor III
    ni = alphabet.find(i) + count_III
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    i = alphabet[ni]
    terug_III = {val:key for (key, val) in rotor_III.items()}
    i = alphabet[alphabet.find(terug_III[i]) - count_III]
    #terug Rotor II
    ni = alphabet.find(i) + count_II
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    i = alphabet[ni]
    terug_II = {val:key for (key, val) in rotor_II.items()}
    i = alphabet[alphabet.find(terug_II[i]) - count_II]
    #terug Rotor I
    ni = alphabet.find(i) + count_I
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    i = alphabet[ni]
    terug_I = {val:key for (key, val) in rotor_I.items()}
    ni = alphabet.find(terug_I[i]) - count_I
    while ni < 0:
        ni += 26
    while ni > 25:
        ni -= 26
    i = alphabet[ni]
    print (i)
    output += str(i)

    count_I += 1
    for n in range(0, 10):
        if count_I == 17 * n:
            count_II += 1

    if count_II == 5 and count_I == 17:
        count_III += 1
    print (count_I)
    print (count_II)
    print (count_III)
#0,0,0:
#nftzmgisxipjwgdnjjcoqtyrigdmxfiesrwzgtoiuiejcoqtyrigdmxfiesrwzgtoiuiejco
#NFTZMGISXIPJWGDNJJCOQTYRIGDMXFIESRWZGTOIUIEKKDCSHTPYOEPVXNHVRWWESFRUXDGWOZDMNKIZWNCZ

#0,4 0
#uboojeglcpxkublyflgovbuypkojwbowsecqzookviiodtbzdqrojxhnfhbofdzctzqpowvomqn

print (output)
