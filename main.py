import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def adlasld(message):
	bot.send_message(message.chat.id, 'Привет!')

# простое число или нет
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

# RUN
bot.polling(none_stop=True)