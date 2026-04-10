import os

Non_Ratio_Channel = {"vent-advice-channel"}

def Fish(I):
    if I.message.channel.name not in Non_Ratio_Channel:
        target = I.message.content.strip('*').lower()
        path = os.getcwd()
        path = f"{path}\\Fish.xlsx"
        
        with open('Information Files\\fish.txt', 'r') as file:
            Fish_list = [line.strip() for line in file.readlines()]

        Message = target.split()
        Message_list = []
        for word in Message:
            if word[-2:] == '\'s':
                Message_list.append(word[:-2])
            elif word[-1:] == 's':
                Message_list.append(word[:-1])
            else:
                Message_list.append(word)

        any_common = not set(Fish_list).isdisjoint(Message_list)
        if any_common:
            I.Return_Message = 'Fish Found'
        else:
            I.Return_Message = ''
