"""Code for I hardly know her"""
import random
import string

NON_IHKR_CHANNEL = {"vent-advice-channel"}

def ihkh(info):
    """Checks message for I hardly know her"""
    message_str = info.message.content
    no_punct = message_str.translate(str.maketrans('', '', string.punctuation)).lower()
    split_message = no_punct.split()

    valid_channel = not str(info.message.channel) in NON_IHKR_CHANNEL

    if info.message.author.id == 186239130596933632:
        info.chandler = True

    # I hardly know her command
    if len(message_str) < 100 and valid_channel:
        banned_words = ["boomer", "chandler"]
        er_words = []
        for i in split_message:
            try:
                if i[-2:] == 'er' and i not in banned_words and len(i) > 3:
                    er_words.append(i)
            except IndexError:
                continue
        if bool(er_words):
            info.is_ihkh = True
            if len(er_words) == 1:
                info.return_message = f"{er_words.pop().capitalize()}? I hardly know her!"

            else:
                len_er_words = len(er_words)
                the_chosen_num = random.randint(1,len_er_words)
                the_chosen_str = er_words[the_chosen_num-1]
                info.return_message = f"{the_chosen_str.capitalize()}? I hardly know her!"
