import telebot
import config
import random
from telebot import types

# добавить клавиатуру, (рандомное число, как дела) markup

bot = telebot.TeleBot(config.TOKEN)

# consts
D = 0

@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("🎮 Игра в крестики-нолики")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Hello my friend! \nЯ бот, который знает какие числа простые, а какие нет. \nНапиши любое число, и я скажу тебе: простое оно или нет!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    # (message.chat.id, 'Привет!')

@bot.message_handler(content_types=['text'])
def lalala(message):
    # найти в message.text числа, если есть - то перевод на поиск выбранного вопроса.
    # если числа нет, то другое - (привет, пока, как дела, сколько времени)
    message_end = ''
    number = ''
    cikl = True
    if message.text.isdigit():
        # если сообщение - число
        try:
            # преобразование
            number = int(message.text)
        except:
            cikl = False
            number = 1
        # если все ок, то отправляем сообщение
        if cikl:
            # отправка сообщения
            mess = isprime(number)
            if mess:
                message_end = 'Число ' + str(number) + ' простое!'
                # число X простое
                # число X составное
                # это число -простое -составное
                # это число составное, так как 2 * 3 = 6.
                #  
            else:
                message_end = 'Число ' + str(number) + ' составное!'
                # из функции isprime найти 
    elif message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            pass
            # bot.send_message(message.chat.id, 'Я не знаю что ответить')
            # если число не указано
            # message_end = "Вы не выбрали никакого числа!"
    # ================
    if (message.text == "Как дела?") or (message.text == "как дела?") or (message.text == "Как дела") or (message.text == "какдела") or (message.text == "какдела?"):
        d = ["Хорошо", "нормально", "Лучше некуда.", "неплохо", "Здорово!", "окей", "замечательно", "прекрасно"]
        # процесс изменения D
        message_end = d[random.randint(0, 8)]
        # D = 1
        # pass
    
    if (message.text == "пока") or (message.text == "Пока") or (message.text == "пока.") or (message.text == "Пока."):
        message_end = "Пока!"

    if (message.text == "привет") or (message.text == "Привет"):
        message_end = "Привет"

    

    # отправка ответа, end message
    if message_end != '':
        bot.send_message(message.chat.id, message_end)

# функция определения простого числа, методом while.
def isprime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ТЕСТ")
    
    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)

# Работает:
# приветствие +(ток при /start)

# TODO:
# зависание, подвисание.
# больше текста добавить.
# функцию добавить (1, 2)

# добавление функций...
# изменить функцию isprime так, чтобы можно было получить числа, составляющие.
# 1. показывает числа из которых состоит, в случае если оно составное
# 2. показывает док. что оно простое
# -+Добавить функцию рандомного числа (например чтобы потом определить уже на нём простое оно или нет)
# 3. Добавить функцию генерации пароля, по заданным вариантам (только числа, только буквы, символы...)
# 3.1. Проверка пароля - хороший пароль или плохой.
# Экспериментально: проверка файла на наличие вирусов.