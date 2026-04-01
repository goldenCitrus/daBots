import random
import string

Non_Ratio_Channel = {"vent-advice-channel"}

def I_hardly_know_her(I):
    message_str = I.message.content
    no_punct = message_str.translate(str.maketrans('', '', string.punctuation)).lower()
    no_punct = no_punct
    split_message = no_punct.split()
        
    # rnd = random.randint(10,30)
    if I.message.author.id == 186239130596933632:
        I.CF = True
    else:
        # I hardly know her command v v
        if len(message_str) < 100 and not(str(I.message.channel) in Non_Ratio_Channel):
            banned_words = ["boomer", "chandler"]
            er_words = []
            for i in split_message:
                try:
                    if i[-2:] == 'er' and i not in banned_words and len(i) > 3:
                        er_words.append(i)
                except IndexError:
                    continue
            if bool(er_words) == True:
                I.IHKH_vaule = True
                if len(er_words) == 1:
                    I.Return_Message = f"{er_words.pop().capitalize()}? I hardly know her!"

                else:
                    len_er_words = len(er_words)
                    the_chosen_num = random.randint(1,len_er_words)
                    the_chosen_str = er_words[the_chosen_num-1]
                    I.Return_Message = f"{the_chosen_str.capitalize()}? I hardly know her!"