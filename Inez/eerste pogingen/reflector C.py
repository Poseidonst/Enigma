dictionary_C = { "a":"f",
                 "b":"v",
                 "c":"p",
                 "d":"j",
                 "e":"i",
                 "f":"a",
                 "g":"o",
                 "h":"y",
                 "i":"e",
                 "j":"d",
                 "k":"r",
                 "l":"z",
                 "m":"x",
                 "n":"w",
                 "o":"g",
                 "p":"c",
                 "q":"t",
                 "r":"k",
                 "s":"u",
                 "t":"q",
                 "u":"s",
                 "v":"b",
                 "w": "n",
                 "x": "m",
                 "y": "h",
                 "z": "l"}

print (dictionary_C)
print (len(dictionary_C))

enters_ref_heen = "d" #uitkomst van de derde rotor, moet nog veranderd worden
for key in dictionary_C:
  if enters_ref_heen == key:
    exit_ref_heen = dictionary_C[key] #gaat weer terug de derde rotor in
    print (exit_ref_heen)
