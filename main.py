"""
Telegram bot for evaluation arbitrary python code
"""

import os
import telebot

bot = telebot.TeleBot(os.environ['API_TOKEN'])


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    """
    Welcome message function
    :param message: message
    :return: None
    """
    bot.reply_to(message, """
        I can do any python code, for example I can serve as calculator
    """)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def code_execute(message):
    """
    function for arbitrary python code execution
    :param message: code
    :return: None
    """
    result = eval(message.text)  # pylint: disable=W0123
    bot.reply_to(message, str(result))


bot.infinity_polling()
