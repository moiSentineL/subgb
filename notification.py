import requests

def send(bot_message):
    
    bot_token = '5551558898:AAHjJxvOgmoxKKjNhvSizqKggrEE1Kvj0qk'
    bot_chatID = '1316756456'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

# test = send("*moanarr*\nTesting Telegram bot")
# print(test)