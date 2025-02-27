import telebot
import random
from telebot import types
# пакет для создания меню

bot = telebot.TeleBot('8190304206:AAENTor74c4q66tiYfcvV_UhZwEhMjfGMdo')

rules = "🎲 Правила игры.\n\nВы получаете 7 карт. Ваша задача сбросить все карты с руки. После того, как вы сбросили карты - вы берёте 6 карт. Потом 5, 4 ...\nПобедитель тот, кто первый останется без карт!"

start_message = "Я бот для игры в УНО!\nНапиши старт для старта игры."

#################
carts_count = 108
# 1-9 по две карты
# красная
# жёлтая
# зелёная
# синяя
# 0 - 4 карты разных цветов
# по 4 цвета * 2 штуки = 8 карт:
# пропуск_хода
# смена хода
# +2 карты
# +4 карты - ток 4 карты
# выбор цвета - ток 4 карты
#################

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# кнопки
item1 = types.KeyboardButton("Мои карты")
item2 = types.KeyboardButton(" ")
item3 = types.KeyboardButton("🎲 Правила игры.")
# реализация кнопок
markup.add(item1, item2, item3)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, start_message.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

priv = False
color = -1
run = True # False - ход бота
bot_gameRESET = False
#==========
player = []
bot_game = []
sel = ''
sel1 = ''
sel2 = ''
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "🎲 Правила игры.":
            bot.send_message(message.chat.id, rules)
    
    if message.chat.type == 'private':
        if message.text == "Мои карты":
            bot.send_message(message.chat.id, 'Ваши карты: \n' + '\n'.join(player))
    
    global priv
    global sel
    global sel1
    global sel2
    if priv == True:
        # 0жёл, 1син, 2зел, 3кр
        if message.text == "жёл":
            bot.send_message(message.chat.id, 'Вы выбрали жёлтый цвет.')
            color = 0
            bot.send_message(message.chat.id, 'Бот ходит жёлтым цветом.')
            run = False
            bot_gaming(1, color)
        elif message.text == "син":
            bot.send_message(message.chat.id, 'Вы выбрали синий цвет.')
            color = 1
            bot.send_message(message.chat.id, 'Бот ходит синим цветом.')
            run = False
            bot_gaming(1, color)
        elif message.text == "зел":
            bot.send_message(message.chat.id, 'Вы выбрали зелёный цвет.')
            color = 2
            bot.send_message(message.chat.id, 'Бот ходит зелёным цветом.')
            run = False
            bot_gaming(1, color)
        elif message.text == "кр":
            bot.send_message(message.chat.id, 'Вы выбрали красный цвет.')
            color = 3
            bot.send_message(message.chat.id, 'Бот ходит красным цветом.')
            run = False
            bot_gaming(1, color)
        priv = False
    
    if message.text == 'старт':
        game = "Начало игры в уно."
        bot.send_message(message.chat.id, game)
        carts = ['0 кр', '0 син', '0 зел', '0 жёл', '1 кр', '1 кр', '1 син', '1 син', '1 жёл', '1 жёл', '1 зел', '1 зел',
        '2 кр', '2 кр', '2 син', '2 син', '2 жёл', '2 жёл', '2 зел', '2 зел', 
        '3 кр', '3 кр', '3 син', '3 син', '3 жёл', '3 жёл', '3 зел', '3 зел',
        '4 кр', '4 кр', '4 син', '4 син', '4 жёл', '4 жёл', '4 зел', '4 зел',
        '5 кр', '5 кр', '5 син', '5 син', '5 жёл', '5 жёл', '5 зел', '5 зел',
        '6 кр', '6 кр', '6 син', '6 син', '6 жёл', '6 жёл', '6 зел', '6 зел',
        '7 кр', '7 кр', '7 син', '7 син', '7 жёл', '7 жёл', '7 зел', '7 зел',
        '8 кр', '8 кр', '8 син', '8 син', '8 жёл', '8 жёл', '8 зел', '8 зел',
        '9 кр', '9 кр', '9 син', '9 син', '9 жёл', '9 жёл', '9 зел', '9 зел',
        '(/) кр', '(/) кр', '(/) син', '(/) син', '(/) жёл', '(/) жёл', '(/) зел', '(/) зел',
        '-> кр', '-> кр', '-> син', '-> син', '-> жёл', '-> жёл', '-> зел', '-> зел',
        '+2 кр', '+2 кр', '+2 син', '+2 син', '+2 жёл', '+2 жёл', '+2 зел', '+2 зел',
        '+4', 'X4', '+4', 'X4', '+4', 'X4', '+4', 'X4']
        for i in range(7):
            pl0 = carts.pop(random.randint(0, len(carts)))
            player.append(pl0)

        for i in range(7):
            bg0 = carts.pop(random.randint(0, len(carts)))
            bot_game.append(bg0)
        #bot.send_message(message.chat.id, 'Bot: ' + ' '.join(bot_game))

        one_cart = carts[random.randint(0, len(carts))]
        bot.send_message(message.chat.id, 'Карта: ' + one_cart)
        bot.send_message(message.chat.id, 'Первый ход игрока.')
        
    for i in range(0, len(player)):
        if message.text == player[i]:
            if message.text == "X4":
                bot.send_message(message.chat.id, 'Выберите цвет: ')
                priv = True
            elif message.text == "+4":
                for i in range(4):
                    pl0 = carts.pop(random.randint(0, len(carts)))
                    bot_game.append(pl0)
                bot.send_message(message.chat.id, 'Выберите цвет: ')
                priv = True
            elif message.text.replace(' ', '')[0:2] == "+2":
                for i in range(2):
                    pl0 = carts.pop(random.randint(0, len(carts)))
                    bot_game.append(pl0)
            elif message.text.replace(' ', '')[0:2] == "->" or message.text.replace(' ', '')[0:3] == "(/)":
                bot.send_message(message.chat.id, 'Бот пропускает ход, вы ходите снова.')
            elif message.text.replace(' ', '')[0:1] == "0":
                bot.send_message(message.chat.id, 'Ваши карты становятся картами бота, а карты бота вашими.')
                # .
            else:
                if message.text.replace(' ', '')[0] == "1":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "2":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "3":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "4":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "5":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "6":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "7":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "8":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
                if message.text.replace(' ', '')[0] == "9":
                    t = message.text.replace(' ', '')[1:-1]
                    if t == 'жёл':
                        color = 0
                    elif t == 'син':
                        color = 1
                    elif t == 'зел':
                        color = 2
                    elif t == 'кр':
                        color = 3
            try:
                a0 = message.text.replace(' ', '')[0]
                b0 = message.text.replace(' ', '')[1:-1]
            except:
                bot.send_message(message.chat.id, ': ')
            bot.send_message(message.chat.id, 'Вы сходили: ' + player[i])
            sel = player[i]
            sel1 = sel[0]
            sel2 = sel.strip()[1:-1]
            a = player.pop(i)

def bot_gaming():
    # 0 - ход
    # 1 - ход с выбранным цветом
    pass

def next():
    # вернуть True если есть ход
    pass

# RUN
bot.polling(none_stop=True)