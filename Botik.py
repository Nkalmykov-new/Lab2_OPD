import telebot
from telebot import types

bot = telebot.TeleBot('7067239330:AAEBRPDcD4D-03C0RF1VoiqLp_oFmzX60Qc')

@bot.message_handler(commands=['start'], func=lambda message: True)
def maine(message):
    makeup1 = types.InlineKeyboardMarkup(row_width=1)
    b11 = types.InlineKeyboardButton('Yes', callback_data='go')
    b21 = types.InlineKeyboardButton('No', callback_data='no_go')
    makeup1.row(b11, b21)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!\n'
                                      f'Готов начать игру? Yes/No', reply_markup=makeup1)

@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == 'right1':
        bot.edit_message_text('Всё верно, ведь сначала выполняется умножение, а потом сложение. Двигаемся дальше!',
                              chat_id=callback.message.chat.id,message_id=callback.message.message_id,
                              reply_markup=None)

        makeup2 = types.InlineKeyboardMarkup(row_width=1)
        b12 = types.InlineKeyboardButton('1937-1945', callback_data='bad')
        b22 = types.InlineKeyboardButton('1941-1945', callback_data='bad')
        b32 = types.InlineKeyboardButton('1939-1941', callback_data='bad')
        b42 = types.InlineKeyboardButton('1939-1945', callback_data='right2')
        makeup2.row(b12, b22)
        makeup2.row(b32, b42)
        bot.send_message(callback.message.chat.id, 'Укажите периоды Второй Мировой Войны', reply_markup=makeup2)

    elif callback.data == 'right2':
        bot.edit_message_text('Великая Отечественная началась в 1941, а Вторая Мировая в 1939. Идём дальше!',
                              chat_id=callback.message.chat.id,message_id=callback.message.message_id,
                              reply_markup=None)
        makeup3 = types.InlineKeyboardMarkup(row_width=1)
        b13 = types.InlineKeyboardButton('23', callback_data='bad')
        b23 = types.InlineKeyboardButton('15', callback_data='right3')
        b33 = types.InlineKeyboardButton('8', callback_data='bad')
        b43 = types.InlineKeyboardButton('12', callback_data='bad')
        makeup3.row(b13, b23)
        makeup3.row(b33, b43)
        bot.send_message(callback.message.chat.id, 'Сколько корпусов находится в ОмГТУ?', reply_markup=makeup3)

    elif callback.data == 'right3':
        bot.edit_message_text('Да, в ОмГТУ есть 15 учебных корпусов!',
                              chat_id=callback.message.chat.id,message_id=callback.message.message_id,
                              reply_markup=None)
        makeup4 = types.InlineKeyboardMarkup(row_width=1)
        b14 = types.InlineKeyboardButton('Франция', callback_data='right4')
        b24 = types.InlineKeyboardButton('Германия', callback_data='bad')
        b34 = types.InlineKeyboardButton('Испания', callback_data='bad')
        b44 = types.InlineKeyboardButton('Португалия', callback_data='bad')
        makeup4.row(b14, b24)
        makeup4.row(b34, b44)
        bot.send_message(callback.message.chat.id, 'Гавр - это город какой страны?', reply_markup=makeup4)

    elif callback.data == 'right4':
        bot.edit_message_text('Гавр(Le Havre) - город, расположенный на северо-западе Франции! Продолжаем путь!',
                              chat_id=callback.message.chat.id,message_id=callback.message.message_id,
                              reply_markup=None)
        makeupf = types.InlineKeyboardMarkup(row_width=1)
        b1f = types.InlineKeyboardButton('Из лопаты', callback_data='bad')
        b2f = types.InlineKeyboardButton('Из топора', callback_data='rightf')
        b3f = types.InlineKeyboardButton('Из шляпы', callback_data='ифв')
        b4f = types.InlineKeyboardButton('Из сапог', callback_data='bad')
        makeupf.row(b1f, b2f)
        makeupf.row(b3f, b4f)
        bot.send_message(callback.message.chat.id, 'Из чего варилась каша в русской сказке?', reply_markup=makeupf)

    elif callback.data == 'rightf':
        bot.edit_message_text('Поздравляю, вы прошли игру! Спасибо, что прошли, надеюсь, было интересно!',
                              chat_id=callback.message.chat.id,message_id=callback.message.message_id,
                              reply_markup=None)

    elif callback.data == 'bad':
        bot.edit_message_text('Чел, ты неверно ответил/a на вопрос',
                              chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              reply_markup=None)
    elif callback.data == 'go':
        bot.edit_message_text('Приступим!\n'
                              'Да начнется игра "Кто хочет стать миллионером?"(тот много хочет)\n'
                              'Надеюсь, вы прочитали правила игры!',
                              chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              reply_markup=None)
        makeup = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton('8', callback_data='bad')
        b2 = types.InlineKeyboardButton('6', callback_data='right1')
        b3 = types.InlineKeyboardButton('12', callback_data='bad')
        b4 = types.InlineKeyboardButton('4', callback_data='bad')
        makeup.row(b1, b2)
        makeup.row(b3, b4)
        bot.send_message(callback.message.chat.id, 'Внимание, первый вопрос! \n'
                                              'Первый вопрос: 2+2*2 = ?', reply_markup=makeup)
    elif callback.data == 'no_go':
        bot.edit_message_text('Возвращайтесь, когда будете готовы!',
                              chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              reply_markup=None)

    elif callback.data == 'Aut':
        makeupp = types.InlineKeyboardMarkup(row_width=1)
        bp1 = types.InlineKeyboardButton('Author', callback_data='Aut')
        bp2 = types.InlineKeyboardButton('Bot', callback_data='Bot')
        makeupp.row(bp1, bp2)
        bot.edit_message_text('Создатель:\n'
                              'Студент ОмГТУ\n'
                              'Курс обучения: 2\n'
                              'Группа: Ивт-223\n'
                              'Калмыков Никита Дмитриевич',
                              chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              reply_markup=makeupp)

    elif callback.data == 'Bot':
        makeupp = types.InlineKeyboardMarkup(row_width=1)
        bp1 = types.InlineKeyboardButton('Author', callback_data='Aut')
        bp2 = types.InlineKeyboardButton('Bot', callback_data='Bot')
        makeupp.row(bp1, bp2)
        bot.edit_message_text('Бот начал работать 26.04.2024, полностью не готов.\n'
                              'Предназначен для мини-версии игры "Кто хочет стать миллионером!"',
                              chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              reply_markup=makeupp)


@bot.message_handler(commands=['info'])
def maine(message):
    makeupp = types.InlineKeyboardMarkup(row_width=1)
    bp1 = types.InlineKeyboardButton('Author', callback_data='Aut')
    bp2 = types.InlineKeyboardButton('Bot', callback_data='Bot')
    makeupp.row(bp1, bp2)
    bot.send_message(message.chat.id, f'Выберите, какую информацию вы бы хотели увидеть:', reply_markup=makeupp)

@bot.message_handler(commands=['rules'])
def maine(message):
    bot.send_message(message.chat.id, f'Правила довольно простые:\n'
                                      f'Есть вопрос - ты на него отвечаешь.\n'
                                      f'Отвечаешь правильно - переходишь к следующему вопросу,\n'
                                      f'А в случае неудачи, ты заканчиваешь игру!\n'
                                      f'Надеюсь, всё понятно. Удачи!')

@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f'Hello, {message.from_user.username}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Id: {message.from_user.id}')
    elif message.text.lower() == 'no':
        bot.send_message(message.chat.id, 'Возвращайтесь, как будете готовы!')

bot.polling(none_stop=True)