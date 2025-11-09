import unittest
import math
from app import (
    is_valid_email,
    circle_area,
    filter_even,
    convert_date_format,
    is_palindrome
)

class TestFunkcje(unittest.TestCase):
# Klasa testowa dla funkcji z modułu 'app'.

    def setUp(self):
        # Dane dla testów parametryzowanych (is_valid_email)
        self.valid_emails = [
            "test.user@example.com",
            "a@b.co",
            "name.surname123@sub.domain.pl",
            "u-ser_1@dom-ena.com"
        ]
        self.invalid_emails = [
            "zly_adres",
            "user@domain",    
            "user@.com",
            "user@domain.c",
            "user@domena."
        ]

        # Dane dla testów parametryzowanych (is_palindrome)
        self.palindromes = [
            "kajak",
            "anna",
            "A nut for a jar of tuna",
            "Kobyła ma mały bok",
            "",
            "a",
            "!@#$"
        ]
        self.non_palindromes = [
            "palindrom",
            "abacabae"
        ]

    # 1. TESTY DLA is_valid_email
    def test_email_valid_cases(self):
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), f"Oczekiwano True dla: {email}")

    def test_email_invalid_cases(self):
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"Oczekiwano False dla: {email}")

    # 2. TESTY DLA circle_area
    def test_area_typical_cases(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), math.pi * 4)
        self.assertAlmostEqual(circle_area(0.5), math.pi * 0.25)

    def test_area_edge_case_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_invalid_input(self):
        with self.assertRaises(ValueError):
            circle_area(-5)

    # 3. TESTY DLA filter_even
    def test_filter_typical_cases(self):
        self.assertEqual(filter_even([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_filter_edge_cases(self):
        self.assertEqual(filter_even([]), [])
        self.assertEqual(filter_even([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(filter_even([1, 3, 5, 7]), [])
        self.assertEqual(filter_even([0]), [0])

    def test_filter_negative_numbers(self):
        self.assertEqual(filter_even([-1, -2, -3, -4]), [-2, -4])

    # 4. TESTY DLA convert_date_format
    def test_date_typical_cases(self):
        self.assertEqual(convert_date_format("31-12-2023"), "2023/12/31")
        self.assertEqual(convert_date_format("01-01-2000"), "2000/01/01")

    def test_date_edge_cases(self):
        self.assertEqual(convert_date_format("05-08-2025"), "2025/08/05")
        self.assertEqual(convert_date_format("29-02-2024"), "2024/02/29")

    def test_date_invalid_input(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/12/31")
        with self.assertRaises(ValueError):
            convert_date_format("30-02-2023")
        with self.assertRaises(ValueError):
            convert_date_format("99-99-9999")

    # 5. TESTY DLA is_palindrome
    def test_palindrome_true_cases(self):
        for text in self.palindromes:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text), f"Oczekiwano True dla: '{text}'")

    def test_palindrome_false_cases(self):
        for text in self.non_palindromes:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text), f"Oczekiwano False dla: '{text}'")


if __name__ == '__main__':
    unittest.main()
