heen_ref = "d"
alphabet = "abcdefghijklmnopqrstuvwxyz"
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

enters_ref_heen = heen_ref #uitkomst van de derde rotor, moet nog gefixt
for key in dictionary_B:
  if enters_ref_heen == key:
    exit_ref_heen = dictionary_B[key] #gaat weer terug de derde rotor in
    print (exit_ref_heen)

Tnum_enter_rotorIII = alphabet.find(exit_ref_heen) + count_III
print (alphabet[Tnum_enter_rotorIII])
print (Tnum_enter_rotorIII)
if Tnum_enter_rotorIII < 0:
    Tnum_enter_rotorIII += 26
elif Tnum_enter_rotorIII > 26:
    Tnum_enter_rotorIII -= 26

Trotor_III_in = alphabet[Tnum_enter_rotorIII]

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
Trotor_III_uit = alphabet[alphabet.find(rotor_III[Trotor_III_in]) - count_III]

Tnum_rotorII_in = alphabet.find(Trotor_III_uit) - count_II
Theen_rotorII = alphabet[Tnum_rotorII_in]
print (Theen_rotorII)
