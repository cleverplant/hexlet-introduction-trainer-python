#  Сложение с помощью оператора +
print( 1 + 3) # 4
# Подсчет длины с помощью функции len()
name = 'Hexlet'
print(len(name))  # 6
# В такой схеме у нас есть четкое разделение: данные отдельно, функции отдельно.
'''
В Python наравне с таким разделением, используется и другой подход 
- объектно-ориентированный (ОО).'''

# Объектно-ориентированный код 
# строится на объединении данных и функций в одну сущность, называемую объектом. 
# Данные в таком случае называются атрибутами, а функции - методами.

# данные => атрибуты
name = 'Hexlet'
# функция => метод upper()
upper_name = name.upper()
print(upper_name)  # => 'HEXLET'

# данные + функции = объект => 
# атрибуты + методы = объектно ориентированный код

# строки => объект
# вызов функции - это вызов метода 
# вызов метода происходит через точку. 
# в остальном методы работают как обычные функции. 

# список методов в документации 
# в Python почти все является объектом: числа, строки и др. типы данных 

# странное имя метода с двумя подчеркиваниями в начале и в конце? 
# это методы, которые не предназначены для прямого вызова.  
# Для них созданы функции, которые внутри себя уже сами делают вызовы методов:
x = -5
print(abs(x))     # вызывает x.__abs__()
# -5 в 3 степени
print(pow(x, 3))  # вызывает x.__pow__(3)

'''==============================================================================='''
# Что будет выведено на экран?

company = "hexlet"
print(company.capitalize())  # ? => Hexlet

'''Hexlet'''
# HEXLET
# У строки нет такого метода
# hexlet
# =================================================================================
# Какое значение содержится в переменной company?

company = "Hexlet"
print(company.lower().upper())

# HEXLET
# hexlet
'''Hexlet'''
# Код завершится с ошибкой
# =================================================================================
# Выберите верные утверждения
# (нужно выбрать все корректные ответы)

# У объектов нет статических свойств, есть только методы
# Методы в Python – это обычные функции
''' Метод – это функции, находящиеся внутри атрибутов объекта '''
''' Метод применяется к данным, на которых он вызван '''

'''============================================================================='''
# src/solution.py
'''
Данные, вводимые пользователями, часто содержат лишние пробельные символы 
в конце или начале строки. Обычно их вырезают с помощью метода .strip(), 
например, было: ' hello\n ', стало: 'hello'.
Обновите переменную first_name, записав в неё то же самое значение, 
но обработанное методом .strip(). Распечатайте то, что получилось, на экран.'''

my_st = "Пример строки Python"
print(my_st.split())
'''=================================================================='''
first_name = '  Grigor   \n '
# BEGIN (write your solution here)
print(first_name.split())
print(first_name)
# END
'''=================================================================='''
# решение учителя
# BEGIN (write your solution here)
first_name = first_name.strip()
print(first_name)
# END


