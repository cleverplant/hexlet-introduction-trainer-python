# Function Parameters
# Параметры функций
'''
Функции могут не только возвращать значения, но и принимать их в виде параметров. 
С параметрами функций мы уже сталкивались много раз:'''

# Принимает на вход один параметр любого типа
from unicodedata import name


print('я параметр')
# Принимает на вход два строковых параметра
# первый – что ищем, второй – на что меняем
print('google'.replace('go', 'mo'))  # moogle
# Принимает на вход два числовых параметра
# первый – округляемое число, второй – число знаков после запятой, которые нужно оставить
print(round(10.23456, 3))  # 10.235

'''
В этом уроке мы научимся создавать функции, которые принимают на вход параметры. 
Представим, что перед нами стоит задача – реализовать функцию get_last_char(), 
возвращающую последний символ в строке, переданной ему на вход как параметр. 
Вот как будет выглядеть использование этой функции:'''
# ============================================================================
def get_last_char(text):
    return text[-1]
# Передача параметров напрямую без переменных
print(get_last_char("Hexlet"))  # t
# Передача параметров через переменные
name1 = 'Hexlet'  
print(get_last_char(name1))  # t
name2 = 'Goo'
print(get_last_char(name2))  # o
# ============================================================================
'''
Из описания и примеров кода мы можем сделать следующие выводы:

- Нам нужно определить функцию get_last_char()
- Функция должна принимать на вход один параметр строкового типа
- Функция должна возвращать значение строкового типа
Определение функции:'''

def get_last_char(text):
    return text[-1]
'''
Разберем его. В скобках указывается имя переменной text, которая служит нам параметром. 
Имя параметра может быть любым, главное, чтобы оно отражало смысл того значения, 
которое содержится внутри. Мы могли бы определить функцию и так:'''

def get_last_char(string):
  return string[-1]
'''
Конкретное значение параметра будет зависеть от вызова этой функции.'''  
# Внутри функции string будет равна 'hexlet'
print(get_last_char('hexlet'))  # t

# Внутри функции string будет равна 'code'
print(get_last_char('code'))  # e

# Внутри функции string будет равна 'Winter is coming'
# имя переменной снаружи не связанно с именем переменной в определении функции
text = 'Winter is coming'
print(get_last_char(text))  # g

# Внутри функции string будет равна 'hexlet'
print(get_last_char('hexlet'))  # t

# Внутри функции string будет равна 'code'
print(get_last_char('code'))  # e

# Внутри функции string будет равна 'Winter is coming'
# имя переменной снаружи не связанно с именем переменной в определении функции
text = 'Winter is coming'
print(get_last_char(text))  # g
'''
Этот параметр является обязательным. Если попробовать вызвать функцию без параметра, 
то интерпретатор выдаст ошибку:'''
# get_last_char()  # такой код не имеет смысла
# TypeError: get_last_char() missing 1 required positional argument: 'string'
'''
Многие функции работают одновременно с несколькими параметрами, например, 
для округления числа нужно указать не только само число, 
но и количество знаков после запятой:'''

print(round(10.23456, 3))  # 10.235
'''
Тоже самое относится и к методам. Они могут требовать на вход любое количество параметров, 
которое им нужно для работы:'''
# первый параметр – что ищем
# второй параметр – на что меняем
print('google'.replace('go', 'mo'))  # moogle
'''
Для создания таких функций и методов, 
нужно в определении указать нужное количество параметров через запятую, 
дав им понятные имена. Ниже пример определения функции replace(), 
которая заменяет в слове одну часть строки на другую:'''

# replace(text, fro, to):
   # здесь тело функции, но мы его
   # опускаем, чтобы не отвлекаться
   
# def replace('google', 'go', 'mo')  # moogle  

'''
Когда параметров два и более, то практически для всех функций 
становится важен порядок передачи этих параметров. Если его поменять, 
то функция отработает по-другому: '''

# ничего не заменилось,
# так как внутри google нет mo
# def replace('google', 'mo', 'go') # google
# 
# 
'''Решение учителя:'''
def truncate(text, length):
    # BEGIN
    result = f"{text[0:length]}..."
    return result
    # END

