import unittest
import unit_converter


class TestGetFractionalPart(unittest.TestCase):
    def test_None_return(self):
        self.assertEqual(None, unit_converter.get_fractional_part(10))
        self.assertEqual(None, unit_converter.get_fractional_part(0))
        self.assertEqual(None, unit_converter.get_fractional_part(None))

    def test_zero_return(self):
        self.assertEqual(0, unit_converter.get_fractional_part(10.0))

    def test_normal_return(self):
        self.assertEqual(5, unit_converter.get_fractional_part(10.5))
        self.assertEqual(5, unit_converter.get_fractional_part(10.50))
        self.assertEqual(5, unit_converter.get_fractional_part(0.5))


if __name__ == '__main__':
    unittest.main()
