import unittest

from server.calculator import calculator


class ReturnedErrorsTests(unittest.TestCase):

    def test_invalid_argument(self):
        key, value = calculator("34dts", "56", "+")
        self.assertEqual((key, value), ('error', 'Не верный агрумент'))

    def test_invalid_argument_1(self):
        key, value = calculator("34%", "56", "+")
        self.assertNotEqual((key, value), ('error', 'Не верный агрумент'))

    def test_invalid_argument_2(self):
        key, value = calculator("3%4", "56", "+")
        self.assertEqual((key, value), ('error', 'Не верный агрумент'))

    def test_zero_division(self):
        key, value = calculator("34", "0", "/")
        self.assertEqual((key, value), ('error', 'Деление на ноль невозможно'))

    def test_unsupported_operation(self):
        key, value = calculator("34", "34", "//")
        self.assertEqual((key, value), ('error', 'Неподдерживаемая операция'))

class BasicOperationsTests(unittest.TestCase):

    def test_summarize(self):
        key, value = calculator("2", "2", "+")
        self.assertEqual((key, value), ('result', 4))

    def test_substitution(self):
        key, value = calculator("12", "2", "-")
        self.assertEqual((key, value), ('result', 10))

    def test_multiply(self):
        key, value = calculator("20", "5", "*")
        self.assertEqual((key, value), ('result', 100))

    def test_division_fgs(self):
        key, value = calculator("50", "25", "/")
        self.assertEqual((key, value), ('result', 2))

    def test_division_fls(self):
        key, value = calculator("25", "50", "/")
        self.assertEqual((key, value), ('result', 0.5))

class PercentLogicTests(unittest.TestCase):

    def test_two_arg_percent_summarize(self):
        key, value = calculator("50%", "20%", "+")
        self.assertEqual((key, value), ('result', 0.7))

    def test_two_arg_percent_substitution(self):
        key, value = calculator("50%", "20%", "-")
        self.assertEqual((key, value), ('result', 0.3))

    def test_two_arg_percent_multiply(self):
        key, value = calculator("50%", "20%", "*")
        self.assertEqual((key, value), ('result', 0.1))

    def test_two_arg_percent_division_fgs(self):
        key, value = calculator("50%", "20%", "/")
        self.assertEqual((key, value), ('result', 2.5))

    def test_two_arg_percent_division_fls(self):
        key, value = calculator("20%", "50%", "/")
        self.assertEqual((key, value), ('result', 0.4))

#-----------------------------------------------------------------------------

    def test_first_arg_percent_summarize(self):
        key, value = calculator("50%", "20", "+")
        self.assertEqual((key, value), ('result', 20.5))

    def test_first_arg_percent_substitution(self):
        key, value = calculator("50%", "20", "-")
        self.assertEqual((key, value), ('result', -19.5))

    def test_first_arg_percent_multiply(self):
        key, value = calculator("50%", "20", "*")
        self.assertEqual((key, value), ('result', 10))

    def test_first_arg_percent_division_fgs(self):
        key, value = calculator("50%", "20", "/")
        self.assertEqual((key, value), ('result', 0.025))

    def test_first_arg_percent_division_fls(self):
        key, value = calculator("20%", "50", "/")
        self.assertEqual((key, value), ('result', 0.004))

#-----------------------------------------------------------------------

    def test_second_arg_percent_summarize(self):
        key, value = calculator("50", "20%", "+")
        self.assertEqual((key, value), ('result', 60))

    def test_second_arg_percent_substitution(self):
        key, value = calculator("50", "20%", "-")
        self.assertEqual((key, value), ('result', 40))

    def test_second_arg_percent_multiply(self):
        key, value = calculator("50", "20%", "*")
        self.assertEqual((key, value), ('result', 10))

    def test_second_arg_percent_division_fgs(self):
        key, value = calculator("50", "20%", "/")
        self.assertEqual((key, value), ('result', 250))

    def test_second_arg_percent_division_fls(self):
        key, value = calculator("20", "50%", "/")
        self.assertEqual((key, value), ('result', 40))


if __name__ == '__main__':
    unittest.main()
