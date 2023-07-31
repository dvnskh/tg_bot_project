import telebot
from telebot import types
# import config
# import json
# import os
# import random
API_TOKEN = '6481883927:AAEB7cwviE0sm65fSsboLyUXBDi6krKAYe4'
bot = telebot.TeleBot(API_TOKEN)

# пишу лог юзеров
def log(message):
    # print("Нажал кнопку")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                          message.from_user.last_name,
                                                          str(message.from_user.id), message.text))
                                                              

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('/start', '/stop')
    user_markup.row('Easy Task', 'Medium Task', 'Лютая жесть Task', 'Задачи GeekBrains')
    
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
@bot.message_handler(func=lambda message: message.text== '1)Home_Work')
def Hw1(message):
    bot.send_message(message.chat.id, text = '1)Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.   Пример: a = 5; b = 7 -> max = 7a = 2 b = 10 -> max = 10a = -9 b = -3 -> max = -3')
    bot.send_message(message.chat.id, text = '2)Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.Пример: 2, 3, 7 -> 744 5 78 -> 7822 3 9 -> 22')
    bot.send_message(message.chat.id, text = '3)Задача 6: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).   Пример: 4 -> да-3 -> нет7 -> нет')
    bot.send_message(message.chat.id, text = "4)Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.   Пример: 5 -> 2, 48 -> 2, 4, 6, 8")
    bot.send_message(message.shat.id, text ='5)Задача 7 HARD по желанию - идет за 2 обязательных Напишите программу, которая принимает на вход целое число любой разрядности и на выходе показывает третью цифру слева этого числа или говорит, что такой цифры нет. Через строку решать нельзя.    Пример: 456111 -> 678 -> нет  9146548 -> 43 -> нет')
    log(message)
@bot.message_handler(func=lambda message: message.text== '2)Home_Work')
def Hw2(message):
    bot.send_message(message.chat.id,text= '1) Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа. Через строку решать нельзя.   Пример: 456 -> 5, 782 -> 8, 918 -> 1')
    bot.send_message(message.chat.id,text= "2) Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.Через строку решать нельзя.   Пример: 645 -> 5, 78 -> третьей цифры нет, 32679 -> 6")
    bot.send_message(message.chat.id,text= "3) Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.    Пример:6 -> да,7 -> да, 1 -> нет")
    bot.send_message(message.chat.id,text= "4) Задача необязательная 1: на входе целое или вещественное число, надо удалить вторую цифру слева этого числа. Пример: 145 -> 15, 1 -> нет, 567,123 -> 57,123")
    bot.send_message(message.chat.id,text= "5) Задача необязательная 2:В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: <n программистов>.Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание слова.Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом <программист>, для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.")
    log(message)
@bot.message_handler(func=lambda message: message.text== '3)Home_Work')
def Hw3(message):
    bot.send_message(message.chat.id,text="1) Задача 19: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом. Через строку решать нельзя. Пример: 14212 -> нет, 12821 -> да, 23432 -> да")
    bot.send_message(message.chat.id,text= "2) Задача 21: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве. Пример: A (3,6,8); B (2,1,-7), -> 15.84, A (7,-5, 0); B (1,-1,9) -> 11.53")
    bot.send_message(message.chat.id,text="3) Задача 23: Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N. Пример: 3 -> 1, 8, 275 -> 1, 8, 27, 64, 125")
    bot.send_message(message.chat.id,text="4) Задача 21 - HARD необязательная: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек")
    bot.send_message(message.chat.id,text="5) Задача 19 - HARD необязательная: Напишите программу, которая принимает на вход целое число любой разрядности и проверяет, является ли оно палиндромом. Через строку нельзя решать само собой.")
    log(message)
@bot.message_handler(func=lambda message: message.text== '4)Home_Work')
def Hw4(message):
    bot.send_message(message.chat.id,text="1) Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B. Пример: 3, 5 -> 243 (3⁵)")
    bot.send_message(message.chat.id,text="2) Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе. Пример: 452 -> 11, 82 -> 10, 9012 -> 12")
    bot.send_message(message.chat.id,text="3) Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран. Пример: 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19], 6, 1, 33 -> [6, 1, 33]")
    bot.send_message(message.chat.id,text="4) Задача 26 HARD Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.456 -> 3, 0 -> 1, 89,126 -> 5,0,001->4")
    log(message)
@bot.message_handler(func=lambda message: message.text== '5)Home_Work')
def Hw5(message):
    bot.send_message(message.chat.id,text= "1)Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.  Пример: [345, 897, 568, 234] -> 2")
    bot.send_message(message.chat.id,text= "2)Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных индексах.  Пример: [3, 7, 23, 12] -> 19,[-4, -6, 89, 6] -> 0")
    bot.send_message(message.chat.id,text= "3)Задача 38: Задайте массив вещественных случайных чисел. Найдите разницу между максимальным и минимальным элементов массива.")
    bot.send_message(message.chat.id,text= "4)Задача HARD STAT необязательная: Задайте массив случайных целых чисел. Найдите максимальный элемент и его индекс, минимальный элемент и его индекс, среднее арифметическое всех элементов. Сохранить эту инфу в отдельный массив и вывести на экран с пояснениями. Найти медианное значение первоначалального массива , возможно придется кое-что для этого дополнительно выполнить.")
    log(message)
@bot.message_handler(func=lambda message: message.text== '6)Home_Work')
def Hw6(message):
    bot.send_message(message.chat.id,text="1)Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь. Пример: 0, 7, 8, -2, -2 -> 2, 1, -7, 567, 89, 223-> 3")
    bot.send_message(message.chat.id,text="2)Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.   Пример: b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)")
    bot.send_message(message.chat.id,text="3)Задача НЕГАФИБОНАЧЧИ необязательная. Задайте число. Составьте массив чисел НегаФибоначчи, в том числе для отрицательных индексов. Пример: для k = 9 массив будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]")
    bot.send_message(message.chat.id,text="4)Задача VERY HARD необязательная Имеется массив случайных целых чисел. Создайте массив, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.Одно число - это не последовательность.    Пример:[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7,[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8,[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8")
    log(message)
@bot.message_handler(func=lambda message: message.text== '7)Home_Work')
def Hw7(message): 
    bot.send_message(message.chat.id,text="1)Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами. Пример: m = 3, n = 4. 0,5 7 -2 -0,     2, 1 -3,3 8 -9,9,       8 7,8 -7,1 9")
    bot.send_message(message.chat.id,text="2)Задача 50. Напишите программу, которая на вход принимает значение элемента в двумерном массиве, и возвращает позицию этого элемента или же указание, что такого элемента нет.Например, задан массив: 1 4 7 2, 5 9 2 3, 8 4 2 4, 17 -> такого числа в массиве нет")
    bot.send_message(message.chat.id,text="3)Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.Например, задан массив:1 4 7 2,  5 9 2 3,    8 4 2 4.    Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.")
    log(message)
@bot.message_handler(func=lambda message: message.text== '8)Home_Work')
def Hw8(message):    
    bot.send_message(message.chat.id,text="1)Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.Например, задан массив: 1 4 7 2     5 9 2 3      8 4 2 4     В итоге получается вот такой массив:7 4 2 1     9 5 3 2     8 4 4 2")
    bot.send_message(message.chat.id,text="2) Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.Например, задан массив: 1 4 7 2     5 9 2 3    8 4 2 4     5 2 6 7  Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка")
    bot.send_message(message.chat.id,text="3)Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.Например, даны 2 матрицы: 2 4 | 3 4     3 2 | 3 3   Результирующая матрица будет:18 20     15 18")
    bot.send_message(message.chat.id,text="4)Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.")
    bot.send_message(message.chat.id,text="5)Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.")
    log(message)
@bot.message_handler(func=lambda message: message.text== '9)Home_Work')
def Hw9(message):
    bot.send_message(message.chat.id,text="1)Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии")
    bot.send_message(message.chat.id,text="2)Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.")
    bot.send_message(message.chat.id,text="3)Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.")
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
    markup.add(btn1, btn2, btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id, text="Выбирай номер домашки", reply_markup=markup)
    log(message)
# добавляю функции, кнопки с номерами задач, в которых будет распечатываться задача

@bot.message_handler(func=lambda message: message.text == '1)Home_Works')
def HW_1(message):
    bot.send_message(message.chat.id, text="1) Найдите сумму цифр трехзначного числа n.  Пример: n = 123 -> res = 6 (1 + 2 + 3)n = 100 -> res = 1 (1 + 0 + 0)")
    bot.send_message(message.chat.id, text="2) Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей. Пример: n = 6 -> 1 4 1, n = 24 -> 4 16 4, n = 60 -> 10 40 10")  
    bot.send_message(message.chat.id, text="3)Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.")
    bot.send_message(message.chat.id, text="4)Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).Выведите yes или no соответственно. Пример: a, b, c = 3, 2, 4 -> yes a, b, c = 3, 2, 1 -> no ")
    log(message)
@bot.message_handler(func=lambda message: message.text == '2)Home_Works')
def HW_2(message):
    bot.send_message(message.chat.id,text="1)Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть")
    bot.send_message(message.chat.id, text="2)Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.")
    bot.send_message(message.chat.id, text="3)Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")
    log(message)
@bot.message_handler(func=lambda message: message.text == '3)Home_Works')
def HW_3(message):
    bot.send_message(message.chat.id,text="1)Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.Найдите количество и выведите его. Пример: list_1 = [1, 2, 3, 4, 5] k = 3 # 1" ) 
    bot.send_message(message.chat.id,text="2)Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его. Пример: list_1 = [1, 2, 3, 4, 5] k = 6, # 5")
    bot.send_message(message.chat.id, text="3)Сорян, глянь ее на платформе, я не смог ее сюда закинуть из-за объемности, но вот тебе ссылочка => <a href='https://autotest.gb.ru/problems/23?lesson_id=344340&_ga=2.230040479.242068001.1690283553-1519019485.1690283553'>Скрабл</a>", parse_mode='HTML')
    log(message)
@bot.message_handler(func=lambda message: message.text == '4)Home_Works')
def HW_4(message):
    bot.send_message(message.chat.id, text="Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.")
    bot.send_message(message.chat.id, text='Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.')
    log(message)
@bot.message_handler(func=lambda message: message.text == '5)Home_Works')
def HW_5(message):
    bot.send_message(message.chat.id, text="1)Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B спомощью рекурсии.")
    bot.send_message(message.chat.id, text="2)Задача 28: Напишите рекурсивную функцию sum(a, b),возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.Также нельзя использовать циклы.")
    log(message)
@bot.message_handler(func=lambda message:message.text=='6)Home_Works')
def HW_6(message):
    bot.send_message(message.chat.id,text="1)Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула дляполучения n-го члена прогрессии: a = a1 + (n-1) * d. Каждое число вводится с новой строки.")
    bot.send_message(message.chat.id,text="2)Задача 32: Определить индексы элементов массива (списка),значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума")
    log(message)






bot.polling()




