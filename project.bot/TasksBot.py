import telebot
from telebot import types
import config
import os
import random
API_TOKEN = '6481883927:AAEB7cwviE0sm65fSsboLyUXBDi6krKAYe4'
bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('/start', '/stop')
#     user_markup.row('Easy Task', 'Medium Task', 'Лютая жесть Task','Задачи GeekBrains')
    
#     if str(message.from_user.id) == "734890426":
#         bot.send_message(message.chat.id, 'здароу'.format(message.from_user), reply_markup=user_markup)
#     else:
#         bot.send_message(message.chat.id, text="Привет ! Я тестовый бот для решения задач".format(message.from_user.first_name), reply_markup=user_markup)

# @bot.message_handler(commands=['stop'])
# def handle_stop(message):
#     hide_markup = types.ReplyKeyboardRemove()
#     bot.send_message(message.from_user.id, "до новых встреч", reply_markup=hide_markup)

# @bot.message_handler(commands='Задачи GeekBrains')
# def handle_stop(message):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("С#")
#         button2 = types.KeyboardButton("Python")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Выбирайте", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == 'Задачи GeekBrains')
# def send_geekbrains_tasks(message):
#     file_path = "C:/Games/hw/HomeWork_GB.txt"
#     with open(file_path, 'rb') as doc:
#         bot.send_message(message.from_user.id,'Тут все задачи')
#         bot.send_document(message.chat.id, doc)


# bot.polling()
        
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # user_markup.row('/start', '/stop')
    user_markup.row('Easy Task', 'Medium Task', 'Лютая жесть Task','Задачи GeekBrains')
    
    if str(message.from_user.id) == "734890426":
        bot.send_message(message.chat.id, 'здароу'.format(message.from_user), reply_markup=user_markup)
    else:
        bot.send_message(message.chat.id, text="Привет ! Я тестовый бот для решения задач".format(message.from_user.first_name), reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "до новых встреч", reply_markup=hide_markup)

@bot.message_handler(func=lambda message: message.text == 'Задачи GeekBrains')
def send_geekbrains_tasks(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("С#")
    button2 = types.KeyboardButton("Python")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="Выбирай раздел домашки", reply_markup=markup)

    # file_path = "C:/Games/hw/HomeWork_GB.txt"
    # with open(file_path, 'rb') as doc:
    #     bot.send_message(message.from_user.id,'Тут все задачи')
    #     bot.send_document(message.chat.id, doc)

bot.polling()





