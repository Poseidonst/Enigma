list_rotor_I = [i for i in "ekmflgdqvzntowyhxuspaibrcj"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
print (alphabet.find("a"))
count_I = 0
if count_I < 0:
    count_I += 26
elif count_I > 26:
    count_I -= 26
EnterHeenI = "a"
rotor_I = {"a": list_rotor_I[count_I:count_I + 1:1],
           "b": list_rotor_I[count_I + 1:count_I + 2:1]}
for key in rotor_I:
    if EnterHeenI == key:
        print (rotor_I[key])
        print (str(rotor_I[key]))
        print (alphabet.find(str(rotor_I[key])))# hier zit een fout!

count_II = 3
if count_II < 0:
    count_II += 26
elif count_II > 26:
    count_II -= 26

nummer_if_II_A = alphabet.find(str(rotor_I[key])) - count_I
if nummer_if_II_A < 0:
    nummer_if_II_A += 26
elif nummer_if_II_A > 26:
    nummer_if_II_A -= 26
uitkomst_if_II_A = alphabet[nummer_if_II_A]
print (nummer_if_II_A)
print (nummer_if_II_A - count_II)
EnterHeenII = alphabet[nummer_if_II_A - count_II]
print (EnterHeenII)

count_I += 1
