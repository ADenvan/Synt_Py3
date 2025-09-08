import time
from typing import Tuple
# -------------------------------------
# -------------------------------------
# -------------------------------------
# -------------------------------------







# -------------------------------------
# 10.
def timing_decorator(func):
    """Декоратор для измерения времени выполнения функции"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция выполнилась за {end - start:.4f} секунд(ы)")
        return result
    return wrapper
# -------------------------------------
# 9.
def common_elements(list_1: list, list_2: list):
    return set(list_1) & set(list_2)

# -------------------------------------
# 8.
class BankAccount:
    """Простейший класс банковского счёта"""
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Нельзя внести отрицательную сумму")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Нельзя снять отрицательную сумму")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance


# -------------------------------------
# 7.
def count_lines_and_words(filename: str):
    """Возвращает (кол-во строк, кол-во слов) в файле"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words

# -------------------------------------
# 6.
def factorial(n):
    if n < 0:
        raise ValueError("Negstiv value")
    if n in (0,1):
        return 1
    return n * factorial(n - 1)

# -------------------------------------
# 5.
def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

# -------------------------------------
# 4.
def sieve_of_eratosthenes(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return primes

# -------------------------------------
# 3.
def char_frequency(str_: str) -> dict[str, str]:
    result = {}
    for char in str_:
        result[char] = result.get(char, 0) + 1
    return result

# -------------------------------------
# 2.
def custom_sort(nums: list) -> list[int]:
    if len(nums) <= 0:
        return nums
    elem = nums[0]
    left = list(filter(lambda x: x < elem, nums))
    center = [i for i in nums if i == elem]
    right = list(filter(lambda x: x > elem, nums))
    return custom_sort(left) + center + custom_sort(right)
# -------------------------------------
# 1. 
def is_palindrome(st:str) -> bool:
    repl = st.lower().replace(" ", "")
    result = True if repl[::-1] == repl else False
    return result
        
    