"""
Test file for testing the utility class at utils\string.py
"""

# Importing the required libraries
import os
import sys
import locale
import unittest

# Adding project path to the sys.path
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils.string as str
import utils.datetime as dttm


class TestString(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setup method for the test class
        """
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_is_string(self):
        """
        Test method to check if text is a string
        """
        # Test valid string
        self.assertTrue(str.is_string("This is a string"))
        self.assertTrue(str.is_string("123.456"))
        self.assertTrue(str.is_string(""))

    def test_is_full_string(self):
        """
        Test method to check if text is a full string
        """
        # Test valid full string
        self.assertTrue(str.is_full_string("This is a string"))
        self.assertTrue(str.is_full_string("123.456"))
        self.assertFalse(str.is_full_string(""))

    def test_is_multiline(self):
        """
        Test method to check if text is a multiline string
        """
        # Test valid multiline string
        self.assertTrue(str.is_multiline("This is a multiline string\nThis is a multiline string"))
        self.assertTrue(str.is_multiline("123.456\n123.456"))
        self.assertFalse(str.is_multiline("This is a string"))

    def test_is_alpha(self):
        """
        Test method to check if text is an alphabetic string
        """
        # Test valid alphabetic string
        self.assertTrue(str.is_alpha("abc"))
        self.assertTrue(str.is_alpha("efgddgwáéíóúÁÉÍÓÚ"))
        self.assertFalse(str.is_alpha("abc 123"))
        self.assertFalse(str.is_alpha("abc-123"))

    def test_is_alphanumeric(self):
        """
        Test method to check if text is an alphanumeric string
        """
        # Test valid alphanumeric string
        self.assertTrue(str.is_alphanumeric("abc123"))
        self.assertTrue(str.is_alphanumeric("123abc"))
        self.assertFalse(str.is_alphanumeric("abc 123"))
        self.assertFalse(str.is_alphanumeric("abc-123"))

    def test_is_number(self):
        """
        Test method to check if text is a number
        """
        # Test valid number
        self.assertTrue(str.is_number("123"))
        self.assertTrue(str.is_number("123,456"))
        self.assertTrue(str.is_number("-9,12"))
        self.assertTrue(str.is_number("1e3"))

        # Test invalid number
        self.assertFalse(str.is_number("123-456"))
        self.assertFalse(str.is_number("123.456"))
        self.assertFalse(str.is_number("123 456"))
        self.assertFalse(str.is_number("abc"))
        self.assertFalse(str.is_number("abc 123"))
        self.assertFalse(str.is_number("abc-123"))

    def test_is_integer(self):
        """
        Test method to check if text is a parseable int string
        """
        # Test valid integer
        self.assertTrue(str.is_integer("123"))
        self.assertTrue(str.is_integer("-123"))
        self.assertTrue(str.is_integer("+123"))
        self.assertTrue(str.is_integer("0"))
        self.assertTrue(str.is_integer("000"))
        self.assertTrue(str.is_integer("000123"))
        self.assertTrue(str.is_integer("123000"))

        # Test invalid integer
        self.assertFalse(str.is_integer("123.456"))
        self.assertFalse(str.is_integer("123,456"))
        self.assertFalse(str.is_integer("123 456"))
        self.assertFalse(str.is_integer("123-456"))

    def test_is_decimal(self):
        """
        Test method to check if text is a parseable float string
        """
        # Test valid decimal
        self.assertTrue(str.is_decimal("123,456"))
        self.assertTrue(str.is_decimal("-123,456"))
        self.assertTrue(str.is_decimal("+123,456"))
        self.assertTrue(str.is_decimal("0,0"))
        self.assertTrue(str.is_decimal("000,000"))
        self.assertTrue(str.is_decimal("000123,456"))
        self.assertTrue(str.is_decimal("123000,456"))

        # Test invalid decimal
        self.assertFalse(str.is_decimal("000123"))
        self.assertFalse(str.is_decimal("123.456"))
        self.assertFalse(str.is_decimal("123 456"))
        self.assertFalse(str.is_decimal("123-456"))

    def test_is_datetime(self):
        """
        Test method to check if text is a datetime string
        
        *Examples:*

        >>> is_datetime('2018-01-01 12:00:00') # returns true
        >>> is_datetime('25/01/2018 12:00') # returns true
        >>> is_datetime('25/1/2018 12:30:00') # returns true

        >>> is_datetime('2018-01-01') # returns false
        >>> is_datetime('1/25/2018') # returns false
        >>> is_datetime('1/1/2018 12:99') # returns false
        >>> is_datetime('25/1/2018 12:99') # returns false
        >>> is_datetime('25/01/2018 12:00:99') # returns false
        """
        # Test valid datetime
        self.assertTrue(dttm.is_parseable("2018-01-01 12:00:00"))
        self.assertTrue(dttm.is_parseable("25/01/2018 12:00"))
        self.assertTrue(dttm.is_parseable("25/1/2018 12:30:00"))
        # Test invalid datetime
        self.assertFalse(dttm.is_parseable("2018-01-01"))
        self.assertFalse(dttm.is_parseable("1/25/2018"))
        self.assertFalse(dttm.is_parseable("1/1/2018 12:99"))
        self.assertFalse(dttm.is_parseable("25/1/2018 12:99"))
        self.assertFalse(dttm.is_parseable("25/01/2018 12:00:99"))
        
    def test_is_date(self):
        """
        Test method to check if text is a date string
        
        *Examples:*

        >>> is_date('2018-01-01') # returns true
        >>> is_date('2018-01-01 12:00:00') # returns false
        """
        # Test valid date
        self.assertTrue(str.is_date("2018-01-01"))
        self.assertFalse(str.is_date("2018-01-01 12:00:00"))

    # def test_is_time(self):

    # def test_is_bool(self):

    # def test_is_path(self):

    # def test_is_filename(self):

    # def test_is_url(self):

    # def test_is_ip(self):

    # def test_is_hostname(self):

    # def test_is_domain(self):

    # def test_is_email(self):

    # def test_is_password(self):

    # def test_is_json(self):

    # def test_is_xml(self):