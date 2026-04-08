import random

def CurrentRules(I):
    with open('Rules.txt', 'r') as file:
        I.Return_Message = file.read()

def AddRules():
    return

def Join_The_Game(I):
    with open('Game_Members.txt', 'r') as file:
        player_list = [line.strip() for line in file.readlines()]
        file.close
    
    if str(I.message.user) not in player_list:
        with open('Game_Members.txt', 'a') as file:
            file.write(f'{I.message.user}\n')
            file.close
        I.Return_Message = 'was added to the Game'
    else:
        I.Return_Message = "you can't join twice"
        