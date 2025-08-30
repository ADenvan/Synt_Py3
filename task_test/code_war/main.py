# from codeWars.number_tasks import number_tasks
# from tasks.codeWars_tasks.number_tasks import number_tasks
# # ---------------------------------------
# # ---------------------------------------
# # ---------------------------------------
# # ---------------------------------------
# # ---------------------------------------


# # ---------------------------------------
# 35.





# # ---------------------------------------
# 34. Removing elemen
my_lisst = ["Keep", "Remove", "Keep", "Remove", "Keep"]
my_num_list = [1, 2, 3, 4, 5]
my_set = [{'Great': 'Job', 'Great': 'Job'}]

def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    # return [v for c, v in enumerate(my_list) if not c%2]



# # ---------------------------------------
# 33. count_by_x
# Создайте функцию с двумя аргументами, которая будет возвращать массив первых n кратных x. Предположим, что и данное число, и количество раз, которое нужно посчитать, будут положительными числами, большими 0.
x, n = 1, 10
x, n = 2, 5
# def count_by(x, n):
#     if x <=1:
#         return [i for i in range(x, n)]
#     else:
#         ret = [i * a for i in range(n + 1)]
#         return ret[1:]
#     # num = [i * x for i in range(1, n+1)]



# # ---------------------------------------
# 32. Counting sheep...
# Рассмотрим массив/список овец, где некоторые овцы могут отсутствовать на своем месте. Нам нужна функция, которая подсчитывает количество овец, присутствующих в массиве (true означает наличие).
#
# Правильный ответ будет 17.
def count_sheeps(sheep):
    a_count = 0
    for i in sheep:
        if i == True:
            a_count += 1
    return a_count
    # return sheep.count(True)
    # return len([x for x in sheep if x])

# # ---------------------------------------
# 31. Super Duper Easy
# Создайте функцию, которая возвращает значение, умноженное на 50 и увеличенное на 6. Если введенное значение является строкой, оно должно возвращать «Ошибка».

def problem(a):
    return "Error" if type(a) == str else a * 50 + 6

    # return "Error" if isinstance(a, str) else a * 50 + 6

    # try:
    #     return a * 50 + 6
    # except TypeError:
    #     return "Error"

# # ---------------------------------------
# 30. Beginner - Reduce but Grow
# Учитывая непустой массив целых чисел, вернуть результат умножения значений вместе по порядку. Пример:import math
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

from functools import reduce
from operator import mul
def grow(arr):
    a, b = 1, 0
    while b < len(arr):
        b += 1
        a *= arr[-b]
    return a
    # return reduce(lambda a, y: a * y, arr)
    # return math.prod(arr)
    # return reduce(mul, arr)

# # ---------------------------------------
# 29. Volume of a Cuboid.
# Бобу нужен быстрый способ вычисления объема прямоугольного параллелепипеда с тремя значениями: длина, ширина и высота прямоугольного параллелепипеда. Напишите функцию, которая поможет Бобу в этом вычислении.
def get_volume_of_cuboid(length, width, height):
    return round(length * height * width)


# # ---------------------------------------
# 28. Powers of 2
# Завершите функцию, которая принимает неотрицательное целое число n в качестве входных данных и возвращает список всех степеней числа 2 с показателем степени от 0 до n (включительно).

def powers_of_two(n):
    return [2 ** i for i in range(n+1)]

# # ---------------------------------------
# 27. Beginner Series #2 Clock.
#Часы показывают ч часов, m минут и s секунд после полуночи.
# Ваша задача — написать функцию, которая возвращает время с полуночи в миллисекундах.
def past(h, m, s):
    if 0 <= h <= 23 or 0 <= m <= 59 or 0 <= s <= 59:
        x = h * 3600000
        y = m * 60000
        z = s * 1000
        total = x + y + z
        return(total)
    else:
        return("Please input an hour between 0 and 23 and a minute or second inbetween 0 and 59.")

# # ---------------------------------------
# 26. Reversed Strings.
# Завершите решение так, чтобы оно перевернуло переданную в него строку.

def solution(string):
    st = ""
    tes = [y for y in string[::-1]]
    for x in tes:
        st += x
    return string[::-1]

# def solution(string):
#     temp = list(string)
#     temp.reverse()
#     return ''.join(temp)

# def solution(string):
#     s = list(string)
#     j = len(s)-1
#     for i in range(len(s)):
#         if (i<j):
#             s[i], s[j] = s[j], s[i]
#             j = j-1
#         else:
#             continue
#     s1 = ''.join(s)
#     return s1

# def solution(string):
#     return ''.join(i for i in reversed(string))

# # ---------------------------------------
# 25. Century From Year
# Первое столетие охватывает период с 1 года по 100 год включительно, второе столетие — с 101 года по 200 год включительно и т. д.
def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1

# # ---------------------------------------
# 24. String repeat
# Напишите функцию, которая принимает целое число n и строку s в качестве параметров и возвращает строку s, повторяющуюся ровно n раз.
# объект 'int' не является итерируемым
# "I"     -> "IIIIII"
# "Hello" -> "HelloHelloHelloHelloHello"
def repeat_str(repeat, st):
    # di = dict.fromkeys(str(repeat), st)
    # s = ""
    # for key, val in di.items():
    #     print(f"Key->{key}", f"Val->{val}")
    #     for x in range(int(key)):
    #         s += val
    #         print(f"X->{x} ", sep="", end="")
    # di.update(dict.fromkeys(str(repeat), s))
    # a = "".join(di.values())
    # print(f"di->{di}| a->{a} ")
    res = ""
    for i in range(int(repeat)):
        res += str(st)
    return res

# # ---------------------------------------
# 23. Quadratic Coefficients Solver.
# В этом Ката вы должны найти коэффициенты квадратного уравнения данных двух корней (x1 и x2).
# Уравнение будет иметь вид ax^2 + bx + c = 0

def quadratic(x1, x2):
    """Return the coefficients
    for a quadratic equation"""
    p = - (x1 + x2)
    q = x1 * x2
    return (1, p, q)

# # ---------------------------------------
# 22. Is the string uppercase?
# Create a method to see whether the string is ALL CAPS.
def is_uppercase(inp):
    N1, N2 = [], []
    for i in str(inp):
        N1.append(ord(i))
        for x in i:
            N2.append(ord(x.upper()))
    print(len(N1), " - ", len(N2))
    print(sum(N1), " - ", sum(N2))

    order = [ord(i) for i in inp]
    orderUpp = [ord(i) for i in str(inp).upper()]
    return order == orderUpp

# # ---------------------------------------
# 21. Abbreviate a Two Word Name.
# Напишите функцию для преобразования имени в инициалы. Это ката строго состоит из двух слов с одним пробелом между ними.
# На выходе должны быть две заглавные буквы с точкой, разделяющей их.
# Патрик Фини => P.F.

def abbrev_name(name):
    arr = str(name).upper().split(" ")
    return str(arr[0][0]) + "." + str(arr[1][0])

    # return '.'.join(w[0] for w in name.split()).upper()
    # return '.'.join(filter(str.isupper,name.title()))

# # ---------------------------------------
# 20. Opposites Attract.
# Напишите функцию, которая будет принимать количество лепестков каждого цветка и возвращать true, если они влюблены, и false, если нет.
def lovefunc(flower1, flower2):
    return True if (flower1 + flower2) % 2 != 0 else False

# # ---------------------------------------
# 19. Is it a palindrome?
# Палиндром — это слово, число, фраза или другая последовательность символов, которая читается так же, как и вперед, и назад, например, мадам или гоночная машина, дата и время 21/12/33 12:21
def is_palindrome(s):
    A = [i for i in str(s).lower()]
    return True if A[:] == A[::-1] else False

# # ---------------------------------------
# 18. Sum of positive
# Вы получаете массив чисел, возвращаете сумму всех положительных.
# Пример [1,-4,7,12] => 1 + 7 + 12 = 20
def positive_sum(arr):
    total = sum(int(i) for i in arr if i > 0)
    return total

    # return sum(map(lambda x: x if x > 0 else 0, arr))
    # return sum(filter(lambda x: x > 0, arr))

# # ---------------------------------------
# 17. Convert number to reversed array of digits
# Учитывая случайное неотрицательное число, вы должны вернуть цифры этого числа в массиве в обратном порядке.
def digitize(n):
    L = ([])
    for i in str(n):
        L.append(int(i))
    return L[::-1]

    # return list(map(int, str(n)[::-1]))
    # return [int(i) for i in str(n)[::-1]]

    # output = list("k" * len(str(n)))
    # output_info = []
    # info = []
    #
    # def indextualize(lst, num):
    #     index = []
    #     for c in range(len(lst)):
    #         if lst[c] == num:
    #             index.append(c)
    #     return index
    #
    # for x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    #     info.append(indextualize(list(str(n)), x))
    #
    # for num in info:
    #     sub_lst = []
    #     for i in num:
    #         sub_lst.append(len(str(n)) - i - 1)
    #     output_info.append(sub_lst)
    #
    # for num in output_info:
    #     for indexx in num:
    #         output[indexx] = output_info.index(num)
    #
    # return [int(y) for y in list("".join([str(x) for x in output]))]
# # ---------------------------------------
# 16.
# Очень просто, по заданному целому числу или числу с плавающей запятой найти его противоположность.

def opposite(number):
    return (-abs(number) if number > 0 else abs(number))
    # opposite = lambda x: -x
# # ---------------------------------------
# 15. Grasshopper - Check for factor
# Возвратите true, если это фактор или false, если это не так.
# Факторы — это числа, которые вы можете перемножить, чтобы получить другое число.
# 2 и 3 являются делителями 6, потому что: 2 * 3 = 6

def check_for_factor(base, factor):
    return (True if base % factor == 0 else False)

# # ---------------------------------------
# 14. Returning Strings
# Создайте функцию, которая будет возвращать оператор приветствия, использующий ввод; ваша программа должна вернуть "Привет, <имя>, как дела сегодня?".
def greet(name):
    set_name = [name]
    name_list = dict.fromkeys(set_name, f"Hello, {name} how are you doing today?")
    return name_list.get(name)
# # ---------------------------------------
# 13 Wilson primes.
# Ваша задача — создать функцию, возвращающую истину, если заданное число является простым числом Вильсона.

from math import factorial
def am_i_wilson(n: int):
    """ Check if given number is a wilson prime. """
    if 563 >= n > 1:
        return not (factorial(n - 1) + 1) % pow(n, 2)
    return False
    # return n in (5, 13, 563)

# # ---------------------------------------
# 12. DNA to RNA Conversion.
# "GCAT" => "GCAU"
# Входная строка может быть произвольной длины, в частности, она может быть пустой. Все входные данные гарантированно верны, т. е. каждая входная строка будет состоять только из букв «G», «C», «A» и/или «T».
def dna_to_rna(dna):
     T = ""
     for i in dna:
         if i == "T":
             T = T + "U"
         else:
             T = T + i
     return T
    # return str(dna).replace("T", "U")

# # ---------------------------------------
# 11. Expressions Matter.
# Даны три целых числа a ,b ,c, вернуть наибольшее число, полученное после вставки следующих операторов и скобок: +, *, ()
# Другими словами, попробуйте каждую комбинацию a,b,c с [*+()] и верните максимальное полученное значение (подробнее об этом читайте в примечаниях)
# 1 * (2 + 3) = 5
# 1 * 2 * 3 = 6
# 1 + 2 * 3 = 7
# (1 + 2) * 3 = 9

def expression_matter(a, b ,c):
    return max(a+b+c, a*b*c, (a+b)*c, a*(b+c))
    # if a == 1: b += 1
    # if c == 1: b += 1
    # if b == 1:
    #     if a < c: a += 1
    #     else: c += 1
    # return a * b * c
# # ---------------------------------------
# 10. Twice as old.
# Подсчитайте, сколько лет назад отец был вдвое старше сына (или через сколько лет он будет вдвое старше).
# Ответ всегда больше или равен 0, независимо от того, был он в прошлом или в будущем.
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)
# # ---------------------------------------
# 9. Return Negative.
# В этом простом задании вам дается число, и вы должны сделать его отрицательным.
# Число может быть уже отрицательным, и в этом случае никаких изменений не требуется.
def make_negative(number):
    return -abs(number)

# # ---------------------------------------
# 8. Find Multiples of a Number
# Если предел кратен целому числу, он также должен быть включен. В функцию всегда будут передаваться только положительные целые числа, не состоящие из 0. Предел всегда будет выше основания.
# Например, если переданы параметры (2, 6), функция должна вернуть [2, 4, 6], так как 2, 4 и 6 кратны от 2 до 6.
def find_multiples(integer, limit):
    arr = []
    count = integer
    while count <= limit:
        arr.append(count)
        count += integer
    return arr

# def find_multiples(integer, limit):
#     return [i for i in range(integer, limit + 1, integer)]

# # ---------------------------------------
# 7. Take the Derivative
# Ваша функция должна умножать два числа, а затем вычитать 1 из показателя степени. Затем он должен вернуть выражение (например, 28x^7). «^1» не следует усекать, если показатель степени = 2.
def derive(coefficient, exponent):
    sum = 0
    if exponent != 2:
        sum = coefficient * exponent
    return f"{sum}x^{exponent-1}"
    # return ("{}x^{}".format(coefficient * exponent, exponent - 1))
# # ---------------------------------------
# 6. Is he gonna survive?
# true, если да, иначе false :)
def hero(bullets, dragons):
    pass
# # ---------------------------------------
# 5. Thinkful - Logic Drills: Traffic light
# Вам нужна функция для обработки каждого перехода от зеленого к желтому, к красному, а затем снова к зеленому.
# зеленый, выход должен быть желтым.
def update_light(current):
    GYR = ['green', 'yellow', 'red']
    if current == 'green':
        return GYR[1]
    if current == 'yellow':
        return GYR[2]
    if current == 'red':
        return GYR[0]
# def update_light(current):
#     return {"green": "yellow", "yellow": "red", "red": "green"}[current]
# # ---------------------------------------
# 4. Keep Hydrated!
# Поскольку Натан знает, как важно избегать обезвоживания, он выпивает 0,5 литра воды за час езды на велосипеде.
# time = 3 ----> litres = 1
def litres(time):
    return  int(time * 0.5)
# # ---------------------------------------
# 3. Total amount of points
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# Нам нужно написать функцию, которая берет эту коллекцию и возвращает количество очков, набранных нашей командой (x) в чемпионате по приведенным выше правилам.
def points(games):
    score = 0
    for i in games:
        x, y = i.split(':')
        if x > y:
            score += 3
        if x == y:
            score += 1
    return score
# def points(a):
#     return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
# def points(games):
#     result = 0
#     for item in games:
# 	    result += 3 if item[0] > item[2] else 0
# 	    result += 1 if item[0] == item[2] else 0
#     return result

# 2. Did she say hallo?
# Напишите простую функцию, проверяющую, содержит ли строка слово «привет» на разных языках.

def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False
# def validate_hello(greetings):
#     return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])

# from re import compile, search, I
# REGEX = compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', I)
# def validate_hello(greeting):
#     return bool(search(REGEX, greeting))

# 1. Name Shuffler
# Напишите функцию, которая возвращает строку, в которой имя заменено на фамилию.
def name_shuffler(str_):
    AA = str_.split(' ')
    BB = AA[1] + ' ' + AA[0]
    return BB
# def name_shuffler(str_):
#     return ' '.join(str_.split(' ')[::-1])
# def name_shuffler(str_):
#     [first, last] = str_.split()
#     return last + " " + first
# def name_shuffler(s):
#     return ' '.join(reversed(s.split()))

# Is your period late?      --
# 5 without numbers !!      --
# Take the Derivative       ++
# Is he gonna survive?      --
# Thinkful - Logic Drills: Traffic light ++
# Keep Hydrated!            ++
