list_rotor_I = [i for i in "ekmflgdqvzntowyhxuspaibrcj"]
list_alphabet = "abcdefghijklmnopqrstuvwxyz"
print (list_alphabet.find("a"))
count_I = 0
heen_enter_rotorI = "a"
rotor_I = {"a": list_rotor_I[count_I:count_I + 1:1],
           "b": list_rotor_I[count_I + 1:count_I + 2:1]}
for key in rotor_I:
    if heen_enter_rotorI == key:
        print (rotor_I[key])
        print (str(rotor_I[key]))
        print (list_alphabet.find(str(rotor_I[key])))# hier zit een fout!
        count_I += 1

heen_enter_rotorI = "a"
rotor_I = {"a": list_rotor_I[count_I:count_I + 1:1]}
for key in rotor_I:
    if heen_enter_rotorI == key:
        print (rotor_I[key])
        count_I += 1
count_II = 0

#list_alphabet.find(str(rotor_I[key])) - count_I = nummer_if_II_A
#uitkomst_if_II_A = list_alphabet[nummer_if_II_A]
#heen_enter_rotorII = list_alphabet.find(nummer_if_II_A - count_II)
