import requests
import configparser

# ConfigParser to parse ini
config = configparser.ConfigParser()
config.read('notif.ini')

# Telegram Bot Credentials
bot_token = config.get('Credentials', 'token')
bot_chatID = config.get('Credentials', 'chatID')

title= config.get('Pattern', 'title')
message= config.get('Pattern', 'message')

def send(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response.json()
