import telebot
from telebot import types
from dictionary_sharp import tasks_c_sharp
from python_dictionary import python_tasks
import pyodbc


API_TOKEN = '6481883927:AAEB7cwviE0sm65fSsboLyUXBDi6krKAYe4'
bot = telebot.TeleBot(API_TOKEN)
# лог юзеров
def log(message):
    
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                          message.from_user.last_name,
                                                          str(message.from_user.id), message.text))


def connect_to_database():
    try:
        #прикручиваю путь к бд для коннекта
        connection_string = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Тёмич\Desktop\Database21.accdb;'
        connection = pyodbc.connect(connection_string)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Подключение к базе данных
connection = connect_to_database()
if connection:
    print("Connected to the database successfully!")
else:
    print("Failed to connect to the database.")





                                                       

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/start', '/stop')
    user_markup.row('Easy Task', 'Medium Task', 'Hard Task', 'Задачи GeekBrains')
    
    if str(message.from_user.id) == "734890426":
        bot.send_message(message.chat.id, 'здароу'.format(message.from_user), reply_markup=user_markup)
    else: 
        bot.send_message(message.chat.id, text="Привет, я маленький проект, для упрощения поиска задач в нашей школе".format(message.from_user.first_name), reply_markup=user_markup)
    log(message)
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Все-го хоро-шего!", reply_markup=hide_markup)
    log(message)
@bot.message_handler(func=lambda message: message.text == 'Easy Task')
def handle_stop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "в процессе)", reply_markup=markup)
  

@bot.message_handler(func=lambda message: message.text == 'Medium Task')
def handle_stop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "в процессе)", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Лютая жесть Task')
def handle_stop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "в процессе)", reply_markup=markup)


# создал кнопку 'Задачи GeekBrains' и функцию с добавлением выборки языка домашки
@bot.message_handler(func=lambda message: message.text == 'Задачи GeekBrains')

def send_geekbrains_tasks(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("С#")
    button2 = types.KeyboardButton("Python")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="Выбирай раздел домашки", reply_markup=markup)
    log(message)
# Кнопки с шарпом

@bot.message_handler(func=lambda message: message.text == 'С#')
def send_python_tasks(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1)Home_Work")
    btn2 = types.KeyboardButton("2)Home_Work")
    btn3 = types.KeyboardButton("3)Home_Work")
    btn4 = types.KeyboardButton("4)Home_Work")
    btn5 = types.KeyboardButton("5)Home_Work")
    btn6 = types.KeyboardButton("6)Home_Work")
    btn7 = types.KeyboardButton("7)Home_Work")
    btn8 = types.KeyboardButton("8)Home_Work")
    btn9 = types.KeyboardButton("9)Home_Work")
    markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8, btn9)
    bot.send_message(message.chat.id, text="Выбирай номер домашки", reply_markup=markup)
    log(message)
@bot.message_handler(func=lambda message: message.text == '1)Home_Work')
def Hw1(message):
    bot.send_message(message.chat.id, text=tasks_c_sharp[1])
    bot.send_message(message.chat.id, text=tasks_c_sharp[2])
    bot.send_message(message.chat.id, text=tasks_c_sharp[3])
    bot.send_message(message.chat.id, text=tasks_c_sharp[4])
    bot.send_message(message.chat.id,text=tasks_c_sharp[5])

    log(message)
@bot.message_handler(func=lambda message: message.text== '2)Home_Work')
def Hw2(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[6])
    bot.send_message(message.chat.id,text=tasks_c_sharp[7])
    bot.send_message(message.chat.id,text=tasks_c_sharp[8])
    bot.send_message(message.chat.id,text=tasks_c_sharp[9])
    bot.send_message(message.chat.id,text=tasks_c_sharp[10])
    log(message)
@bot.message_handler(func=lambda message: message.text== '3)Home_Work')
def Hw3(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[11])
    bot.send_message(message.chat.id,text=tasks_c_sharp[12])
    bot.send_message(message.chat.id,text=tasks_c_sharp[13])
    bot.send_message(message.chat.id,text=tasks_c_sharp[14])
    bot.send_message(message.chat.id,text=tasks_c_sharp[15])
    log(message)
@bot.message_handler(func=lambda message: message.text== '4)Home_Work')
def Hw4(message):

    bot.send_message(message.chat.id,text=tasks_c_sharp[16])
    bot.send_message(message.chat.id,text=tasks_c_sharp[17])
    bot.send_message(message.chat.id,text=tasks_c_sharp[18])
    bot.send_message(message.chat.id,text=tasks_c_sharp[19])
    log(message)
@bot.message_handler(func=lambda message: message.text== '5)Home_Work')
def Hw5(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[20])
    bot.send_message(message.chat.id,text=tasks_c_sharp[21])
    bot.send_message(message.chat.id,text=tasks_c_sharp[22])
    bot.send_message(message.chat.id,text=tasks_c_sharp[23])
    log(message)
@bot.message_handler(func=lambda message: message.text== '6)Home_Work')
def Hw6(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[24])
    bot.send_message(message.chat.id,text=tasks_c_sharp[25])
    bot.send_message(message.chat.id,text=tasks_c_sharp[26])
    bot.send_message(message.chat.id,text=tasks_c_sharp[27])  
    log(message)
@bot.message_handler(func=lambda message: message.text== '7)Home_Work')
def Hw7(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[28])
    bot.send_message(message.chat.id,text=tasks_c_sharp[29])
    bot.send_message(message.chat.id,text=tasks_c_sharp[30])
    log(message)
@bot.message_handler(func=lambda message: message.text== '8)Home_Work')
def Hw8(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[31])
    bot.send_message(message.chat.id,text=tasks_c_sharp[32])
    bot.send_message(message.chat.id,text=tasks_c_sharp[33])
    bot.send_message(message.chat.id,text=tasks_c_sharp[34])
    bot.send_message(message.chat.id,text=tasks_c_sharp[35]) 
          
    log(message)
@bot.message_handler(func=lambda message: message.text== '9)Home_Work')
def Hw9(message):
    bot.send_message(message.chat.id,text=tasks_c_sharp[36])
    bot.send_message(message.chat.id,text=tasks_c_sharp[37])
    bot.send_message(message.chat.id,text=tasks_c_sharp[38])      
    log(message)


    # Кнопки к дз по питону
@bot.message_handler(func=lambda message: message.text == 'Python')
def send_python_tasks(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1)Home_Works")
    btn2 = types.KeyboardButton("2)Home_Works")
    btn3 = types.KeyboardButton("3)Home_Works")
    btn4 = types.KeyboardButton("4)Home_Works")
    btn5 = types.KeyboardButton("5)Home_Works")
    btn6 = types.KeyboardButton("6)Home_Works")
    btn7 = types.KeyboardButton("7)Home_Works")
    btn8 = types.KeyboardButton("8)Home_Works")
    btn9 = types.KeyboardButton("9)Home_Works")
    markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    bot.send_message(message.chat.id, text="Выбирай номер домашки", reply_markup=markup)
    log(message)
# добавляю функции, кнопки с номерами задач, в которых будет распечатываться задача

@bot.message_handler(func=lambda message: message.text == '1)Home_Works')
def HW_1(message):
    bot.send_message(message.chat.id, text=python_tasks[1])
    bot.send_message(message.chat.id, text=python_tasks[2])
    bot.send_message(message.chat.id, text=python_tasks[3])
    bot.send_message(message.chat.id, text=python_tasks[4])
    log(message)
@bot.message_handler(func=lambda message: message.text == '2)Home_Works')
def HW_2(message):
    bot.send_message(message.chat.id, text=python_tasks[5])
    bot.send_message(message.chat.id, text=python_tasks[6])
    bot.send_message(message.chat.id, text=python_tasks[7])
    log(message)
@bot.message_handler(func=lambda message: message.text == '3)Home_Works')
def HW_3(message):
    bot.send_message(message.chat.id, text=python_tasks[8])
    bot.send_message(message.chat.id, text=python_tasks[9])
    bot.send_message(message.chat.id, text=python_tasks[10])
    log(message)
@bot.message_handler(func=lambda message: message.text == '4)Home_Works')
def HW_4(message):
    bot.send_message(message.chat.id, text=python_tasks[11])
    bot.send_message(message.chat.id, text=python_tasks[12]) 
    log(message)
@bot.message_handler(func=lambda message: message.text == '5)Home_Works')
def HW_5(message):
    bot.send_message(message.chat.id, text=python_tasks[13])
    bot.send_message(message.chat.id, text=python_tasks[14])    
    log(message)
@bot.message_handler(func=lambda message:message.text =='6)Home_Works')
def HW_6(message):
    bot.send_message(message.chat.id, text=python_tasks[15])
    bot.send_message(message.chat.id, text=python_tasks[16]) 
    log(message)
@bot.message_handler(func=lambda message: message.text =='7)Home_Works')
def HW_7(message):
    bot.send_message(message.chat.id, text=python_tasks[17])
    bot.send_message(message.chat.id, text=python_tasks[18]) 
@bot.message_handler(func=lambda message: message.text =='8)Home_Works')    
def HW_8(message):
    bot.send_message(message.chat.id, text=python_tasks[19])
@bot.message_handler(func=lambda message: message.text =='9)Home_Works')    
def HW_9(message):
    bot.send_message(message.chat.id, text=python_tasks[20])
    bot.send_message(message.chat.id, text=python_tasks[21])



bot.polling()




