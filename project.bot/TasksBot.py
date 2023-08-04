import telebot
from telebot import types
from dictionary_sharp import tasks_c_sharp
from python_dictionary import python_tasks
from easy_task import easy
from medium_task import medium
from hard_task import hard
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





                                                       
keyboard_with_levels = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_with_levels.add(types.KeyboardButton("Easy Task"))
keyboard_with_levels.add(types.KeyboardButton("Medium Task"))
keyboard_with_levels.add(types.KeyboardButton("Hard Task"))
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
    btn1 = types.KeyboardButton("Task1")
    btn2 = types.KeyboardButton("Task2")
    btn3 = types.KeyboardButton("Task3")
    btn4 = types.KeyboardButton("Task4")
    btn5 = types.KeyboardButton("Task5")
    btn6 = types.KeyboardButton("Task6")
    btn7 = types.KeyboardButton("Task7")
    btn8 = types.KeyboardButton("Task8")
    btn9 = types.KeyboardButton("Task9")
    btn10 = types.KeyboardButton("Task10")
    markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8, btn9,btn10)

    bot.send_message(message.chat.id, text="Выбирай номер задачи", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == 'Task1')
def Task1 (message):
    bot.send_message(message.chat.id, text=easy[1])
@bot.message_handler(func=lambda message: message.text == 'Task2')
def Task2 (message):
    bot.send_message(message.chat.id, text=easy[2])
@bot.message_handler(func=lambda message: message.text == 'Task3')
def Task3 (message):
    bot.send_message(message.chat.id, text=easy[3])
@bot.message_handler(func=lambda message: message.text == 'Task4')
def Task4 (message):
    bot.send_message(message.chat.id, text=easy[4])  
@bot.message_handler(func=lambda message: message.text == 'Task5')
def Task5 (message):
    bot.send_message(message.chat.id, text=easy[5])  
@bot.message_handler(func=lambda message: message.text == 'Task6')
def Task6 (message):
    bot.send_message(message.chat.id, text=easy[6])
@bot.message_handler(func=lambda message: message.text == 'Task7')
def Task7 (message):
    bot.send_message(message.chat.id, text=easy[7])
@bot.message_handler(func=lambda message: message.text == 'Task8')
def Task8 (message):
    bot.send_message(message.chat.id, text=easy[8])
@bot.message_handler(func=lambda message: message.text == 'Task9')
def Task9 (message):
    bot.send_message(message.chat.id, text=easy[9])
@bot.message_handler(func=lambda message: message.text == 'Task10')
def Task10 (message):
    bot.send_message(message.chat.id, text=easy[10])    
@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_to_menu(message):
    bot.send_message(message.chat.id, 'Выберите уровень сложности задач:', reply_markup=keyboard_with_levels)






@bot.message_handler(func=lambda message: message.text == 'Medium Task')
def handle_stop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Task_1")
    btn2 = types.KeyboardButton("Task_2")
    btn3 = types.KeyboardButton("Task_3")
    btn4 = types.KeyboardButton("Task_4")
    btn5 = types.KeyboardButton("Task_5")
    btn6 = types.KeyboardButton("Task_6")
    btn7 = types.KeyboardButton("Task_7")
    btn8 = types.KeyboardButton("Task_8")
    btn9 = types.KeyboardButton("Task_9")
    btn10 = types.KeyboardButton("Task_10")
    markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8, btn9,btn10)
    bot.send_message(message.chat.id, text="Выбирай номер задачи", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == 'Task_1')
def Task_1 (message):
    bot.send_message(message.chat.id, text=medium[1])
@bot.message_handler(func=lambda message: message.text == 'Task_2')
def Task_2 (message):
    bot.send_message(message.chat.id, text=medium[2])
@bot.message_handler(func=lambda message: message.text == 'Task_3')
def Task_3 (message):
    bot.send_message(message.chat.id, text=medium[3]) 
@bot.message_handler(func=lambda message: message.text == 'Task_4')
def Task_4 (message):
    bot.send_message(message.chat.id, text=medium[4]) 
@bot.message_handler(func=lambda message: message.text == 'Task_5')
def Task_5 (message):
    bot.send_message(message.chat.id, text=medium[5])
@bot.message_handler(func=lambda message: message.text == 'Task_6')
def Task_6 (message):
    bot.send_message(message.chat.id, text=medium[6]) 
@bot.message_handler(func=lambda message: message.text == 'Task_7')
def Task_7 (message):
    bot.send_message(message.chat.id, text=medium[7]) 
@bot.message_handler(func=lambda message: message.text == 'Task_8')
def Task_8 (message):
    bot.send_message(message.chat.id, text=medium[8]) 
@bot.message_handler(func=lambda message: message.text == 'Task_9')
def Task_9 (message):
    bot.send_message(message.chat.id, text=medium[9])
@bot.message_handler(func=lambda message: message.text == 'Task_10')
def Task_10 (message):
    bot.send_message(message.chat.id, text=medium[10])  




@bot.message_handler(func=lambda message: message.text == 'Hard Task')
def handle_stop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1task")
    btn2 = types.KeyboardButton("2task")
    btn3 = types.KeyboardButton("3task")
    btn4 = types.KeyboardButton("4task")
    btn5 = types.KeyboardButton("5task")
    btn6 = types.KeyboardButton("6task")
    btn7 = types.KeyboardButton("7task")
    btn8 = types.KeyboardButton("8task")
    btn9 = types.KeyboardButton("9task")
    btn10 = types.KeyboardButton("10task")
    markup.add(btn1, btn2, btn3,btn4,btn5,btn6,btn7,btn8, btn9,btn10)
    bot.send_message(message.chat.id, text="Выбирай номер таски", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == '1task')
def task1(message):
    bot.send_message(message.chat.id, text=hard[1])
@bot.message_handler(func=lambda message: message.text == '2task')
def task2 (message):
    bot.send_message(message.chat.id, text=hard[2]) 
@bot.message_handler(func=lambda message: message.text == '3task')    
def task3 (message):
    bot.send_message(message.chat.id, text=hard[3]) 
@bot.message_handler(func=lambda message: message.text == '4task')
def task4 (message):
    bot.send_message(message.chat.id, text=hard[4])
@bot.message_handler(func=lambda message: message.text == '5task')  
def task5 (message):
    bot.send_message(message.chat.id, text=hard[5]) 
@bot.message_handler(func=lambda message: message.text == '6task')
def task6 (message):
    bot.send_message(message.chat.id, text=hard[6]) 
@bot.message_handler(func=lambda message: message.text == '7task')
def task7 (message):
    bot.send_message(message.chat.id, text=hard[7]) 
@bot.message_handler(func=lambda message: message.text == '8task')
def task8 (message):
    bot.send_message(message.chat.id, text=hard[8]) 
@bot.message_handler(func=lambda message: message.text == '9task')
def task9 (message):
    bot.send_message(message.chat.id, text=hard[9]) 
@bot.message_handler(func=lambda message: message.text == '10task')
def task10 (message):
    bot.send_message(message.chat.id, text=hard[10]) 



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




