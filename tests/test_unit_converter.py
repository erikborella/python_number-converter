import unittest
import unit_converter


class TestGetFractionalPart(unittest.TestCase):
    def test_None_return(self):
        self.assertEqual(None, unit_converter.get_fractional_part(10))
        self.assertEqual(None, unit_converter.get_fractional_part(0))
        self.assertEqual(None, unit_converter.get_fractional_part(None))

    def test_zero_return(self):
        self.assertEqual('0', unit_converter.get_fractional_part(10.0))

    def test_normal_return(self):
        self.assertEqual('5', unit_converter.get_fractional_part(10.5))
        self.assertEqual('5', unit_converter.get_fractional_part(10.50))
        self.assertEqual('5', unit_converter.get_fractional_part(0.5))


class TestIntegerDecimalToAnyBase(unittest.TestCase):
    def test_binary_convert(self):
        self.assertEqual('1010', unit_converter.integer_decimal_to_any_base(10, 2))
        self.assertEqual('1010', unit_converter.integer_decimal_to_any_base(10.1, 2))
        self.assertEqual('11111111', unit_converter.integer_decimal_to_any_base(255, 2))

    def test_octal_convert(self):
        self.assertEqual('12', unit_converter.integer_decimal_to_any_base(10, 8))
        self.assertEqual('12', unit_converter.integer_decimal_to_any_base(10.1, 8))
        self.assertEqual('377', unit_converter.integer_decimal_to_any_base(255, 8))

    def test_decimal_convert(self):
        self.assertEqual('10', unit_converter.integer_decimal_to_any_base(10, 10))
        self.assertEqual('10', unit_converter.integer_decimal_to_any_base(10.1, 10))
        self.assertEqual('255', unit_converter.integer_decimal_to_any_base(255, 10))

    def test_hexadecimal_convert(self):
        self.assertEqual('A', unit_converter.integer_decimal_to_any_base(10, 16))
        self.assertEqual('A', unit_converter.integer_decimal_to_any_base(10.1, 16))
        self.assertEqual('FF', unit_converter.integer_decimal_to_any_base(255, 16))


class TestFloatingDecimalToAnyBase(unittest.TestCase):
    def test_binary_convert(self):
        self.assertEqual('1010.0', unit_converter.floating_decimal_to_any_base(10, 2))
        self.assertEqual('1010.0', unit_converter.floating_decimal_to_any_base(10.0, 2))
        self.assertEqual('1010.1', unit_converter.floating_decimal_to_any_base(10.10, 2))
        self.assertEqual('11111111.11111111', unit_converter.floating_decimal_to_any_base(255.255, 2))

    def test_octal_convert(self):
        self.assertEqual('12.0', unit_converter.floating_decimal_to_any_base(10, 8))
        self.assertEqual('12.0', unit_converter.floating_decimal_to_any_base(10.0, 8))
        self.assertEqual('12.1', unit_converter.floating_decimal_to_any_base(10.1, 8))
        self.assertEqual('377.377', unit_converter.floating_decimal_to_any_base(255.255, 8))

    def test_decimal_convert(self):
        self.assertEqual('10.0', unit_converter.floating_decimal_to_any_base(10, 10))
        self.assertEqual('10.0', unit_converter.floating_decimal_to_any_base(10.0, 10))
        self.assertEqual('10.1', unit_converter.floating_decimal_to_any_base(10.1, 10))
        self.assertEqual('255.255', unit_converter.floating_decimal_to_any_base(255.255, 10))

    def test_hexadecimal_convert(self):
        self.assertEqual('A.0', unit_converter.floating_decimal_to_any_base(10, 16))
        self.assertEqual('A.0', unit_converter.floating_decimal_to_any_base(10.0, 16))
        self.assertEqual('A.1', unit_converter.floating_decimal_to_any_base(10.1, 16))
        self.assertEqual('FF.FF', unit_converter.floating_decimal_to_any_base(255.255, 16))


class TestDecimalToAnyBase(unittest.TestCase):
    def test_binary_convert(self):
        self.assertEqual('1010', unit_converter.decimal_to_any_base(10, 2))
        self.assertEqual('1010', unit_converter.decimal_to_any_base(10.0, 2))
        self.assertEqual('1010.1', unit_converter.decimal_to_any_base(10.1, 2))

    def test_octal_convert(self):
        self.assertEqual('12', unit_converter.decimal_to_any_base(10, 8))
        self.assertEqual('12', unit_converter.decimal_to_any_base(10.0, 8))
        self.assertEqual('12.1', unit_converter.decimal_to_any_base(10.1, 8))

    def test_decimal_convert(self):
        self.assertEqual('10', unit_converter.decimal_to_any_base(10, 10))
        self.assertEqual('10', unit_converter.decimal_to_any_base(10.0, 10))
        self.assertEqual('10.1', unit_converter.decimal_to_any_base(10.1, 10))

    def test_hexadecimal_convert(self):
        self.assertEqual('A', unit_converter.decimal_to_any_base(10, 16))
        self.assertEqual('A', unit_converter.decimal_to_any_base(10.0, 16))
        self.assertEqual('A.1', unit_converter.decimal_to_any_base(10.1, 16))


class TestIntegerAnyBaseToDecimal(unittest.TestCase):
    def test_binary_convert(self):
        self.assertEqual(10, unit_converter.integer_any_base_to_decimal('1010', 2))
        self.assertEqual(255, unit_converter.integer_any_base_to_decimal('11111111', 2))

    def test_octal_convert(self):
        self.assertEqual(10,  unit_converter.integer_any_base_to_decimal('12', 8))
        self.assertEqual(255, unit_converter.integer_any_base_to_decimal('377', 8))

    def test_decimal_convert(self):
        self.assertEqual(10, unit_converter.integer_any_base_to_decimal('10', 10))
        self.assertEqual(255, unit_converter.integer_any_base_to_decimal('255', 10))

    def test_hexadecimal_convert(self):
        self.assertEqual(10, unit_converter.integer_any_base_to_decimal('A', 16))
        self.assertEqual(255, unit_converter.integer_any_base_to_decimal('FF', 16))


class TestFloatingAnyBaseToDecimal(unittest.TestCase):
    def test_binary_convert(self):
        self.assertEqual('10.1', unit_converter.floating_any_base_to_decimal('1010.1', 2))
        self.assertEqual('255.255', unit_converter.floating_any_base_to_decimal('11111111.11111111', 2))

    def test_octal_convert(self):
        self.assertEqual('10.1', unit_converter.floating_any_base_to_decimal('12.1', 8))
        self.assertEqual('255.255', unit_converter.floating_any_base_to_decimal('377.377', 8))

    def test_decimal_convert(self):
        self.assertEqual('10.1', unit_converter.floating_any_base_to_decimal('10.1', 10))
        self.assertEqual('255.255', unit_converter.floating_any_base_to_decimal('255.255', 10))

    def test_hexadecimal_convert(self):
        self.assertEqual('10.1', unit_converter.floating_any_base_to_decimal('A.1', 16))
        self.assertEqual('255.255', unit_converter.floating_any_base_to_decimal('FF.FF', 16))


if __name__ == '__main__':
    unittest.main()
