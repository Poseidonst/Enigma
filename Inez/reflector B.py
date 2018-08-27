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

enters_ref_heen = "d" #uitkomst van de derde rotor, moet nog gefixt
for key in dictionary_B:
  if enters_ref_heen == key:
    exit_ref_heen = dictionary_B[key] #gaat weer terug de derde rotor in
    print (exit_ref_heen)
