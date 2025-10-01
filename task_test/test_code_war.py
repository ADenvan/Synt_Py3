import unittest
from task_test.code_war.main import name_shuffler, validate_hello, points, add_binary, no_space, array_space, who_is_paying, merge_arrays,cookie, grader, subtract_sum, reverse_words, is_uppercase, wrap, to_alternating_case, summation, sp_eng, str_count, double_char, reverse_seq, first_non_consecutive
# from main import name_shuffler
from random import randint

# ---------------------------------------
# ---------------------------------------
# ---------------------------------------
# 53.
class Test_53_(unittest.TestCase):
    pass
# ---------------------------------------
# 52.
class Test_52_(unittest.TestCase):
    def test_first_non_consecutive(self):
        self.assertEqual(first_non_consecutive([1,2,3,4,6,7,8]), 6)
        self.assertEqual(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
        self.assertEqual(first_non_consecutive([4,6,7,8,9,11]), 6)
        self.assertEqual(first_non_consecutive([4,5,6,7,8,9,11]), 11)
        self.assertEqual(first_non_consecutive([31,32]), None)
        self.assertEqual(first_non_consecutive([-3,-2,0,1]), 0)
        self.assertEqual(first_non_consecutive([-5,-4,-3,-1]), -1)
# ---------------------------------------
# 51.
class Test_51_(unittest.TestCase):
    def test_reverse_seq(self):
        self.assertEqual(reverse_seq(5),[5,4,3,2,1])
# ---------------------------------------
# 50.
class Test_50_(unittest.TestCase):
    def test_double_char(self):
        self.assertEqual(double_char("String"),"SSttrriinngg")
        self.assertEqual(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
        self.assertEqual(double_char("1234!_ "),"11223344!!__  ")
# ---------------------------------------
# 49.
class Test_49_(unittest.TestCase):
    def test_str_count(self):
        self.assertEqual(str_count('hello', 'l'), 2)
        self.assertEqual(str_count('hello', 'e'), 1)
        self.assertEqual(str_count('codewars', 'c'), 1)
        self.assertEqual(str_count('ggggg', 'g'), 5)
        self.assertEqual(str_count('hello world', 'o'), 2)
        self.assertEqual(str_count('', 'z'), 0)
# ---------------------------------------
# 48.
class Test_48_(unittest.TestCase):
    def test_sp_eng(self):
        res = sp_eng()
        self.assertEqual(res.__equel__("english"), True)
        self.assertEqual(res.__equel__("egnlish"), False)
        self.assertEqual(res.__equel__("engliish"), False)
        self.assertEqual(res.__equel__("1234egn lis;h"), False)
        self.assertEqual(res.__equel__("1234english ;k"), True)
        self.assertEqual(res.__equel__("English"), True)
        self.assertEqual(res.__equel__("eNgliSh"), True)
        self.assertEqual(res.__equel__("1234#$%%eNglish ;k9"), True)
        self.assertEqual(res.__equel__("EGNlihs"), False)
        self.assertEqual(res.__equel__("1234englihs**"), False)
# ---------------------------------------
# 47.
class Test_47_(unittest.TestCase):
     def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)
        self.assertEqual(summation(22), 253)
        self.assertEqual(summation(100), 5050)
        self.assertEqual(summation(213), 22791)

# ---------------------------------------
# 46.
class Test_46_(unittest.TestCase):
    def test_fixed(self):
        self.assertEqual(to_alternating_case("hello world"), "HELLO WORLD")
        self.assertEqual(to_alternating_case("HELLO WORLD"), "hello world")
        self.assertEqual(to_alternating_case("hello WORLD"), "HELLO world")
        self.assertEqual(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
        self.assertEqual(to_alternating_case("12345"), "12345")
        self.assertEqual(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
        self.assertEqual(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
        self.assertEqual(to_alternating_case(to_alternating_case("Hello World")), "Hello World")

# ---------------------------------------
# 45.
class Test_45_(unittest.TestCase):
    def test_case(self):
        res = wrap("my_test")
        self.assertEqual(res["value"], "my_test")
        self.assertEqual(wrap(343)["value"], 343)
        obj = {"test":"testy"}
        self.assertEqual(wrap(obj)["value"], obj)

# ---------------------------------------
# 44.
class Test_44_(unittest.TestCase):
    def test_cases(self):
        def gen_test_case(inp, res):
            self.assertEqual(is_uppercase(inp), res, inp)
        gen_test_case("c", False)
        gen_test_case("C", True)
        gen_test_case("hello I AM DONALD", False)
        gen_test_case("HELLO I AM DONALD", True)
        gen_test_case("$%&", True)

# ---------------------------------------
# 43.
class Test_43_(unittest.TestCase):
    def test_grader(self):
        self.assertEqual(grader(1), "A")
        self.assertEqual(grader(1.01), "F")
        self.assertEqual(grader(0.20), "F")
        self.assertEqual(grader(0.70), "C")
        self.assertEqual(grader(0.80), "B")
        self.assertEqual(grader(0.90), "A")
        self.assertEqual(grader(0.60), "D")
        self.assertEqual(grader(0.50), "F")
        self.assertEqual(grader(0.00), "F")

# ---------------------------------------
# 42.
class Test_42_(unittest.TestCase):
    def test_subtract_sum(self):
    # from math import factorial


        for _ in range(100):
            n = randint(11,10000)
            # @test.it(f"testing for subtract_sum({n})")
            # def test_case(self):
            self.assertEqual(subtract_sum(n), "apple")
            self.assertEqual(subtract_sum(10),"apple")



# ---------------------------------------
# 41.
class Test_41_(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello world!"), "world! hello")
        self.assertEqual(reverse_words("yoda doesn't speak like this" ),  "this like speak doesn't yoda")
        self.assertEqual(reverse_words("foobar"                       ),  "foobar")
        self.assertEqual(reverse_words("kata editor"                  ),  "editor kata")
        self.assertEqual(reverse_words("row row row your boat"        ),  "boat your row row row")
# ---------------------------------------
# 40.
class Test_40_(unittest.TestCase):
    def test_cookie(self):
        self.assertEqual(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
        self.assertEqual(cookie(2.3), "Who ate the last cookie? It was Monica!")
        self.assertEqual(cookie(26), "Who ate the last cookie? It was Monica!")
        self.assertEqual(cookie(True), "Who ate the last cookie? It was the dog!")
        self.assertEqual(cookie("True"), "Who ate the last cookie? It was Zach!")
        self.assertEqual(cookie(False), "Who ate the last cookie? It was the dog!")
        self.assertEqual(cookie(1.98528462),"Who ate the last cookie? It was Monica!")
# ---------------------------------------
# 39.
class Test_39_(unittest.TestCase):
    def test_merge_arrays(self):
        self.assertEqual(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_arrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8])
# ---------------------------------------
# 38.
class Test_38_(unittest.TestCase):
    def test_who_is_paying(self):
        self.assertEqual(who_is_paying("Mexico"),["Mexico", "Me"])
        self.assertEqual(who_is_paying("Melania"),["Melania", "Me"])
        self.assertEqual(who_is_paying("Melissa"),["Melissa", "Me"])
        self.assertEqual(who_is_paying("Me"),["Me"])
        self.assertEqual(who_is_paying(""), [""])
        self.assertEqual(who_is_paying("I"), ["I"])
# 37.
class Test_37_(unittest.TestCase):
    def test_array_space(self):
        self.assertEqual(array_space('1,2,3'), '2')
        self.assertEqual(array_space('1,2,3,4'), '2 3')
        self.assertEqual(array_space('1,2,3,4,5'), '2 3 4')
    # @test.it("Should return None if the final result is an empty string")
    def test_array_space_none(self):
        self.assertEqual(array_space(''), None)
        self.assertEqual(array_space('1'), None)
        self.assertEqual(array_space('1,2'), None)

# ---------------------------------------
# 36.
class Test_36_(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
        self.assertEqual(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
        self.assertEqual(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
        self.assertEqual(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
        self.assertEqual(no_space('8j aam'), '8jaam')

# ---------------------------------------
# 35.
class Test_35_(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(add_binary(1, 1), "10")
        self.assertEqual(add_binary(0, 1), "1")
        self.assertEqual(add_binary(1, 0), "1")
        self.assertEqual(add_binary(2, 2), "100")
        self.assertEqual(add_binary(51, 12), "111111")


# ---------------------------------------
# # 34.
# # def fixed_tests():
# #     @test.it('Basic Test Cases')
# #     def basic_test_cases():
# #         test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
# #                            ['Hello', 'Hello Again'])
# #         test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
# #                            [1, 3, 5, 7, 9])
# #         test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
# #         test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
# #                            [['Goodbye']])


# # ---------------------------------------
# # 33.
# # def basic_tests():
# #     @test.it("Fixed tests")
# #     def fixed_tests():
# #         test.assert_equals(count_by(1, 5), [1, 2, 3, 4, 5])
# #         test.assert_equals(count_by(2, 5), [2, 4, 6, 8, 10])
# #         test.assert_equals(count_by(3, 5), [3, 6, 9, 12, 15])
# #         test.assert_equals(count_by(50, 5), [50, 100, 150, 200, 250])
# #         test.assert_equals(count_by(100, 5), [100, 200, 300, 400, 500])


# # ---------------------------------------
# # 32.
# class Count_sheeps(unittest.TestCase):
#     def tests_sheep(bass_in):
#         array1 = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True,
#                   True, True, True, True, False, False, True, True]
#         array2 = [True] * 500 + [None] * 5 + [False] * 100
#         array3 = []

#         result1 = count_sheeps(array1)
#         result2 = count_sheeps(array2)
#         result3 = count_sheeps(array3)

#         bass_in.assertEqual(result1, 17, f"There are 17 sheeps in total, not {result1}")
#         bass_in.assertEqual(result2, 500, f"There are 500 sheeps in total, not {result2}")
#         bass_in.assertEqual(result3, 0, f"There are 0 sheeps in total, not {result3}")

# # 31.
# class Problem(unittest.TestCase):
#     def test_problem(bass_in):
#         bass_in.assertEqual(problem("hello"), "Error")
#         bass_in.assertEqual(problem(1), 56)

# # 30.
# class Grow(unittest.TestCase):
#     def test_grow(bass_in):
#         tests = [
#             [6, [1, 2, 3]],
#             [16, [4, 1, 1, 1, 4]],
#             [64, [2, 2, 2, 2, 2, 2]],
#         ]

#         for exp, inp in tests:
#             bass_in.assertEqual(grow(inp), exp)

# # 29.
# class Get_volume_of_cuboid(unittest.TestCase):
#     def test_get_volume_of_cuboid(bass_in):
#         bass_in.assertEqual(get_volume_of_cuboid(1, 2, 2), 4)
#         bass_in.assertEqual(get_volume_of_cuboid(6.3, 2, 5), 63)

# # 28.
# class Powers_of_two(unittest.TestCase):
#     def test_power_of_two(bass_in):
#         bass_in.assertEqual(powers_of_two(0), [1])
#         bass_in.assertEqual(powers_of_two(1), [1, 2])
#         bass_in.assertEqual(powers_of_two(4), [1, 2, 4, 8, 16])

# # 27.
# class Past(unittest.TestCase):
#     def test_past(bass_in):
#         bass_in.assertEqual(past(0, 1, 1), 61000)
#         bass_in.assertEqual(past(1, 1, 1), 3661000)
#         bass_in.assertEqual(past(0, 0, 0), 0)
#         bass_in.assertEqual(past(1, 0, 1), 3601000)
#         bass_in.assertEqual(past(1, 0, 0), 3600000)

# # 26.
# class Solution_reversed_strings(unittest.TestCase):
#     def test_solution(bass_in):
#         bass_in.assertEqual(solution('world'), 'dlrow')
#         bass_in.assertEqual(solution('hello'), 'olleh')
#         bass_in.assertEqual(solution(''), '')
#         bass_in.assertEqual(solution('h'), 'h')


# # 25.
# class Century(unittest.TestCase):
#     def test_century(bass_in):
#         bass_in.assertEqual(century(1705), 18, 'Testing for year 1705')
#         bass_in.assertEqual(century(1900), 19, 'Testing for year 1900')
#         bass_in.assertEqual(century(1601), 17, 'Testing for year 1601')
#         bass_in.assertEqual(century(2000), 20, 'Testing for year 2000')
#         bass_in.assertEqual(century(356), 4, 'Testing for year 356')
#         bass_in.assertEqual(century(89), 1, 'Testing for year 89')


# # 24.
# class Repeat_str(unittest.TestCase):
#     def test_repeat_str(bass_in):
#         bass_in.assertEqual(repeat_str(4, 'a'), 'aaaa')
#         bass_in.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')
#         bass_in.assertEqual(repeat_str(2, 'abc'), 'abcabc')

# # 23.
# class Quadratic(unittest.TestCase):
#     def test_quadratic(bass_in):
#         bass_in.assertEqual(quadratic(0, 1), (1, -1, 0))
#         bass_in.assertEqual(quadratic(4, 9), (1, -13, 36))
#         bass_in.assertEqual(quadratic(2, 6), (1, -8, 12))
#         bass_in.assertEqual(quadratic(-5, -4), (1, 9, 20))

# # 22.
# class Is_uppercase(unittest.TestCase):
#     def test_is_uppercase(self):
#         self.assertEqual(is_uppercase("c"), False)
#         self.assertEqual(is_uppercase("C"), True)
#         self.assertEqual(is_uppercase("hello I AM DONALD"), False)
#         self.assertEqual(is_uppercase("HELLO I AM DONALD"), True)
#         self.assertEqual(is_uppercase("$%&"), True)

# # 21.
# class Abbrev_name(unittest.TestCase):
#     def test_addrev(bass_in):
#         bass_in.assertEqual(abbrev_name("Sam Harris"), "S.H")
#         bass_in.assertEqual(abbrev_name("patrick feenan"), "P.F")
#         bass_in.assertEqual(abbrev_name("Evan C"), "E.C")
#         bass_in.assertEqual(abbrev_name("P Favuzzi"), "P.F")
#         bass_in.assertEqual(abbrev_name("David Mendieta"), "D.M")

# # 20.
# class Lovefunc(unittest.TestCase):
#     def test_lovefunc(bass_in):
#         bass_in.assertEqual(lovefunc(1, 4), True)
#         bass_in.assertEqual(lovefunc(2, 2), False)
#         bass_in.assertEqual(lovefunc(0, 1), True)
#         bass_in.assertEqual(lovefunc(0, 0), False)
# # 19.
# class Is_palindrome(unittest.TestCase):
#     def tests_is_palindrome(bass_in):
#         bass_in.assertEqual(is_palindrome('a'), True)
#         bass_in.assertEqual(is_palindrome('aba'), True)
#         bass_in.assertEqual(is_palindrome('Abba'), True)
#         bass_in.assertEqual(is_palindrome('malam'), True)
#         bass_in.assertEqual(is_palindrome('walter'), False)
#         bass_in.assertEqual(is_palindrome('kodok'), True)
#         bass_in.assertEqual(is_palindrome('Kasue'), False)

# # 18.
# class Positive_sum(unittest.TestCase):
#     def test_positive_sum(bass_in):
#         bass_in.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
#         bass_in.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)
#         bass_in.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)
# # 17.
# class Digitize(unittest.TestCase):
#     def test_digitize(bass_in):
#         bass_in.assertEqual(digitize(35231), [1, 3, 2, 5, 3])
#         bass_in.assertEqual(digitize(0), [0])
#         bass_in.assertEqual(digitize(23582357), [7, 5, 3, 2, 8, 5, 3, 2])
#         bass_in.assertEqual(digitize(984764738), [8, 3, 7, 4, 6, 7, 4, 8, 9])
#         bass_in.assertEqual(digitize(45762893920), [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4])
#         bass_in.assertEqual(digitize(548702838394), [4, 9, 3, 8, 3, 8, 2, 0, 7, 8, 4, 5])

# # 16.
# class Opposite(unittest.TestCase):
#     def test_opposite(bass_in):
#         bass_in.assertEqual(opposite(1), -1)
#         bass_in.assertEqual(opposite(25.6), -25.6)
#         bass_in.assertEqual(opposite(0), 0)
#         bass_in.assertEqual(opposite(1425.2222), -1425.2222)
#         bass_in.assertEqual(opposite(-3.1458), 3.1458)
#         bass_in.assertEqual(opposite(-95858588225), 95858588225)


# # 15.
# class Check_for_factor(unittest.TestCase):
#     # def fixed_tests():
#         # @test.it("Should return True")
#     def test_should_return_true(bass_in):
#         bass_in.assertEqual(check_for_factor(10, 2), True)
#         bass_in.assertEqual(check_for_factor(63, 7), True)
#         bass_in.assertEqual(check_for_factor(2450, 5), True)
#         bass_in.assertEqual(check_for_factor(24612, 3), True)

#     # @test.it("Should return False")
#     def test_should_return_false(bass_in):
#         bass_in.assertEqual(check_for_factor(9, 2), False)
#         bass_in.assertEqual(check_for_factor(653, 7), False)
#         bass_in.assertEqual(check_for_factor(2453, 5), False)
#         bass_in.assertEqual(check_for_factor(24617, 3), False)

# # 14.
# class Greet(unittest.TestCase):
#     def test_greet(bass_in):
#         bass_in.assertEqual(greet('Ryan'), "Hello, Ryan how are you doing today?")
#         bass_in.assertEqual(greet('Shingles'), "Hello, Shingles how are you doing today?")

# # 13.
# class Am_i_wilson(unittest.TestCase):
#     def test_wilson_prime(bass_in):
#         for n, expected in (
#                 (0, False),
#                 (1, False),
#                 (5, True),
#                 (8, False),
#                 (9, False)
#         ):
#             bass_in.assertEqual(am_i_wilson(n), expected, f"Test failed for n = {n}")


# # 12.
# # from tasks.codeWars_tasks.codeWars import *
# # class Dna_to_rna(unittest.TestCase):
# #     def test_dna_to_rna(bass_in):
# #         bass_in.assertEqual(dna_to_rna("TTTT"), "UUUU")
# #         bass_in.assertEqual(dna_to_rna("GCAT"), "GCAU")
# #         bass_in.assertEqual(dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")
# # 11.
# class Expression_matter(unittest.TestCase):
#     def test_expression_matter(bass_in):
#         bass_in.assertEqual(expression_matter(2, 1, 2), 6)
#         bass_in.assertEqual(expression_matter(2, 1, 1), 4)
#         bass_in.assertEqual(expression_matter(2, 2, 4), 16)
#         bass_in.assertEqual(expression_matter(3, 3, 3), 27)
#         bass_in.assertEqual(expression_matter(1, 1, 1), 3)
#         bass_in.assertEqual(expression_matter(1, 2, 3), 9)
#         bass_in.assertEqual(expression_matter(1, 3, 1), 5)
#         bass_in.assertEqual(expression_matter(2, 2, 2), 8)
#         bass_in.assertEqual(expression_matter(5, 1, 3), 20)
#         bass_in.assertEqual(expression_matter(3, 5, 7), 105)
#         bass_in.assertEqual(expression_matter(5, 6, 1), 35)
#         bass_in.assertEqual(expression_matter(1, 6, 1), 8)
#         bass_in.assertEqual(expression_matter(2, 6, 1), 14)
#         bass_in.assertEqual(expression_matter(6, 7, 1), 48)
#         bass_in.assertEqual(expression_matter(2, 10, 3), 60)
#         bass_in.assertEqual(expression_matter(1, 8, 3), 27)
#         bass_in.assertEqual(expression_matter(9, 7, 2), 126)
#         bass_in.assertEqual(expression_matter(1, 1, 10), 20)
#         bass_in.assertEqual(expression_matter(9, 1, 1), 18)
#         bass_in.assertEqual(expression_matter(10, 5, 6), 300)
#         bass_in.assertEqual(expression_matter(1, 10, 1), 12)

# # 10.
# class Twic_as(unittest.TestCase):
#     def test_twice_as_old(bass_in):
#         bass_in.assertEqual(twice_as_old(36, 7), 22)
#         bass_in.assertEqual(twice_as_old(55, 30), 5)
#         bass_in.assertEqual(twice_as_old(42, 21), 0)
#         bass_in.assertEqual(twice_as_old(22, 1), 20)
#         bass_in.assertEqual(twice_as_old(29, 0), 29)


# # 9.
# class Make_negative(unittest.TestCase):
#     def test_make_negative(bsss_in):
#         for n, expected in ((42, -42), (-9, -9), (0, 0)):
#             actual = make_negative(n)
#             message = f"For n = {n}, expected {expected} but got {actual}"
#             bsss_in.assertEqual(actual, expected, message)

# # 8.
# class Find_multiples(unittest.TestCase):
#     def test_find_multiples(bass_in):
#         bass_in.assertEqual(find_multiples(5, 25), [5, 10, 15, 20, 25])
#         bass_in.assertEqual(find_multiples(1, 2), [1, 2])
#         bass_in.assertEqual(find_multiples(5, 7), [5])
#         bass_in.assertEqual(find_multiples(4, 27), [4, 8, 12, 16, 20, 24])
#         bass_in.assertEqual(find_multiples(11, 54), [11, 22, 33, 44])
# # 7
# class Derive(unittest.TestCase):
#     def test_derive(bass_in):
#         bass_in.assertEqual(derive(7, 8), "56x^7")
#         bass_in.assertEqual(derive(5, 9), "45x^8")
# # 6.
# # class Hero(unittest.TestCase):
# #     def test_hero(bass_in):
# #         bass_in.assertEqual(hero(10, 5), True)
# #         bass_in.assertEqual(hero(7, 4), False)
# #         bass_in.assertEqual(hero(4, 5), False)
# #         bass_in.assertEqual(hero(100, 40), True)
# #         bass_in.assertEqual(hero(1500, 751), False)
# #         bass_in.assertEqual(hero(0, 1), False)
# # 5.
# class Update_light(unittest.TestCase):
#     def test_update_light(bass_in):
#         bass_in.assertEqual(update_light('green'), 'yellow')
#         bass_in.assertEqual(update_light('yellow'), 'red')
#         bass_in.assertEqual(update_light('red'), 'green')

# # 4.
# class Liters(unittest.TestCase):
#     def test_liters(bass_in):
#         bass_in.assertEqual(litres(2), 1, 'should return 1 litre')
#         bass_in.assertEqual(litres(1.4), 0, 'should return 0 litres')
#         bass_in.assertEqual(litres(12.3), 6, 'should return 6 litres')
#         bass_in.assertEqual(litres(0.82), 0, 'should return 0 litres')
#         bass_in.assertEqual(litres(11.8), 5, 'should return 5 litres')
#         bass_in.assertEqual(litres(1787), 893, 'should return 893 litres')
#         bass_in.assertEqual(litres(0), 0, 'should return 0 litres')


# 3.
class Test_03_Points_t(unittest.TestCase):
    def test_points(bass_in):
        bass_in.assertEqual(
            points(
                ["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"]
            ),
            30,
        )
        bass_in.assertEqual(
            points(
                ["1:1", "2:2", "3:3", "4:4", "2:2", "3:3", "4:4", "3:3", "4:4", "4:4"]
            ),
            10,
        )
        bass_in.assertEqual(
            points(
                ["0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4"]
            ),
            0,
        )
        bass_in.assertEqual(
            points(
                ["1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"]
            ),
            15,
        )
        bass_in.assertEqual(
            points(
                ["1:0", "2:0", "3:0", "4:4", "2:2", "3:3", "1:4", "2:3", "2:4", "3:4"]
            ),
            12,
        )


# 2.
class Test_02_Validate_hello(unittest.TestCase):
    def test_validate_hello(bass_in):
        # bass_in.assertEqual(validate_hello('hello'), True)
        # bass_in.assertEqual(validate_hello('ciao bella!'), True)
        for inp, exp in [
            ("hello", True),
            ("ciao bella!", True),
            ("salut", True),
            ("hallo, salut", True),
            ("hombre! Hola!", True),
            ("Hallo, wie geht's dir?", True),
            ("AHOJ!", True),
            ("czesc", True),
            ("meh", False),
            ("Ahoj", True),
        ]:
            bass_in.assertEqual(
                validate_hello(inp), exp, f"Testing for validate_hello({inp!r})"
            )


# 1.
class Test_01_NameShuffler(unittest.TestCase):
    def test_name_shuffler(bass_in):
        bass_in.assertEqual(name_shuffler("William O'Brien"), "O'Brien William")
        bass_in.assertEqual(name_shuffler("john McClane"), "McClane john")
        (bass_in.assertEqual(name_shuffler("john McClane"), "McClane john"),)
        (bass_in.assertEqual(name_shuffler("Mary jeggins"), "jeggins Mary"),)
        (bass_in.assertEqual(name_shuffler("tom jerry"), "jerry tom"),)
        (bass_in.assertEqual(name_shuffler("Mary Jane"), "Jane Mary"),)
        (bass_in.assertEqual(name_shuffler("John Doe"), "Doe John"),)
        (bass_in.assertEqual(name_shuffler("William O'Brien"), "O'Brien William"),)
        bass_in.assertEqual(
            name_shuffler("George Huffingquane-McGafferty"),
            "Huffingquane-McGafferty George",
        )
