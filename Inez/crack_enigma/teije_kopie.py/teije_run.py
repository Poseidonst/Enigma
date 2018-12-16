from tkinter import *

alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_dict = {chr(65+i) : i for i in range(26)}

class ReflectorClass(object):

    def __init__(self, listname):
        self.listname = listname

class RotorClass(object):

    def __init__(self, listname, revlistname, position, rotortip):
        self.listname = listname
        self.revlistname = revlistname
        self.position = position
        self.rotortip = rotortip

plugdiction = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B",
               "C" : "F", "F" : "C",
               "D" : "G", "G" : "D",
               "E" : "H", "H" : "E",}

plugdiction2 = {"A" : "Z", "Z" : "A",
               "B" : "T", "T" : "B",
               "C" : "F", "F" : "C",
               "D" : "G", "G" : "D",
               "E" : "H", "H" : "E",
               "I" : "N", "N" : "I",
               "J" : "O", "O" : "J",
               "K" : "P", "P" : "K",
               "L" : "Q", "Q" : "L",
               "M" : "R", "R" : "M",}
emptydict = {}

def enigma(userinput, rotor1, rotor2, rotor3, reflector, rotorsetting1, rotorsetting2, rotorsetting3, plugdictionary):

    plugdict = plugdictionary

    output = ""

    rotor1.position = rotorsetting1 % 26
    rotor2.position = rotorsetting2 % 26
    rotor3.position = rotorsetting3 % 26


    rotor1list = rotor1.listname
    rotor2list = rotor2.listname
    rotor3list = rotor3.listname

    rotor1revlist = rotor1.revlistname
    rotor2revlist = rotor2.revlistname
    rotor3revlist = rotor3.revlistname

    reflector = reflector.listname

    for i in userinput.upper():
        if i in "!?.',/+-_<>@#$%^&*():; ":
            output += i
        else:
            pos1 = rotor1.position
            pos2 = rotor2.position
            pos3 = rotor3.position

            diff1 = pos2 - pos1
            diff2 = pos3 - pos2

            try:
                i = plugdict[i]
            except:
                pass

            i = alphabet_dict[i]
            i = rotor1list[(i + pos1) % 26]
            i = rotor2list[(i + diff1) % 26]
            i = rotor3list[(i + diff2) % 26]
            i = reflector[(i - pos3) % 26]
            i = rotor3revlist[(i + pos3) % 26]
            i = rotor2revlist[(i - diff2) % 26]
            i = rotor1revlist[(i - diff1) % 26]
            i = alphabet_list[(i - pos1) % 26]

            try:
                i = plugdict[i]
            except:
                pass

            output += i

            rotor1.position = (rotor1.position + 1) % 26
            if rotor1.position == rotor1.rotortip:
                rotor2.position = (rotor2.position + 1) % 26
            if rotor1.position == rotor1.rotortip and rotor2.position == rotor2.rotortip:
                rotor3.position = (rotor3.position + 1) % 26

    return(output)

rotorI = RotorClass([alphabet_dict[i] for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"], [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9], 0, 17)
rotorII = RotorClass([alphabet_dict[i] for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"], [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18], 0, 5)
rotorIII = RotorClass([alphabet_dict[i] for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"], [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12], 0, 22)
reflectorB = ReflectorClass([alphabet_dict[i] for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"])
reflectorC = ReflectorClass([alphabet_dict[i] for i in "FVPJIAOYEDRZXWGCTKUQSBNMHL"])


#------------------------- GUI Frame -------------------------#

class UserInterface():
    def __init__(self, master):
        self.master = master
        self.page1()
        self.bool = True

    def page1(self):
        self.bool = True
        self.rotorset = [0, 0, 0]
        self.unloadPage()
        self.frame1 = Frame(self.master, bg="white")
        self.frame1.pack(fill="both", expand=True, anchor="n")
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)

        self.output_page = Text(self.frame1, bg="grey80", height=10, relief="raised", state="normal", font="system")
        self.output_page.grid(row=0, column=0, sticky="nsew", padx=1, pady=1, columnspan=3)
        self.output_page.insert("1.0", "\n\n\n\n\n\n\n                                                          This is your output")
        self.output_page.configure(state="disabled")

        self.entry = Text(self.frame1, bg="grey75", height=10, relief="sunken", font="system")
        self.entry.insert("1.0", "\n\n\n\n\n\n\n                                                This is your input, click to begin")
        self.entry.grid(row=1, column=0, sticky="nsew", padx=1, pady=1, columnspan=3)
        self.entry.bind("<KeyRelease-Return>", self.createOutput)
        self.entry.bind("<Button-1>", self.firstSelect)

        self.rotor_label1 = Label(self.frame1, text="             Rotor 1             ", bg="lightskyblue2", font="system", relief="raised")
        self.rotor_label1.grid(row=2, column=0, sticky="nsew", padx=1)
        self.rotor_label2 = Label(self.frame1, text="             Rotor 2             ", bg="lightskyblue2", font="system", relief="raised")
        self.rotor_label2.grid(row=2, column=1, sticky="nsew", padx=1)
        self.rotor_label3 = Label(self.frame1, text="             Rotor 3             ", bg="lightskyblue2", font="system", relief="raised")
        self.rotor_label3.grid(row=2, column=2, sticky="nsew", padx=1)

        self.rotorvar1 = StringVar(self.frame1)
        self.rotorvar1.set("--Select Position--")

        self.rotorvar2 = StringVar(self.frame1)
        self.rotorvar2.set("--Select Postition--")

        self.rotorvar3 = StringVar(self.frame1)
        self.rotorvar3.set("--Select Position--")

        options1 = range(0, 25)
        options2 = range(0, 25)
        options3 = range(0, 25)

        self.rotor_1 = OptionMenu(self.frame1, self.rotorvar1, *options1, command=self.getRotor1)
        self.rotor_1.configure(bg="lightskyblue2", activebackground="lightskyblue1", font="system")
        self.rotor_1.grid(row=3, column=0, sticky="nsew")

        self.rotor_2 = OptionMenu(self.frame1, self.rotorvar2, *options2, command=self.getRotor2)
        self.rotor_2.configure(bg="lightskyblue2", activebackground="lightskyblue1", font="system")
        self.rotor_2.grid(row=3, column=1, sticky="nsew")

        self.rotor_3 = OptionMenu(self.frame1, self.rotorvar3, *options3, command=self.getRotor3)
        self.rotor_3.configure(bg="lightskyblue2", activebackground="lightskyblue1", font="system")
        self.rotor_3.grid(row=3, column=2, sticky="nsew")

        self.button_1 = Button(self.frame1, text="Plugboard", command=self.page2, bg="lightskyblue2", font="system", activebackground="lightskyblue1")
        self.button_1.grid(row=4, column=0, sticky="nsew", padx=1, pady=1, columnspan=3)

    def page2(self):
        self.unloadPage()
        self.frame2 = Frame(self.master, bg="blue", width=50, height=50)
        self.frame2.pack(fill="x", expand=True, anchor="n")
        button_2 = Button(self.frame2, text="next page", command=self.page1).pack(fill="both", expand=True, padx=1, pady=1)

    #---- The Logic ----#
    def firstSelect(self, event):
        if self.bool:
            self.entry.delete("1.0", END)
            self.bool = False

    def unloadPage(self):
        try:
            self.frame1.destroy()
        except:
            pass
        try:
            self.frame2.destroy()
        except:
            pass

    def getRotor1(self, value):
        self.rotorset[0] = value
        print(self.rotorset)

    def getRotor2(self, value):
        self.rotorset[1] = value
        print(self.rotorset)

    def getRotor3(self, value):
        self.rotorset[2] = value
        print(self.rotorset)

    def createOutput(self, event):
        self.output_page.configure(state="normal")
        entry_output = self.entry.get("1.0", END)[:-1:]
        output_list = [i for i in entry_output]
        output_list_filtered = [i for i in entry_output]
        output_list_filtered.remove("\n")
        entry_output = ""
        for i in output_list_filtered:
            entry_output += i
        output = enigma(entry_output, rotorI, rotorII, rotorIII, reflectorB, self.rotorset[0], self.rotorset[1], self.rotorset[2], emptydict)
        enigma_list = [i.lower() for i in output]
        enigma_list[0] = enigma_list[0].upper()
        for i in range(len(enigma_list)):
            if output_list_filtered[i].isupper():
                enigma_list[i] = enigma_list[i].upper()
        output = ""
        for i in enigma_list:
            output += i
        self.output_page.delete("1.0", END)
        self.output_page.insert("1.0", output)
        self.entry.delete("1.0", END)
        self.output_page.configure(state="disabled")

#------------------------- Start Program ----------------------#

if __name__ == "__main__":
    root = Tk()
    root.title("Enigma Machine")
    root.geometry("600x600")
    GUI = UserInterface(root)
    root.mainloop()
