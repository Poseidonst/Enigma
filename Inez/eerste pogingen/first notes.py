list_alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
# test voor slicing: print (list_alphabet[0:2:1])

list_rotor_I = [i for i in "ekmflgdqvzntowyhxuspaibrcj"]
list_rotor_II = [i for i in "ajdksiruxblhwtmcqgznpyfvoe"]
list_rotor_III = [i for i in "bdfhjlcprtxvznyeiwgakmusqo"]

list_reflector_B = [i for i in "yruhqsldpxngokmiebfzcwvjat"]
list_reflector_C = [i for i in "fvpjiaoyedrzxwgctkuqsbnmhl"]

count = 0
count += 1


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
print (dictionary_B)
print (len(dictionary_B))
print (dictionary_B["a"])

enters_ref_heen = "d" #uitkomst van de derde rotor
for key in dictionary_B:
  if enters_ref_heen == key:
    exit_ref_heen = dictionary_B[key] #gaat weer terug de derde rotor in
    print (exit_ref_heen)

input = input("geef een letter: ")#gaat dan eerst door schakelbord
#heen_enter_rotorI
#heen_enter_rotorII
#heen_enter_rotorIII
#enters_ref_heen
#terug_enter_rotorIII == exit_ref_heen
#terug_enter_rotorII
#terug_enter_rotorII
#uitkomst

schakelbord = {"a":"a",
               "b":"z",
               "c":"c",
               "d":"d",
               "e":"e",
               "f":"f",
               "g":"g",
               "h":"h",
               "i":"i",
               "j":"j",
               "k":"k",
               "l":"l",
               "m":"m",
               "n":"n",
               "o":"o",
               "p":"p",
               "q":"q",
               "r":"r",
               "s":"s",
               "t":"t",
               "u":"u",
               "v":"v",
               "w": "w",
               "x": "x",
               "y": "y",
               "z": "z"}
for key in schakelbord:
    if input == key:
        heen_enter_rotorI = schakelbord[key]
        print(heen_enter_rotorI)\

woord = ["H", "E", "Y"]
print (woord[0:1:1])
