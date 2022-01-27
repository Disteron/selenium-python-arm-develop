import requests


def telegram_bot_send_text(bot_message):
    bot_token = '1956238082:AAH81f7cW0kR6SIuMsYh7QyVuYY_nU5Sj5w'
    bot_chatID = '-1001509453518'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
