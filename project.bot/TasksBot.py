import telebot
from telebot import types
import config
import json
import os
import random
API_TOKEN = '6481883927:AAEB7cwviE0sm65fSsboLyUXBDi6krKAYe4'
bot = telebot.TeleBot(API_TOKEN)

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
Home_work1 = []
@bot.message_handler(commands = '1)Home_Works')
def send_python_tasks(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('1)Home_Works')
    btn2 = types.KeyboardButton("HW №2")
    btn3 = types.KeyboardButton("HW №3")
    btn4 = types.KeyboardButton("HW №4")
    markup.add(btn1, btn2,btn3,btn4)
    bot.send_message(message.chat.id, text="Выбирай номер дз", reply_markup=markup)
#Собирался заполнить список с задачами
@bot.message_handler(commands= ["1)Home_Works"])
def HW_1 (message):
        Home_work1.append('1)Найдите сумму цифр трехзначного числа n.')
        Home_work1.append('2)Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.')
        bot.send_message(message.chat.id, text ='Домашка загружена' )
   




    #Можно ли использовать конструкцию switch/case 
    #Можно ли использовать if/elif/elif
    #Как использовать тут списки
    #А может быть словарь??????

# @bot.message_handler(func=lambda message: message.text == 'HW №1 ')
# def handle_start(message):
#     bot.send_message(message.chat.id, text="1)Найдите сумму цифр трехзначного числа n.")
    # user_markup.row("2 Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей")
                    
    
                    

   
    # file_path = "C:/Games/hw/HomeWork_GB.txt"
    # with open(file_path, 'rb') as doc:
    #     bot.send_message(message.from_user.id,'Тут все задачи')
    #     bot.send_document(message.chat.id, doc)

bot.polling()







