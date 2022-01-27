from slack import WebClient


def slack_bot_send_text(bot_message):
    bot_token = 'xoxb-2462030320881-2476605325270-EQgciBh4LJ0uSLF4luRgH5J3'
    channel = '#allure_report'

    client = WebClient(token=bot_token)
    client.chat_postMessage(channel=channel, text=bot_message)
