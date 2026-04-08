import os

def Fish(I):
    target = I.message.content.strip().lower()
    print(target)
    path = os.getcwd()
    path = f"{path}\\Fish.xlsx"
    
    with open('fish.txt', 'r') as file:
        Fish_list = [line.strip() for line in file.readlines()]

    Message = target.split()
    Message_list = [word.rstrip('s') for word in Message]
    any_common = not set(Fish_list).isdisjoint(Message_list)
    if any_common:
        I.Return_Message = 'Fish Found'
    else:
        I.Return_Message = ''
