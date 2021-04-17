import telebot
from telebot import types
from ques_list import questions_for_company, funny_questions, embar_ques, vulgar_questions
from dare_list import dare_funny, dare_for_company, vulgar_dare, very_vulgar_dare
import random

bot = telebot.TeleBot('1773643559:AAHpWHVmg3PhTyJ_8oHXqFZEwNrENHsxREs', parse_mode=None)
ques_numbers_list = []
dare_numbers_list = []
questions_pool = []
dare_pool = []


def name_checker(name):
    if name is not None:
        return name
    else:
        return ''


def photo_sender(situation):
    index_photo = open('pictures/app-icon_hudd4a76fdd1418ef19e5c7e82173a6378_67317_1024x0_resize_q75_box.jpeg', 'rb')
    rules_photo = open('pictures/reules.png', 'rb')
    contacts_photo = open('pictures/Контакты.png', 'rb')
    error_photo = open("pictures/Pole-ob'ekta-nedostupno-dlya-zapisi-1S.jpeg", 'rb')
    if situation == 'welcome':
        return index_photo
    if situation == 'rules':
        return rules_photo
    if situation == 'contacts':
        return contacts_photo
    if situation == 'error':
        return error_photo


@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    start_game = types.KeyboardButton('Начать игру')
    game_rules = types.KeyboardButton('Правила игры')
    contacts = types.KeyboardButton('Связаться с разработчиком')
    markup.add(start_game, game_rules, contacts)
    send_mess = f"<b>Привет {name_checker(message.from_user.first_name)} {name_checker(message.from_user.last_name)}</b>!" \
                f"\nЭтот бот поможет тебе с выбором вопросов и действий для игры правда или действие!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    bot.send_photo(message.chat.id, photo_sender(situation="welcome"), parse_mode='html',
                   caption='<b>Выбери, что тебя интересует?</b>')


@bot.message_handler(content_types=['text'])
def rules(message):
    message_from_user = message.text.strip().lower()

    if message_from_user == 'правила игры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start_game = types.KeyboardButton('Начать игру')
        contacts = types.KeyboardButton('Связаться с разработчиком')
        markup.add(start_game, contacts)
        returned_message = 'В игре играют от 2 и более людей.\nСначала компания решает, с кого начнётся игра (за вас это ' \
                           'сделает бот).\nПервого спрашивают: «Правда или действие?». Если игрок отвечает: «Правда», то ' \
                           'он должен будет правдиво ответить на вопрос, который ему будет задан. Если он выбирает ' \
                           'действие, то должен будет выполнить задание (совершить задаваемое ему действие).\nПосле того, ' \
                           'как игрок ответил на вопрос или выполнил задание, то он спрашивает: «Правда или действие?» ' \
                           'уже следующего (по часовой стрелке). И так далее.\nДабы игра была более интересна, выбрать правду рекомендовано ' \
                           'не более 2 раз подряд!\n<b>Дерзайте! Да прибудет с вами веселье!</b>'
        bot.send_photo(message.chat.id, photo_sender(situation="rules"))
        bot.send_message(message.chat.id, returned_message, parse_mode='html', reply_markup=markup)

    elif message_from_user == 'связаться с разработчиком':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start_game = types.KeyboardButton('Начать игру')
        game_rules = types.KeyboardButton('Правила игры')
        markup.add(start_game, game_rules)
        returned_message = 'Для связи с администратором данного бота, напиши @musicallifeinchine'
        bot.send_message(message.chat.id, returned_message, reply_markup=markup)
        bot.send_photo(message.chat.id, photo_sender(situation='contacts'), caption="<b>Не стейсняйся, пиши!</b>",
                       parse_mode='html')

    elif message_from_user == 'начать игру':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        returned_message = """Задайте темы для вопросов игры (можно выбрать несколько тем, для этого в ответ напишите слово "Вопросы" и номера тем через пробел, например, если вы выбираете темы "забавные" и "смущающие", напишите в ответ - Вопросы 2 4).\n
        Темы вопросов:
        1) Вопросы для компании;
        2) Забавные вопросы;
        3) Пошлые вопросы;
        4) Смущающие вопросы\n\nПосле окончания выбора Вы перейдете в выбор тем для действий. 
        Немного терпения! =)"""
        game_end = types.KeyboardButton('Закончить игру')
        markup.add(game_end)
        bot.send_message(message.chat.id, returned_message, reply_markup=markup)

    elif 'вопросы' in message_from_user:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        returned_message = """
        Спасибо! Выбор сделан! Выбери темы для действий (выбор также как и с вопросами, напиши слово "Действия" и номера тем через пробел):
        1) Действия для компании;
        2) Забавные и слегка (самый минимум) пошлые действия;
        3) Горячие действия (внимание, очень горячо!);
        4) Веселый действия.
        """
        for i in message_from_user:
            if i.isnumeric():
                ques_numbers_list.append(i)
        if '1' in ques_numbers_list:
            for j in questions_for_company:
                questions_pool.append(j)
        if '2' in ques_numbers_list:
            for k in funny_questions:
                questions_pool.append(k)
        if '3' in ques_numbers_list:
            for m in vulgar_questions:
                questions_pool.append(m)
        if '4' in ques_numbers_list:
            for h in embar_ques:
                questions_pool.append(h)
        game_end = types.KeyboardButton('Закончить игру')
        bot.send_message(message.chat.id, returned_message, reply_markup=markup)
        markup.add(game_end)

    elif 'действия' in message_from_user:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        returned_message = """
        Хороший выбор! Начнем игру?! Если готов - нажимай "начать"!
        """
        for i in message_from_user:
            if i.isnumeric():
                dare_numbers_list.append(i)
        if '1' in dare_numbers_list:
            for j in dare_for_company:
                dare_pool.append(j)
        if '2' in dare_numbers_list:
            for k in vulgar_dare:
                dare_pool.append(k)
        if '3' in dare_numbers_list:
            for m in very_vulgar_dare:
                dare_pool.append(m)
        if '4' in dare_numbers_list:
            for h in dare_funny:
                dare_pool.append(h)
        start_game_this_fkn_game = types.KeyboardButton('Начать эту чертову игру!')
        game_end = types.KeyboardButton('Закончить игру')
        markup.add(start_game_this_fkn_game, game_end)
        bot.send_message(message.chat.id, returned_message, reply_markup=markup)

    elif message_from_user == 'начать эту чертову игру!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        returned_mess = 'Правда или действие?'
        truth = types.KeyboardButton('Правда 😉')
        dare = types.KeyboardButton('Действие 😍')
        game_end = types.KeyboardButton('Закончить игру')
        markup.add(truth, dare, game_end)
        bot.send_message(message.chat.id, returned_mess, reply_markup=markup)

    elif message_from_user == 'правда 😉':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        return_ques = random.choice(questions_pool)
        truth = types.KeyboardButton('Правда 😉')
        dare = types.KeyboardButton('Действие 😍')
        game_end = types.KeyboardButton('Закончить игру')
        markup.add(truth, dare, game_end)
        bot.send_message(message.chat.id, return_ques, reply_markup=markup)

    elif message_from_user == 'действие 😍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        return_ques = random.choice(dare_pool)
        truth = types.KeyboardButton('Правда 😉')
        dare = types.KeyboardButton('Действие 😍')
        game_end = types.KeyboardButton('Закончить игру')
        markup.add(truth, dare, game_end)
        bot.send_message(message.chat.id, return_ques, reply_markup=markup)

    elif message_from_user == 'закончить игру':
        questions_pool.clear()
        dare_pool.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start_game = types.KeyboardButton('Начать игру')
        game_rules = types.KeyboardButton('Правила игры')
        contacts = types.KeyboardButton('Связаться с разработчиком')
        markup.add(start_game, game_rules, contacts)
        send_mess = f"<b>Спасибо за игру {name_checker(message.from_user.first_name)} {name_checker(message.from_user.last_name)}</b>!" \
                    f"\nСыграем еще раз? 🥳\nЭтот бот поможет тебе с выбором вопросов и действий для игры правда или действие!"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        bot.send_photo(message.chat.id, photo_sender(situation="welcome"), parse_mode='html',
                       caption='<b>Выбери, что тебя интересует?</b>')

    # В случае отправки неизвестной команды:

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start_game = types.KeyboardButton('Начать игру')
        game_rules = types.KeyboardButton('Правила игры')
        contacts = types.KeyboardButton('Связаться с разработчиком')
        markup.add(start_game, game_rules, contacts)
        returned_message = 'Такой команды нет! Не мухлюй!'

        bot.send_message(message.chat.id, returned_message, reply_markup=markup)
        bot.send_photo(message.chat.id, photo_sender(situation='error'),
                       caption="<b>Доступные команды в виде кнопок ниже!</b>",
                       parse_mode='html')


if __name__ == '__main__':
    bot.polling()
