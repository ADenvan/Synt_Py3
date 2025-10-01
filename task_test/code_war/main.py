
# from codeWars.number_tasks import number_tasks
# from tasks.codeWars_tasks.number_tasks import number_tasks
# # ---------------------------------------
# # ---------------------------------------
# 52.
def first_non_consecutive(n: list):
    idx = n[0]
    for i in n:
        if idx != i:
            return i
        idx += 1


# # ---------------------------------------
# 51.
class Reverse_seq():
    def __init__(self, n):
        self._n = n
        self._ls = []

    def str_c(self):
        num = [i for i in range(self._n)]
        ret = len(num[::-1]) + 1
        return ret

    def ret_count_str(self):
        ap = []
        for _ in range(self._n):
            self._n -= 1
            ap.append(self.str_c())
        return ap

def reverse_seq(n: int):
    ret = Reverse_seq(n)
    log = ret.ret_count_str()

    return log

# # ---------------------------------------
# 50.
class Double_char():
    def __init__(self, list_str: list):
        self.list_str = list_str
    def get_indx_(self, str_: str):
        join_str = "".join(self.list_str)
        idx = join_str.index(str_)
        return idx

    def str_c(self, str_: str):
        ap = []
        ls = self.list_str
        for s in ls:
            idx = self.get_indx_(s)
            if s in str_:
                ap.append(ls[idx] + s)
        self.list_str = ap
        return self.list_str

    def ret_count_str(self, str_: str):
        res = "".join(self.str_c(str_))
        return res

def double_char(st: str):
    list_str = [i for i in st]
    ret = Double_char(list_str)
    res = ret.ret_count_str(st)
    return res

# # ---------------------------------------
# 49.
class Str_count():
    def __init__(self, str_, letter):
        self._str_ = str_
        self._letter = letter
        self._new_dict = {}

    def str_c(self):
        for item in self._str_:
            self._new_dict[item] = self._new_dict.get(item, 0) + 1
        return self._new_dict

    def ret_count_str(self):
        char = self._letter
        new_dict = self.str_c()

        return new_dict.get(char)

def str_count(st: str, char: str):
    ret = Str_count(st, char)
    log_result = ret.ret_count_str()
    if log_result is None:
        return 0
    else:
        return log_result

# # ---------------------------------------
# 48.
class sp_eng:
    def __init__(self,  value="english"):
        self.value = value

    def is_lower(self, value_str: str):
        return value_str.lower()

    def __equel__(self, st: str):
        if self.value in self.is_lower(st):
            return True
        else:
            return False


# # ---------------------------------------
# 47.
def summation(n):
    result = sum([int(i) for i in range(0, n+1)])
    return result

def summation(n):
    count = 0
    i = 0
    while i < n:
        i += 1
        count = count + i
    return count
# # ---------------------------------------
# 46.
def to_alternating_case(word):
    from re import search
    ls = []
    for elem in word:
        if search(r'[a-z]', elem):
            ls.append(elem.upper())
        elif search(r'[A-Z]', elem):
            ls.append(elem.lower())
        else:
            ls.append(elem)
    return "".join(ls)

def to_alternating_case(string):
    new_string = ''
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string
# # ---------------------------------------
# 45.
# def wrap(wrap):
#     dic = {}
#     dic["value"] = wrap
#     return dic

class wrap:
    def __init__(self,value,key="value"):
        self.__value = value
        self.__key = key
    def __getitem__(self,key):
        if self.__key == key:
            return self.__value
        raise KeyError("Your key", key,"is incorrect")

# # ---------------------------------------
# 44.
def is_uppercase(inp):
    ret = True if inp == inp.upper() else False
    return ret

def is_uppercase(inp):
    for letter in inp:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True

def is_uppercase(inp):
    from re import search
    if search(r'[a-z]', inp):
        return False
    return True
# # ---------------------------------------
# 43.
def grader(score):
    # if type(score) == int:
    #     return "A"
    if score >= 0.00 and score <= 0.59 or score > 1.00:
        return "F"
    elif score >= 0.60 and score <= 0.69:
        return "D"
    elif score >= 0.70 and score <= 0.79:
        return "C"
    elif score >= 0.80 and score <= 0.89:
        return "B"
    elif score >= 0.90 and score <= 0.99:
        return "A"
    else:
        return "A"
def grader(score):
    for limit, grade in [(0.9, "A"), (0.8, "B"), (0.7, "C"), (0.6, "D")]:
        if limit <= score <= 1:
            return grade
    return 'F'

# # ---------------------------------------
# 42.
fruit = {1:'kiwi',2:'pear',3:'kiwi',4:'banana',5:'melon',6:'banana',7:'melon',
         8:'pineapple',9:'apple',10:'pineapple',11:'cucumber',12:'pineapple',
         13:'cucumber',14:'orange',15:'grape',16:'orange',17:'grape',18:'apple',
         19:'grape',20:'cherry',21:'pear',22:'cherry',23:'pear',24:'kiwi',
         25:'banana',26:'kiwi',27:'apple',28:'melon',29:'banana',30:'melon',
         31:'pineapple',32:'melon',33:'pineapple',34:'cucumber',35:'orange',
         36:'apple',37:'orange',38:'grape',39:'orange',40:'grape',41:'cherry',
         42:'pear',43:'cherry',44:'pear',45:'apple',46:'pear',47:'kiwi',
         48:'banana',49:'kiwi',50:'banana',51:'melon',52:'pineapple',53:'melon',
         54:'apple',55:'cucumber',56:'pineapple',57:'cucumber',58:'orange',
         59:'cucumber',60:'orange',61:'grape',62:'cherry',63:'apple',
         64:'cherry',65:'pear',66:'cherry',67:'pear',68:'kiwi',69:'pear',
         70:'kiwi', 71:'banana',72:'apple',73:'banana',74:'melon',
         75:'pineapple',76:'melon',77:'pineapple',78:'cucumber',79:'pineapple',
         80:'cucumber',81:'apple',82:'grape',83:'orange',84:'grape',85:'cherry',
         86:'grape',87:'cherry',88:'pear',89:'cherry',90:'apple',91:'kiwi',
         92:'banana',93:'kiwi',94:'banana',95:'melon',96:'banana',97:'melon',
         98:'pineapple',99:'apple',100:'pineapple'}
def subtract_sum(n, fruit):
    ret = sum([int(i) for i in str(n)])
    num = n - ret

    if num < 100:
        for item in fruit:
            if item.get(num):
                return item.get(num)
        return num
    return subtract_sum(num)

def subtract_sum(n):
  n -= (sum([int(i) for i in str(n)]))
  while not n in fruit:
    n -= (sum([int(i) for i in str(n)]))
  return fruit[n]
def subtract_sum(number):
    while True:
        number -= sum(map(int, str(number)))
        if number <= 100:
            for e in fruit.split('\n'):
                if str(number) in e:
                    return e.split('-')[1]
# # ---------------------------------------
# 41.
def reverse_words(words: str):
    return " ".join(reversed(words.split(" ")))
def reverseWords(str: str):
    return " ".join(str.split(" ")[::-1])

# # ---------------------------------------
# 40.
def cookie(x):
    if type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    else:
        ryan = [{"Ryan": "Zach", 2.3: "Monica", 26: "Monica", True: "the dog"}]
        dc = "".join([i.get(x) for i in ryan])
        return f"Who ate the last cookie? It was {dc}!"

# == try except
def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who

# == format
CULPRITS = {
    str: 'Zach',
    int: 'Monica', float: 'Monica'
}
def cookie(x):
    return "Who ate the last cookie? It was {}!".format(CULPRITS.get(type(x), 'the dog'))


# # ---------------------------------------
# 39.
def merge_arrays(first, second):
    list_ = list(first + second)
    sort_result = sorted(set(list_))
    return sort_result

def merge_arrays(first, second):
    working = []
    for e in first:
        if e not in working:
            working.append(e)
    for i in second:
        if i not in working:
            working.append(i)
    return sorted(working)
# # ---------------------------------------
# 38.
def who_is_paying(name):
    if len(name) <= 2:
        a = [name]
        return a
    ch = name[0:2]

    arr = [name]
    arr.append(ch)
    return arr

def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0:2]]
    else:
        return [name[0:len(name)]]


# # ---------------------------------------
# 37.
def array_space(st: str):
    n = st.split(",")
    if len(n) < 3:
        return
    ap = []
    for i in n:
        ap.append(i)
    ret = " ".join(ap[1:-1])
    return ret

def array(string: str):
    split = string.split(",")
    remove = split[1:-1]
    return " ".join(remove) if remove else None

def array(s: str):
    r = ' '.join(s.split(',')[1:-1])
    return r if r else None

# # ---------------------------------------
# 36.
def no_space(x: str):
    return "".join(x.split())
    # return x.replace(" ", "")

# # ---------------------------------------
# 35.
def add_binary(a, b):
    return '{0:b}'.format(a+b)
    # return bin(a+b).replace("0b", "")




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
