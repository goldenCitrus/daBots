import requests

def send_random_gif(info):
    message_str = info.message.content.replace(' ', '-')
    print(message_str)
    response = requests.get(f'https://tenor.com/search/{message_str}-gifs')


    print(response.text)

