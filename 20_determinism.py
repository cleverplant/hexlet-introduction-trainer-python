# determinism
# детерминированность

'''Независимо от того, какой язык программирования используется, 
функции внутри него обладают некоторыми фундаментальными свойствами. 
Зная эти свойства, легче прогнозировать поведение функций, 
способы их тестирования и место их использования. 
К таким свойствам относится детерминированность. 
Функция называется детерминированной тогда, когда для одних и тех же входных параметров 
она возвращает один и тот же результат. 
Например, функция, считающая количество символов, детерминированная:'''

print(len('hexlet'))  # 6
print(len('hexlet'))  # 6

print(len('wow'))  # 6
print(len('wow'))  # 6

'''
Сколько бы раз мы не вызывали эту функцию, передавая туда значение 'hexlet', 
она всегда вернет 6. В свою очередь функция, возвращающая случайное число, 
не является детерминированной, так как у одного и того же входа 
(даже если он пустой, то есть параметры не принимаются) 
мы получим всегда разный результат. Насколько он разный - не важно, 
даже если хотя бы один из миллиона вызовов вернет что-то другое, 
эта функция автоматически считается недетерминированной.'''

# Синтаксис импортов будет изучаться позже на Хекслете
# from random import random

# Функция, возвращающая случайное число
from random import random
print(random() * 10)

print(random())  # 0.09856613113197676 => каждый раз вывщдятся разные значения
print(random())  # 0.8839904367241888

'''Зачем это нужно знать? 
Детерминированность серьезно влияет на многие аспекты. 
Детерминированные функции удобны в работе, их легко оптимизировать,легко тестировать. 
Если есть возможность сделать функцию детерминированной, то лучше ее такой и сделать'''

'''================================================================================='''
# Побочные эффекты

'''Вы, скорее всего, уже заметили (может, подсознательно), что print() - это тоже функция. Она принимает на вход данные любого типа и выводит их на экран.

Внимание, вопрос: что возвращает функция print()? 
Ответ: что бы она ни возвращала, это значение никак не используется.

print() выводит что-то на экран, но это не возврат значения, это просто какое-то действие,
которое выполняет функция.

Вывод на экран и возврат значения из функции — разные и независимые операции. 
Технически вывод на экран равносилен записи в файл (немного особый, но все-таки файл). 
Для понимания этой темы необходимо немного разобраться в устройстве операционных систем, 
что крайне важно для программистов.

С точки зрения программы вывод на экран — это так называемый побочный эффект. 
Побочным эффектом называют действия, которые изменяют внешнее окружение (среду выполнения). К таким действиям относятся любые сетевые взаимодействия, взаимодействие с файловой системой (чтение и запись файлов), вывод информации на экран или печать на принтере и так далее.

Побочные эффекты — один из основных источников проблем и ошибок в программных системах. 
Код с побочными эффектами сложен в тестировании, ненадежен. 
При этом без побочных эффектов программирование не имеет смысла. 
Без них было бы невозможно получить результат работы программы 
(записать в базу, вывести на экран, отправить по сети и так далее).

Понимание принципов работы с побочными эффектами очень сильно влияет на 
стиль программирования и способность строить качественные программы. 
Эта тема полностью раскроется в следующих курсах на Хекслете.

Вопрос для самопроверки. 
Можно ли определить наличие побочных эффектов внутри функции, 
опираясь только на её возврат?
'''





