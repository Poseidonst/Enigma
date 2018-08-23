def print_message(message):
    message = message.upper()
    message_list = list(message)
    iteration_list = [i for i in range(0, (len(message_list)))]
    lenmin = int(len(message_list) - 1)
    for i in iteration_list:
        if i != lenmin:
            if message_list[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print((rotor_I_back[reflector_B[rotor_I[message_list[i]]]]), end = "")
            else:
                print(" ", end = "")
        else:
            print((rotor_I_back[reflector_B[rotor_I[message_list[i]]]]))
