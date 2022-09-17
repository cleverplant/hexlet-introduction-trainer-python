# Logical operators
# Логические операторы

'''
Мы уже умеем писать функции, которые проверяют одиночные условия. 
Теперь научимся строить составные условия.

Хороший пример: проверка пароля. 
Предположим, что некий сайт при регистрации требует, 
чтобы пароль был длиннее восьми символов и короче двадцати символов. 

В математике мы бы написали 8 < x < 20, но во многих языках программирования так сделать нельзя. 
К счастью, Python такие составные условия писать позволяет. 
И всё же на минутку мы забудем о такой возможности. 
Попробуем сделать два отдельных логических выражения и соединить их специальным оператором «И»:

Пароль длиннее 8 символов И пароль короче 20 символов.
Вот функция, которая принимает пароль и говорит, 
соответствует ли он условиям (True) или не соответствует (False):'''

def is_correct_password(password):
    length = len(password)
    return length > 8 and length < 20

print(is_correct_password('qwerty'))                   # => False
print(is_correct_password('qwerty1234'))               # => True
print(is_correct_password('zxcvbnmasdfghjkqwertyui'))  # => False

'''================================================================================================
and — означает «И» - УМНОЖЕНИЕ (в математической логике это называют конъюнкцией).
Всё выражение считается истинным, только если истинен каждый операнд — каждое из составных выражений. 
Иными словами, and означает «и то, и другое». 

Приоритет этого оператора ниже, чем приоритет операторов сравнения, 
поэтому выражение length > 8 and length < 20 отрабатывает правильно без скобок.
====================================================================================================

Кроме and часто используется оператор or — «ИЛИ» СЛОЖЕНИЕ (дизъюнкция). 
Он означает «или то, или другое, или оба». То есть выражение a or b считается истинным, 
если хотя бы один из операндов (a или b или одновременно все операнды) является истинным. 
Иначе выражение ложное.

Операторы можно комбинировать в любом количестве и любой последовательности, 
но когда одновременно встречаются and и or, то приоритет лучше задавать скобками. 
Ниже пример расширенной функции определения корректности пароля:
===================================================================================================='''

def has_special_chars(str):
    # проверяет содержание специальных символов в строке
    return

def is_strong_password(password):
    length = len(password)
    # Скобки задают приоритет. Понятно что к чему относится.
    return (length > 8 and length < 20) and has_special_chars(password)

'''=================================================================================================
Другой пример. 
Мы хотим купить квартиру, которая удовлетворяет условиям: площадь от 100 кв. метров 
и больше на любой улице ИЛИ площадь от 80 кв. метров и больше, но на центральной улице Main Street. 
Напишем функцию, проверяющую квартиру. Она принимает два аргумента: 
площадь (число) и название улицы (строку):'''

def is_good_apartment(area, street):
  return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street'))  # => True
print(is_good_apartment(120, 'Main Street'))    # => True
print(is_good_apartment(80, 'Main Street'))     # => True

''' ======================================================================================
Область математики, в которой изучаются логические операторы, называется булевой алгеброй. 
Ниже показаны «таблицы истинности» — по ним можно определить, 
каким будет результат применения оператора:
==========================================================================================

И and

A	    B	    A and B
True	True	True
True	False	False
False	True	False
False	False	False  
==========================================================================================

ИЛИ or

A	    B	    A or B
True	True	True
True	False	True
False	True	True
False	False	False
==========================================================================================
Отрицание

Наряду с логическими операторами И и ИЛИ, часто используется операция «отрицание». 
Отрицание меняет логическое значение на противоположное. 
В программировании ему соответствует унарный оператор not.'''

not True   # False
not False  # True

'''
Например, если есть функция, проверяющая чётность числа, 
то с помощью отрицания можно выполнить проверку нечётности:'''

def is_even(number):
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False

'''
То есть мы просто добавили not слева от вызова функции и получили обратное действие.
Отрицание — мощный инструмент, который позволяет лаконично выражать задуманные правила в коде 
без необходимости писать новые функции.

А что если написать так not not is_even(10)? Удивительно, но код сработает:'''

print(not not is_even(10))  # => True

'''В логике двойное отрицание подобно отсутствию отрицания вообще:'''

not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False




