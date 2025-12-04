# unittest
# based on junit
# compatible with pytest.
# part of the standard lib
# subclasses
# test_ - auto discoverable

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_calculator_class_instance(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_calculator_has_add_method(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_raises_error(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom error: must be numeric"):
            calc.add("a", 5)

    def test_add_method_logic(self):
        calc = Calculator()
        self.assertEqual(calc.add(5,5), 10)
        self.assertEqual(calc.add(10,10), 20)
        self.assertEqual(calc.add(-1,-1), -2)

