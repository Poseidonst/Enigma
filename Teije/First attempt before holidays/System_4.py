alphabet_list = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_I_list = [i for i in "EKMFLGDQVZNTOWYHXUSPAIBRCJ"]
reflector_B_list = [i for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]
rotor_II_list = [i for i in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
rotor_III_list = [i for i in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
alphabet_dict = {chr(65 + i) : i for i in range(26)}

rotor_I = {key : value for key, value in zip(alphabet_list, rotor_I_list)}
rotor_I_back = {key : value for key, value in zip(rotor_I_list, alphabet_list)}
rotor_II = {key : value for key, value in zip(alphabet_list, rotor_II_list)}
rotor_II_back = {key : value for key, value in zip(rotor_II_list, alphabet_list)}
rotor_III = {key : value for key, value in zip(alphabet_list, rotor_III_list)}
rotor_III_back = {key : value for key, value in zip(rotor_III_list, alphabet_list)}
reflector_B = {key : value for key, value in zip(alphabet_list, reflector_B_list)}

def make_message(message, start1, start2, start3):
    I = alphabet_dict[start1]
    II = alphabet_dict[start2]
    III = alphabet_dict[start3]
    message = message.upper()
    message_list = [i for i in message]
    end = []

    for i in message_list:
        if I == 26:
            I = 0
        elif I == 17:
            II += 1
            if II == 26:
                II = 0
            elif II == 5:
                III += 1
                if III == 26:
                    III = 0

        prior = I - 26

        alpha = II - I
        if II > I:
            alpha = alpha - 26

        beta = III - II
        if III > II:
            beta = beta - 26

        gamma = -III

        delta = III - 26

        epsilon = II - III
        if III < II:
            epsilon = epsilon - 26

        dzeta = I - II
        if II < I:
            dzeta = dzeta - 26

        secondary = -I

        rotor1 = rotor_I[alphabet_list[alphabet_dict[i] + prior]]
        rotor2 = rotor_II[alphabet_list[alphabet_dict[rotor1] + alpha]]
        rotor3 = rotor_III[alphabet_list[alphabet_dict[rotor2] + beta]]
        reflector = reflector_B[alphabet_list[alphabet_dict[rotor3] + gamma]]
        rotor3_back = rotor_III_back[alphabet_list[alphabet_dict[reflector] + delta]]
        rotor2_back = rotor_II_back[alphabet_list[alphabet_dict[rotor3_back] + epsilon]]
        rotor1_back = rotor_I_back[alphabet_list[alphabet_dict[rotor2_back] + dzeta]]
        ending = alphabet_list[alphabet_dict[rotor1_back] + secondary]

        end.append(ending)
        I += 1

    return ("".join(end))

def decipher(text, guess):
    I = ""
    II = ""
    III = ""
    for i in range(0, 26):
        for j in range(0, 26):
           for k in range(0,26):
                c = make_message(text, alphabet_list[k], alphabet_list[j], alphabet_list[i])
                print(c)
                if guess.upper() in c:
                    I = alphabet_list[k]
                    II = alphabet_list[j]
                    III = alphabet_list[i]
    if not I == "":
        print("\nThese were the rotorsettings: %s %s %s" %(I, II, III))
        print("This is the entire message: \n%s" %(make_message(text, I, II, III)))
    else:
        print("Unable to decipher, try another guess")


print(make_message("struggleofthebetrayedpeopleagainstitsdefraudersthatisintherepressionoftheantisemiticmovementRespectfullyAdolfHitler", "Q", "F", "Q"))
#decipher("XDXHPDZUCMPJYVRNTZNWQOHHEYSETOZKXYFXIXALYOXGINWCUHBGAOHGZHTXHQURZLEQAOCLMOTIJYBUXOHFOISTYISSKUNXOYFJSWQUEJFCIJQUFHG", "hitler")




def safe():
    coded2 = []
    I = start1
    II = start2
    for i in coded:
        if I == 26:
            I = 0
        elif I == 17:
            II += 1
            if II == 26:
                II = 0
        alpha = II - I
        if II > I:
            alpha = alpha - 26
        #i = alphabet_list[alphabet_dict[i] + alpha]
        coded2.append(rotor_II[alphabet_list[alphabet_dict[i] + alpha]])
        I += 1

        coded.append(rotor1)
        coded2.append(rotor2)
        coded3.append(rotor3)
        reflectorlist.append(reflector)
        coded4.append(rotor3_back)
        coded5.append(rotor2_back)
        coded6.append(rotor1_back)

        coded = []
        coded2 = []
        coded3 = []
        reflectorlist = []
        coded4 = []
        coded5 = []
        coded6 = []
