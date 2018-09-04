heen_ref = "a"
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

rotor_III_T ={"b":"a",
           "d":"b",
           "f":"c",
           "h":"d",
           "j":"e",
           "l":"f",
           "c":"g",
           "p":"h",
           "r":"i",
           "t":"j",
           "x":"k",
           "v":"l",
           "z":"m",
           "n":"n",
           "y":"o",
           "e":"p",
           "i":"q",
           "w":"r",
           "g":"s",
           "a":"t",
           "k":"u",
           "m":"v",
           "u":"w",
           "s":"x",
           "q":"y",
           "o":"z" }
Trotor_III_uit = alphabet[alphabet.find(rotor_III_T[Trotor_III_in]) - count_III]

Tnum_rotorII_in = alphabet.find(Trotor_III_uit) - count_II
Theen_rotorII = alphabet[Tnum_rotorII_in]
print (Theen_rotorII)

Tnum_enter_rotorII = alphabet.find(Theen_rotorII) + count_II
print (alphabet[Tnum_enter_rotorII])
print (Tnum_enter_rotorII)
if Tnum_enter_rotorII < 0:
    Tnum_enter_rotorII += 26
elif Tnum_enter_rotorII > 26:
    Tnum_enter_rotorII -= 26

Trotor_II_in = alphabet[Tnum_enter_rotorII]

rotor_II_T ={"a":"a",
           "j":"b",
           "d":"c",
           "k":"d",
           "s":"e",
           "i":"f",
           "r":"g",
           "u":"h",
           "x":"i",
           "b":"j",
           "l":"k",
           "h":"l",
           "w":"m",
           "t":"n",
           "m":"o",
           "c":"p",
           "q":"q",
           "g":"r",
           "z":"s",
           "n":"t",
           "p":"u",
           "y":"v",
           "f":"w",
           "v":"x",
           "o":"y",
           "e":"z" }
Trotor_II_uit = alphabet[alphabet.find(rotor_II_T[Trotor_II_in]) - count_II]

Tnum_rotorI_in = alphabet.find(Trotor_II_uit) - count_I
Theen_rotorI = alphabet[Tnum_rotorI_in]
print (Theen_rotorI)

Tnum_enter_rotorI = alphabet.find(Theen_rotorI) + count_I
print (alphabet[Tnum_enter_rotorI])
print (Tnum_enter_rotorI)
if Tnum_enter_rotorI < 0:
    Tnum_enter_rotorI += 26
elif Tnum_enter_rotorI > 26:
    Tnum_enter_rotorI -= 26

Trotor_I_in = alphabet[Tnum_enter_rotorI]

rotor_I_T ={ "e":"a",
           "k":"b",
           "m":"c",
           "f":"d",
           "l":"e",
           "g":"f",
           "d":"g",
           "q":"h",
           "v":"i",
           "z":"j",
           "n":"k",
           "t":"l",
           "o":"m",
           "w":"n",
           "y":"o",
           "h":"p",
           "x":"q",
           "u":"r",
           "s":"s",
           "p":"t",
           "a":"u",
           "i":"v",
           "b":"w",
           "r":"x",
           "c":"y",
           "j":"z" }
Trotor_I_uit = alphabet[alphabet.find(rotor_I_T[Trotor_I_in]) - count_I]

Tnum_rotorI_uit = alphabet.find(Trotor_I_uit) - count_I
Thuit_rotorI = alphabet[Tnum_rotorI_uit]
print (Thuit_rotorI)
