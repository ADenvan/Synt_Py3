# test_task_functions.py
import unittest
import tempfile
import os
from task_test.AI.fund.main_fund import (
    is_palindrome,
    custom_sort,
    char_frequency,
    sieve_of_eratosthenes,
    fibonacci,
    factorial,
    count_lines_and_words,
    BankAccount,
    common_elements,
    timing_decorator,
)





# 10.
class Test_10_timing_decorator(unittest.TestCase):
    def test_timing_decorator(self):
        @timing_decorator
        def dummy_function(n):
            s = 0
            for i in range(n):
                s += i
            return s

        result = dummy_function(1000)
        self.assertEqual(result, sum(range(1000)))  # Проверяем корректность результата

# 9.
class Test_9_common_elements(unittest.TestCase):
    def test_common_elements(self):
        list1 = [1, 2, 3, 4]
        list2 = [3, 4, 5, 6]
        self.assertEqual(common_elements(list1, list2), {3, 4})
        self.assertEqual(common_elements([], [1, 2]), set())
        self.assertEqual(common_elements([1, 2], [3, 4]), set())

# 8.
class Test_8_BankAccount(unittest.TestCase):
    def test_bank_account(self):
        acc = BankAccount(100)
        acc.deposit(20)
        self.assertEqual(acc.get_balance(), 120)
        acc.withdraw(50)
        self.assertEqual(acc.get_balance(), 70)
        with self.assertRaises(ValueError):
            acc.withdraw(1000)
        with self.assertRaises(ValueError):
            acc.deposit(-10)

# 7.
class Test_7_count_lines_and_words(unittest.TestCase):
    def test_count_lines_and_words(self):
        content = "Hello world\nPython is great\n"
        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_name = tmp.name
        try:
            self.assertEqual(count_lines_and_words(tmp_name), (2, 5))
        finally:
            os.remove(tmp_name)

# 6.
class Test_6_factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-3)


# 5.
class Test_5_fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(0), [])


# 4.
class Test_4_sieve_Of_Aratosthenes(unittest.TestCase):
    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(sieve_of_eratosthenes(2), [2])
        self.assertEqual(sieve_of_eratosthenes(1), [])


# 3.
class Test_3_char_Frequency(unittest.TestCase):
    def test_char_frequency(self):
        self.assertEqual(char_frequency("hello"), {"h": 1, "e": 1, "l": 2, "o": 1})
        self.assertEqual(char_frequency("aaa"), {"a": 3})
        self.assertEqual(char_frequency(""), {})


# 2.
class Test_2_customSort(unittest.TestCase):
    def test_custom_sort(self):
        self.assertEqual(custom_sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])
        self.assertEqual(custom_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(custom_sort([]), [])


# 1.
class Test_1_is_palindrome(unittest.TestCase):
    def test_is_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("hello"))


# class TestTaskFunctions(unittest.TestCase):


if __name__ == "__main__":
    unittest.main()
