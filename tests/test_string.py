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
import utils.string.validation as sv
import utils.datetime.validation as dt


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
        self.assertTrue(sv.is_string("This is a string"))
        self.assertTrue(sv.is_string("123.456"))
        self.assertTrue(sv.is_string(""))

    def test_is_full_string(self):
        """
        Test method to check if text is a full string
        """
        # Test valid full string
        self.assertTrue(sv.is_full_string("This is a string"))
        self.assertTrue(sv.is_full_string("123.456"))
        self.assertFalse(sv.is_full_string(""))

    def test_is_multiline(self):
        """
        Test method to check if text is a multiline string
        """
        # Test valid multiline string
        self.assertTrue(sv.is_multiline("This is a multiline string\nThis is a multiline string"))
        self.assertTrue(sv.is_multiline("123.456\n123.456"))
        self.assertFalse(sv.is_multiline("This is a string"))

    def test_is_alpha(self):
        """
        Test method to check if text is an alphabetic string
        """
        # Test valid alphabetic string
        self.assertTrue(sv.is_alpha("abc"))
        self.assertTrue(sv.is_alpha("efgddgwáéíóúÁÉÍÓÚ"))
        self.assertFalse(sv.is_alpha("abc 123"))
        self.assertFalse(sv.is_alpha("abc-123"))

    def test_is_alphanumeric(self):
        """
        Test method to check if text is an alphanumeric string
        """
        # Test valid alphanumeric string
        self.assertTrue(sv.is_alphanumeric("abc123"))
        self.assertTrue(sv.is_alphanumeric("123abc"))
        self.assertFalse(sv.is_alphanumeric("abc 123"))
        self.assertFalse(sv.is_alphanumeric("abc-123"))

    def test_is_number(self):
        """
        Test method to check if text is a number
        """
        # Test valid number
        self.assertTrue(sv.is_number("123"))
        self.assertTrue(sv.is_number("123,456"))
        self.assertTrue(sv.is_number("-9,12"))
        self.assertTrue(sv.is_number("1e3"))

        # Test invalid number
        self.assertFalse(sv.is_number("123-456"))
        self.assertFalse(sv.is_number("123.456"))
        self.assertFalse(sv.is_number("123 456"))
        self.assertFalse(sv.is_number("abc"))
        self.assertFalse(sv.is_number("abc 123"))
        self.assertFalse(sv.is_number("abc-123"))

    def test_is_integer(self):
        """
        Test method to check if text is a parseable int string
        """
        # Test valid integer
        self.assertTrue(sv.is_integer("123"))
        self.assertTrue(sv.is_integer("-123"))
        self.assertTrue(sv.is_integer("+123"))
        self.assertTrue(sv.is_integer("0"))
        self.assertTrue(sv.is_integer("000"))
        self.assertTrue(sv.is_integer("000123"))
        self.assertTrue(sv.is_integer("123000"))

        # Test invalid integer
        self.assertFalse(sv.is_integer("123.456"))
        self.assertFalse(sv.is_integer("123,456"))
        self.assertFalse(sv.is_integer("123 456"))
        self.assertFalse(sv.is_integer("123-456"))

    def test_is_decimal(self):
        """
        Test method to check if text is a parseable float string
        """
        # Test valid decimal
        self.assertTrue(sv.is_decimal("123,456"))
        self.assertTrue(sv.is_decimal("-123,456"))
        self.assertTrue(sv.is_decimal("+123,456"))
        self.assertTrue(sv.is_decimal("0,0"))
        self.assertTrue(sv.is_decimal("000,000"))
        self.assertTrue(sv.is_decimal("000123,456"))
        self.assertTrue(sv.is_decimal("123000,456"))

        # Test invalid decimal
        self.assertFalse(sv.is_decimal("000123"))
        self.assertFalse(sv.is_decimal("123.456"))
        self.assertFalse(sv.is_decimal("123 456"))
        self.assertFalse(sv.is_decimal("123-456"))

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
        self.assertTrue(dt.is_parseable("2018-01-01 12:00:00"))
        self.assertTrue(dt.is_parseable("25/01/2018 12:00"))
        self.assertTrue(dt.is_parseable("25/1/2018 12:30:00"))
        # Test invalid datetime
        self.assertFalse(dt.is_parseable("1/1/2018 12:99"))
        self.assertFalse(dt.is_parseable("25/1/2018 12:99"))
        self.assertFalse(dt.is_parseable("25/01/2018 12:00:99"))
        
    # def test_is_date(self):

    # def test_is_time(self):

    def test_is_bool(self):
        """
        Test method to check if text is a boolean string
        """
        # Test valid boolean
        self.assertTrue(sv.is_bool("True"))
        self.assertTrue(sv.is_bool("False"))
        self.assertTrue(sv.is_bool("true"))
        self.assertTrue(sv.is_bool("false"))
        self.assertTrue(sv.is_bool("1"))
        self.assertTrue(sv.is_bool("0"))

        # Test invalid boolean
        self.assertFalse(sv.is_bool("truefalse"))
        self.assertFalse(sv.is_bool("123"))
        self.assertFalse(sv.is_bool("abc"))
        self.assertFalse(sv.is_bool(""))

    def test_is_path(self):
        """
        Test method to check if text is a path string
        """
        # Test valid path
        self.assertTrue(sv.is_path("C:/Users/User/Documents/file.txt"))
        self.assertTrue(sv.is_path("c:\\Users\\User\\Documents\\file.txt"))
        self.assertTrue(sv.is_path("\\Documents\\file.txt"))
        self.assertTrue(sv.is_path("/Documents/file.txt"))

        # Test invalid path
        self.assertFalse(sv.is_path("file.txt"))
        self.assertFalse(sv.is_path("file"))
        self.assertFalse(sv.is_path("123"))

    def test_is_filename(self):
        """
        Test method to check if text is a filename string
        """
        # Test valid filename
        self.assertTrue(sv.is_filename("file.txt"))
        self.assertTrue(sv.is_filename("file sdf.txt"))
        self.assertTrue(sv.is_filename("file-sdf (2).txt"))

        # Test invalid filename
        self.assertFalse(sv.is_filename("file"))
        self.assertFalse(sv.is_filename("file-sdf"))
        self.assertFalse(sv.is_filename("C:/Users/User/Documents/file.txt"))
        self.assertFalse(sv.is_filename("c:\\Users\\User\\Documents\\file.txt"))
        self.assertFalse(sv.is_filename("\\Documents\\file.txt"))
        self.assertFalse(sv.is_filename("/Documents/file.txt"))

    def test_is_url(self):
        """
        Test method to check if text is a url string
        """
        # Test valid url
        self.assertTrue(sv.is_url("http://www.google.com"))
        self.assertTrue(sv.is_url("https://www.google.com/"))
        self.assertTrue(sv.is_url("http://www.google.com/path/to/file"))
        self.assertTrue(sv.is_url("https://www.google.com/path/to/file/"))
        self.assertTrue(sv.is_url("http://www.google.com/path/to/file?param1=value1&param2=value2"))
        self.assertTrue(sv.is_url("https://www.google.com/path/to/file/#anchor"))
        self.assertTrue(sv.is_url("http://www.google.com/path/to/file?param1=value1&param2=value2#anchor"))
        self.assertTrue(sv.is_url("ftp://15.142.85.1:8080"))

        # Test invalid url
        self.assertFalse(sv.is_url("15.142.85.1:8080"))
        self.assertFalse(sv.is_url("www.google.com"))
        self.assertFalse(sv.is_url("google.com"))
        self.assertFalse(sv.is_url("google"))
        self.assertFalse(sv.is_url("123"))
        self.assertFalse(sv.is_url(""))
        self.assertFalse(sv.is_url("http://"))

    def test_is_ip(self):
        """
        Test method to check if text is an ip string

        *Examples:*

        >>> is_ip('15.143.85.45') # returns true
        >>> is_ip('15.142.85.45:8080') # returns true

        """
        # Test valid ip
        self.assertTrue(sv.is_ip("15.143.85.45"))
        self.assertFalse(sv.is_ip("15.142.85.1:8080"))

    def test_is_hostname(self):
        """
        Test method to check if text is a hostname string

        *Examples:*

        >>> is_hostname('google') # returns true
        >>> is_hostname('www.google.com') # returns false
        >>> is_hostname('google.com') # returns false
        >>> is_hostname('www.google.com:8080') # returns false

        """
        # Test valid hostname
        self.assertTrue(sv.is_hostname("google"))
        self.assertTrue(sv.is_hostname("google-123"))

        # Test invalid hostname
        self.assertFalse(sv.is_hostname("www.google.com"))
        self.assertFalse(sv.is_hostname("google.com"))
        self.assertFalse(sv.is_hostname("www.google.com:8080"))

    def test_is_domain(self):
        """
        Test method to check if text is a domain string

        *Examples:*

        >>> is_domain('www.google.com') # returns true
        >>> is_domain('google.com') # returns true
        >>> is_domain('google') # returns false
        >>> is_domain('www.google.com:8080') # returns false

        """
        # Test valid domain
        self.assertTrue(sv.is_domain("www.google.com"))
        self.assertTrue(sv.is_domain("google.com"))

        # Test invalid domain
        self.assertFalse(sv.is_domain("google"))
        self.assertFalse(sv.is_domain("www.google.com:8080"))

    def test_is_email(self):
        """
        Test method to check if text is an email string

        *Examples:*

        >>> is_email('example@example.com') # returns true
        >>> is_email('exa.mple@example.com.es') # returns true
        >>> is_email('exa-mple@example.com.es') # returns true

        >>> is_email('example@example') # returns false
        >>> is_email('example') # returns false
        >>> is_email('example@') # returns false
        >>> is_email('@example.com') # returns false
        """
        # Test valid email
        self.assertTrue(sv.is_email("example@example.com"))
        self.assertTrue(sv.is_email("exa.mple@example.com.es"))
        self.assertTrue(sv.is_email("exa-mple@example.com.es"))

        self.assertFalse(sv.is_email("example@example"))
        self.assertFalse(sv.is_email("example"))
        self.assertFalse(sv.is_email("example@"))
        self.assertFalse(sv.is_email("@example.com"))

    def test_is_password(self):
        """
        Test method to check if text is a password string

        *Examples:*

        >>> is_password('123456') # returns true
        >>> is_password('<wq1234$·$89eTRe') # returns true
        >>> is_password('TkO2&4$%^=dHTY89&%') # returns true

        >>> is_password('1234567') # returns false
        >>> is_password('12345') # returns false
        >>> is_password('12345asdf') # returns false
        """
        # Test valid password
        self.assertTrue(sv.is_password("wq1234$$89eTRe"))
        self.assertTrue(sv.is_password("TkO2&4$%dHTY89&%"))
        self.assertTrue(sv.is_password("wq1234=!?$$89eTRe"))

        # Test invalid password
        self.assertFalse(sv.is_password("1234567"))
        self.assertFalse(sv.is_password("12345"))
        self.assertFalse(sv.is_password("12345asdf"))
        
    def test_is_json(self):
        """
        Test method to check if text is a json string

        *Examples:*

        >>> is_json('{"foo": "bar"}') # returns true
        >>> is_json('{"foo": "bar", "bar": "foo"}') # returns true
        >>> is_json('{"name": "Peter"}') # returns true
        >>> is_json('[1, 2, 3]') # returns true
        >>> is_json('{nope}') # returns false
        """
        # Test valid json
        self.assertTrue(sv.is_json('{"foo": "bar"}'))
        self.assertTrue(sv.is_json('{"foo": "bar", "bar": "foo"}'))
        self.assertTrue(sv.is_json('{"name": "Peter"}'))
        self.assertTrue(sv.is_json('[1, 2, 3]'))
        # Test invalid json
        self.assertFalse(sv.is_json('{nope}'))

    def test_is_xml(self):
        """
        Test method to check if text is an xml string

        *Examples:*

        >>> is_xml('<foo>bar</foo>') # returns true
        >>> is_xml('<foo>bar</foo><bar>foo</bar>') # returns true
        >>> is_xml('<foo>bar</foo><bar attr="asdf">foo</bar>') # returns true
        >>> is_xml('<foo>bar</bar>') # returns true
        """
        # Test valid xml
        self.assertTrue(sv.is_xml('<foo>bar</foo>'))
        self.assertTrue(sv.is_xml('<foo>bar</foo><bar>foo</bar>'))
        self.assertTrue(sv.is_xml('<foo>bar</foo><bar attr="asdf">foo</bar>'))
        self.assertTrue(sv.is_xml('<foo>bar</bar>'))

    # def test_is_html(self):
