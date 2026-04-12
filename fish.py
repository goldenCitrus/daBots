"""Code for fish checks"""

NON_FISH_CHANNEL = {"vent-advice-channel"}

def has_fish(info):
    """Code to check for fish names in messages"""
    if info.message.channel.name not in NON_FISH_CHANNEL:
        target = info.message.content.strip('*').lower()
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
            info.return_message = 'Fish Found'
        else:
            info.return_message = ''
