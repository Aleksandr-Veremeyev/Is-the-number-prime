import telebot
import config
# import random
# from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Hello my friend! \nНапиши число, и я скажу простое ли оно!')
    # (message.chat.id, 'Привет!')

@bot.message_handler(content_types=['text'])
def lalala(message):
    # найти в message.text числа, если есть - то перевод на поиск выбранного вопроса.
    # если числа нет, то другое - (привет, пока, как дела, сколько времени)
    message2 = ''
    m1 = ''
    r = True
    if message.text.isdigit():
        # если сообщение - число
        try:
            # преобразование
            m1 = int(message.text)
        except:
            r = False
            m1 = 1
        
        # если все ок, то отправляем сообщение
        if r:
            # отправка сообщения
            a = isprime(m1)
            if a:
                 message2 = 'Это число простое!'
            elif a == False:
                 message2 = 'Это число составное!'
    else:
        message2 = message.text
        
            
    # end message
    bot.send_message(message.chat.id, message2)

# простое число или нет
def isprime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

# RUN
bot.polling(none_stop=True)