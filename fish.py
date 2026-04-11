"""Code for fish checks"""
import os

NON_RATIO_CHANNEL = {"vent-advice-channel"}

def has_fish(information):
    """Code to check for fish names in messages"""
    if information.message.channel.name not in NON_RATIO_CHANNEL:
        target = information.message.content.strip('*').lower()
        path = os.getcwd()
        path = f"{path}\\Fish.xlsx"
        with open('Information Files\\fish.txt', encoding="utf-8") as file:
            fish_list = [line.strip() for line in file.readlines()]

        message = target.split()
        message_list = []
        for word in message:
            if word[-2:] == '\'s':
                message_list.append(word[:-2])
            elif word[-1:] == 's':
                message_list.append(word[:-1])
            else:
                message_list.append(word)

        any_common = not set(fish_list).isdisjoint(message_list)
        if any_common:
            information.Return_Message = 'Fish Found'
        else:
            information.Return_Message = ''
