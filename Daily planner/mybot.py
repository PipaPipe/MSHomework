import telebot
from telebot import types
from Class_task import Task

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

# Создаём класс
main_task_list = Task()

@bot.message_handler(commands=['start'])
def start(message):
    # Начало работы бота
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я — бот-ежедневник, сейчас покажу тебе весь функционал!")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)
        bot.send_message(message.from_user.id, text="Ты готов?", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Напиши команду /start, чтобы всё заработало!")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Вложенное меню бота
    if call.data == "keyboard":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)
        bot.edit_message_text('Ты готов?', call.message.chat.id, call.message.message_id, reply_markup=keyboard)
    # Основное функциональное меню бота
    elif call.data == "yes":
        keyboard_next = types.InlineKeyboardMarkup()
        create_task_but = types.InlineKeyboardButton(text='Создать задачу', callback_data='create_task')
        delete_task_but = types.InlineKeyboardButton(text='Удалить задачу', callback_data='delete_task')
        edit_task_but = types.InlineKeyboardButton(text='Редактировать задачу', callback_data='edit_task')
        viewall_task_but = types.InlineKeyboardButton(text='Увидеть все задачи', callback_data='viewall_task')
        #back = types.InlineKeyboardButton(text='Назад', callback_data='keyboard')
        keyboard_next.add(create_task_but, delete_task_but, edit_task_but, viewall_task_but)
        bot.edit_message_text('Что будем делать?', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_next)
    elif call.data == "no":
        bot.send_message(call.from_user.id, text='Очень жаль:(')
    # Меню создания задачи
    elif call.data == "create_task":
        keyboard_task = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        keyboard_task.add(back)
        bot.edit_message_text('Здесь вы можете создать новую задачу!', call.message.chat.id, call.message.message_id,
                              reply_markup=keyboard_task)
    # Меню удаления задачи

    elif call.data == "delete_task":
        keyboard_task = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        keyboard_task.add(back)
        bot.edit_message_text('Здесь вы можете удалить существующую задачу!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_task
                              )
    # Меню редактирования задачи
    elif call.data == "edit_task":
        keyboard_task = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        keyboard_task.add(back)
        bot.edit_message_text('Здесь вы можете редактировать задачи, выберите задачу для редактирования!',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_task)
    # Меню, в котором находится список всех задач
    elif call.data == "viewall_task":

        keyboard_task = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='yes')
        keyboard_task.add(back)
        bot.edit_message_text(main_task_list.viewall_task(),
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_task)

bot.polling(none_stop=True, interval=0)

# Добавить методы класса Task в меню бота
