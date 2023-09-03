"""
This file contains functions for testing the utility functions at utils\string\
"""

# Importing the required libraries
import os
import sys
import shutil
from unittest import TestCase
import src.utils.string.validate as stvl
import src.utils.string.info as stin
import src.utils.string.process as stpr
import src.utils.datetime.validate as dtvl

class TestStringCase(TestCase):
    """
    Test class for testing string functions
    """

    # Basic string validations

    def test_is_string(self):
        """
        Method to test if the string is generic

        *Examples:*

        >>> is_string('foo') # returns true
        >>> is_string(b'foo') # returns false

        """
        self.assertTrue(stvl.is_string("This is a sample generic string for testing purposes"))
        self.assertFalse(stvl.is_string(123))
        self.assertFalse(stvl.is_string(b'foo'))

    def test_is_full_string(self):
        """
        Method to test if the string is full

        *Examples:*

        >>> is_full_string(None) # returns false
        >>> is_full_string('') # returns false
        >>> is_full_string(' ') # returns false
        >>> is_full_string('hello') # returns true
        """
        self.assertFalse(stvl.is_full_string(None))
        self.assertFalse(stvl.is_full_string(""))
        self.assertFalse(stvl.is_full_string(" "))
        self.assertTrue(stvl.is_full_string("hello"))

    def test_is_empty(self):
        """
        Method to test if the string is empty

        *Examples:*

        >>> is_empty(None) # returns false
        >>> is_empty('') # returns true
        >>> is_empty(' ') # returns true
        >>> is_empty('hello') # returns false
        """
        self.assertTrue(stvl.is_empty(""))
        self.assertFalse(stvl.is_empty(None))
        self.assertTrue(stvl.is_empty(" "))
        self.assertFalse(stvl.is_empty("hello"))

    def test_is_multiline(self):
        """
        Method to test if the string is multiline

        *Examples:*

        >>> is_multiline('hello') # returns false
        >>> is_multiline('hello\\nworld') # returns true
        >>> is_multiline('hello\\rworld') # returns true
        >>> is_multiline('hello\\r\\nworld') # returns true
        """
        self.assertFalse(stvl.is_multiline("hello"))
        self.assertTrue(stvl.is_multiline("hello\nworld"))
        self.assertTrue(stvl.is_multiline("hello\rworld"))
        self.assertTrue(stvl.is_multiline("hello\r\nworld"))

    def test_is_alpha(self):
        """
        Method to test if the string is alphabetic

        *Examples:*

        >>> is_alpha('hello') # returns true
        >>> is_alpha('hello123') # returns false
        >>> is_alpha('hello123!') # returns false
        """
        self.assertTrue(stvl.is_alpha("hello"))
        self.assertFalse(stvl.is_alpha("hello123"))
        self.assertFalse(stvl.is_alpha("hello123!"))

    def test_is_alphanumeric(self):
        """
        Method to test if the string is alphanumeric

        *Examples:*

        >>> is_alphanumeric('hello') # returns true
        >>> is_alphanumeric('hello123') # returns true
        >>> is_alphanumeric('hello123!') # returns false
        """
        self.assertTrue(stvl.is_alphanumeric("hello"))
        self.assertTrue(stvl.is_alphanumeric("hello123"))
        self.assertFalse(stvl.is_alphanumeric("hello123!"))

    # Validation of a string containing data types (int, float, bool, datetime, ...)

    def test_is_number(self):
        """
        Method to test if the string is a number

        *Examples:*

        >>> is_number('42') # returns true
        >>> is_number('19,99') # returns true
        >>> is_number('-9,12') # returns true
        >>> is_number('1e3') # returns true
        >>> is_number('1 2 3') # returns false
        """
        # Test valid number
        self.assertTrue(stvl.is_number("42"))
        self.assertTrue(stvl.is_number("19,99"))
        self.assertTrue(stvl.is_number("-9,12"))
        self.assertTrue(stvl.is_number("1e3"))

        # Test invalid number
        self.assertFalse(stvl.is_number("1 2 3"))

    def test_is_integer(self):
        """
        Method to test if the string is an integer
        DISCLAIMER: Localised to the Spanish format (decimal separator is comma)

        *Examples:*

        >>> is_integer('42') # returns true

        >>> is_integer('42.0') # returns false
        >>> is_integer('42,01') # returns false
        >>> is_integer('123.0') # returns false
        >>> is_integer('-9,12') # returns false
        >>> is_integer('1e3') # returns false
        >>> is_integer('123.456') # returns false
        """
        # Test valid integer
        self.assertTrue(stvl.is_integer("42"))

        # Test invalid integer
        self.assertFalse(stvl.is_integer("42.0"))
        self.assertFalse(stvl.is_integer("42,01"))
        self.assertFalse(stvl.is_integer("123.0"))
        self.assertFalse(stvl.is_integer("-9,12"))
        self.assertFalse(stvl.is_integer("1e3"))
        self.assertFalse(stvl.is_integer("123.456"))

    def test_is_decimal(self):
        """
        Method to test if the string is a decimal

        *Examples:*

        >>> is_integer('42,01') # returns true
        >>> is_integer('42') # returns false
        >>> is_integer('42.0') # returns false
        """
        # Test valid decimal
        self.assertTrue(stvl.is_decimal("42,01"))

        # Test invalid decimal
        self.assertFalse(stvl.is_decimal("42"))
        self.assertFalse(stvl.is_decimal("42.0"))

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
        self.assertTrue(dtvl.is_parseable("2018-01-01 12:00:00"))
        self.assertTrue(dtvl.is_parseable("25/01/2018 12:00"))
        self.assertTrue(dtvl.is_parseable("25/1/2018 12:30:00"))
        # Test invalid datetime
        self.assertFalse(dtvl.is_parseable("1/1/2018 12:99"))
        self.assertFalse(dtvl.is_parseable("25/1/2018 12:99"))
        self.assertFalse(dtvl.is_parseable("25/01/2018 12:00:99"))

    def test_is_bool(self):
        """
        Test method to check if text is a boolean string

        *Examples:*

        >>> is_bool('True') # returns true
        >>> is_bool('False') # returns true
        >>> is_bool('true') # returns true
        >>> is_bool('false') # returns true
        >>> is_bool('1') # returns true
        >>> is_bool('0') # returns true

        >>> is_bool('truefalse') # returns false
        >>> is_bool('123') # returns false
        >>> is_bool('abc') # returns false
        >>> is_bool('') # returns false
        """
        # Test valid boolean
        self.assertTrue(stvl.is_bool("True"))
        self.assertTrue(stvl.is_bool("False"))
        self.assertTrue(stvl.is_bool("true"))
        self.assertTrue(stvl.is_bool("false"))
        self.assertTrue(stvl.is_bool("1"))
        self.assertTrue(stvl.is_bool("0"))

        # Test invalid boolean
        self.assertFalse(stvl.is_bool("truefalse"))
        self.assertFalse(stvl.is_bool("123"))
        self.assertFalse(stvl.is_bool("abc"))
        self.assertFalse(stvl.is_bool(""))

    # Validation of a string containing specific strings (paths, filenames, urls, ...)

    def test_is_path(self):
        """
        Test method to check if text is a path string

        *Examples:*

        >>> is_path('C:/Users/User/Documents/file.txt') # returns true
        >>> is_path('c:\\Users\\User\\Documents\\file.txt') # returns true
        >>> is_path('\\Documents\\file.txt') # returns true
        >>> is_path('/Documents/file.txt') # returns true

        >>> is_path('file.txt') # returns false
        >>> is_path('file') # returns false
        >>> is_path('123') # returns false
        """
        # Test valid path
        self.assertTrue(stvl.is_path("C:/Users/User/Documents/file.txt"))
        self.assertTrue(stvl.is_path("c:\\Users\\User\\Documents\\file.txt"))
        self.assertTrue(stvl.is_path("\\Documents\\file.txt"))
        self.assertTrue(stvl.is_path("/Documents/file.txt"))

        # Test invalid path
        self.assertFalse(stvl.is_path("file.txt"))
        self.assertFalse(stvl.is_path("file"))
        self.assertFalse(stvl.is_path("123"))

    def test_is_filename(self):
        """
        Test method to check if text is a filename string

        *Examples:*

        >>> is_filename('file.txt') # returns true
        >>> is_filename('file sdf.txt') # returns true
        >>> is_filename('file-sdf (2).txt') # returns true

        >>> is_filename('file') # returns false
        >>> is_filename('file-sdf') # returns false
        >>> is_filename('C:/Users/User/Documents/file.txt') # returns false
        >>> is_filename('c:\\Users\\User\\Documents\\file.txt') # returns false
        >>> is_filename('\\Documents\\file.txt') # returns false
        >>> is_filename('/Documents/file.txt') # returns false
        """
        # Test valid filename
        self.assertTrue(stvl.is_filename("file.txt"))
        self.assertTrue(stvl.is_filename("file sdf.txt"))
        self.assertTrue(stvl.is_filename("file-sdf (2).txt"))
        self.assertTrue(stvl.is_filename("file-sdf (2).txt.gz"))

        # Test invalid filename
        self.assertFalse(stvl.is_filename("file"))
        self.assertFalse(stvl.is_filename("file-sdf"))
        self.assertFalse(stvl.is_filename("C:/Users/User/Documents/file.txt"))
        self.assertFalse(stvl.is_filename("c:\\Users\\User\\Documents\\file.txt"))
        self.assertFalse(stvl.is_filename("\\Documents\\file.txt"))
        self.assertFalse(stvl.is_filename("/Documents/file.txt"))

    def test_is_url(self):
        """
        Test method to check if text is a url string

        *Examples:*

        >>> is_url('http://www.google.com') # returns true
        >>> is_url('https://www.google.com/') # returns true
        >>> is_url('http://www.google.com/path/to/file') # returns true
        >>> is_url('https://www.google.com/path/to/file/') # returns true
        >>> is_url('http://www.google.com/path/to/file?param1=value1&param2=value2') # returns true
        >>> is_url('https://www.google.com/path/to/file/#anchor') # returns true
        >>> is_url('http://www.google.com/path/to/file?param1=value1&param2=value2#anchor') # returns true
        >>> is_url('ftp://15.142.85.1:8080') # returns true

        >>> is_url('15.142.85.1:8080') # returns false
        >>> is_url('www.google.com') # returns false
        >>> is_url('google.com') # returns false
        >>> is_url('google') # returns false
        >>> is_url('123') # returns false
        >>> is_url('') # returns false
        >>> is_url('http://') # returns false
        """
        # Test valid url
        self.assertTrue(stvl.is_url("http://www.google.com"))
        self.assertTrue(stvl.is_url("https://www.google.com/"))
        self.assertTrue(stvl.is_url("http://www.google.com/path/to/file"))
        self.assertTrue(stvl.is_url("https://www.google.com/path/to/file/"))
        self.assertTrue(stvl.is_url("http://www.google.com/path/to/file?param1=value1&param2=value2"))
        self.assertTrue(stvl.is_url("https://www.google.com/path/to/file/#anchor"))
        self.assertTrue(stvl.is_url("http://www.google.com/path/to/file?param1=value1&param2=value2#anchor"))
        self.assertTrue(stvl.is_url("ftp://15.142.85.1:8080"))

        # Test invalid url
        self.assertFalse(stvl.is_url("15.142.85.1:8080"))
        self.assertFalse(stvl.is_url("www.google.com"))
        self.assertFalse(stvl.is_url("google.com"))
        self.assertFalse(stvl.is_url("google"))
        self.assertFalse(stvl.is_url("123"))
        self.assertFalse(stvl.is_url(""))
        self.assertFalse(stvl.is_url("http://"))

    def test_is_ip(self):
        """
        Test method to check if text is an ip string

        *Examples:*

        >>> is_ip('15.143.85.45') # returns true
        >>> is_ip('15.142.85.45:8080') # returns true
        """
        # Test valid ip
        self.assertTrue(stvl.is_ip("15.143.85.45"))
        self.assertFalse(stvl.is_ip("15.142.85.1:8080"))

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
        self.assertTrue(stvl.is_hostname("google"))
        self.assertTrue(stvl.is_hostname("google-123"))

        # Test invalid hostname
        self.assertFalse(stvl.is_hostname("www.google.com"))
        self.assertFalse(stvl.is_hostname("google.com"))
        self.assertFalse(stvl.is_hostname("www.google.com:8080"))

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
        self.assertTrue(stvl.is_domain("www.google.com"))
        self.assertTrue(stvl.is_domain("google.com"))

        # Test invalid domain
        self.assertFalse(stvl.is_domain("google"))
        self.assertFalse(stvl.is_domain("www.google.com:8080"))

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
        self.assertTrue(stvl.is_email("example@example.com"))
        self.assertTrue(stvl.is_email("exa.mple@example.com.es"))
        self.assertTrue(stvl.is_email("exa-mple@example.com.es"))

        self.assertFalse(stvl.is_email("example@example"))
        self.assertFalse(stvl.is_email("example"))
        self.assertFalse(stvl.is_email("example@"))
        self.assertFalse(stvl.is_email("@example.com"))

    def test_is_password(self):
        """
        Test method to check if text is a password string

        *Examples:*

        >>> is_password('123456') # returns true
        >>> is_password('<wq1234$�$89eTRe') # returns true
        >>> is_password('TkO2&4$%^=dHTY89&%') # returns true

        >>> is_password('1234567') # returns false
        >>> is_password('12345') # returns false
        >>> is_password('12345asdf') # returns false
        """
        # Test valid password
        self.assertTrue(stvl.is_password("wq1234$$89eTRe"))
        self.assertTrue(stvl.is_password("TkO2&4$%dHTY89&%"))
        self.assertTrue(stvl.is_password("wq1234=!?$$89eTRe"))

        # Test invalid password
        self.assertFalse(stvl.is_password("1234567"))
        self.assertFalse(stvl.is_password("12345"))
        self.assertFalse(stvl.is_password("12345asdf"))

    # Validation of a string containing data structures (json, csv, xml, ...)

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
        self.assertTrue(stvl.is_json('{"foo": "bar"}'))
        self.assertTrue(stvl.is_json('{"foo": "bar", "bar": "foo"}'))
        self.assertTrue(stvl.is_json('{"name": "Peter"}'))
        self.assertTrue(stvl.is_json('[1, 2, 3]'))
        # Test invalid json
        self.assertFalse(stvl.is_json('{nope}'))

    def test_is_csv(self):
        """
        Test method to check if text is a csv string

        *Examples:*

        >>> is_csv('foo,bar') # returns true
        >>> is_csv('foo,bar,foo') # returns true
        >>> is_csv('foo;bar;foo;bar') # returns true
        >>> is_csv('foo;bar;foo;bar;foo') # returns true
        >>> is_csv('foo;bar;foo;bar;foo;bar') # returns true
        >>> is_csv('foo|bar|foo|bar|foo|bar|foo') # returns true
        """
        # Test valid csv
        self.assertTrue(stvl.is_csv('foo,bar'))
        self.assertTrue(stvl.is_csv('foo,bar,foo'))
        self.assertTrue(stvl.is_csv('foo;bar;foo;bar'))
        self.assertTrue(stvl.is_csv('foo;bar;foo;bar;foo'))
        self.assertTrue(stvl.is_csv('foo;bar;foo;bar;foo;bar'))
        self.assertTrue(stvl.is_csv('foo|bar|foo|bar|foo|bar|foo'))
        self.assertTrue(stvl.is_csv('foo|bar|foo|bar|foo|bar|foo|bar'))

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
        self.assertTrue(stvl.is_xml('<foo>bar</foo>'))
        self.assertTrue(stvl.is_xml('<foo>bar</foo><bar>foo</bar>'))
        self.assertTrue(stvl.is_xml('<foo>bar</foo><bar attr="asdf">foo</bar>'))
        self.assertTrue(stvl.is_xml('<foo>bar</bar>'))

    # Information about a string

    def test_get_length(self):
        """
        Test method to get the length of a string

        *Examples:*

        >>> get_length('foo') # returns 3
        >>> get_length('foo bar') # returns 7
        >>> get_length('foo bar foo') # returns 11
        """
        self.assertEqual(stin.get_length("foo"), 3)
        self.assertEqual(stin.get_length("foo bar"), 7)
        self.assertEqual(stin.get_length("foo bar foo"), 11)

    def test_get_chars(self):
        """
        Test method to get the characters of a string

        *Examples:*

        >>> get_chars('foo') # returns ['f', 'o', 'o']
        >>> get_chars('foo bar') # returns ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        >>> get_chars('foo bar foo') # returns ['f', 'o', 'o', ' ', 'b', 'a', 'r', ' ', 'f', 'o', 'o']
        """
        self.assertEqual(stin.get_chars("Hello World!"), ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!'])

    def test_get_words(self):
        """
        Test method to get the words of a string

        *Examples:*

        >>> get_words('foo bar') # returns ['foo', 'bar']
        >>> get_words('foo bar foo') # returns ['foo', 'bar', 'foo']
        """
        self.assertEqual(stin.get_words("foo bar"), ['foo', 'bar'])
        self.assertEqual(stin.get_words("foo bar foo"), ['foo', 'bar', 'foo'])

    def test_get_lines(self):
        """
        Test method to get the lines of a string

        *Examples:*

        >>> get_lines('foo\\nbar') # returns ['foo', 'bar']
        >>> get_lines('foo\\nbar\\nfoo') # returns ['foo', 'bar', 'foo']
        """
        self.assertEqual(stin.get_lines("foo\nbar"), ['foo', 'bar'])
        self.assertEqual(stin.get_lines("foo\nbar\nfoo"), ['foo', 'bar', 'foo'])

    def test_get_alphabetic(self):
        """
        Test method to get the alphabetic characters of a string

        *Examples:*

        >>> get_alphabetic('foo') # returns ['f', 'o', 'o']
        >>> get_alphabetic('foo bar') # returns ['f', 'o', 'o', 'b', 'a', 'r']
        >>> get_alphabetic('foo bar foo') # returns ['f', 'o', 'o', 'b', 'a', 'r', 'f', 'o', 'o']
        """
        self.assertEqual(stin.get_alphabetic("foo"), ['f', 'o', 'o'])
        self.assertEqual(stin.get_alphabetic("foo bar"), ['f', 'o', 'o', 'b', 'a', 'r'])
        self.assertEqual(stin.get_alphabetic("foo bar foo"), ['f', 'o', 'o', 'b', 'a', 'r', 'f', 'o', 'o'])

    def test_get_alphanumeric(self):
        """
        Test method to get the alphanumeric characters of a string

        *Examples:*

        >>> get_alphanumeric('foo') # returns ['f', 'o', 'o']
        >>> get_alphanumeric('foo bar') # returns ['f', 'o', 'o', 'b', 'a', 'r']
        >>> get_alphanumeric('foo bar 123') # returns ['f', 'o', 'o', 'b', 'a', 'r', '1', '2', '3']
        """
        self.assertEqual(stin.get_alphanumeric("foo"), ['f', 'o', 'o'])
        self.assertEqual(stin.get_alphanumeric("foo bar"), ['f', 'o', 'o', 'b', 'a', 'r'])
        self.assertEqual(stin.get_alphanumeric("foo bar 123"), ['f', 'o', 'o', 'b', 'a', 'r', '1', '2', '3'])

    # Processing a string

    def test_remove_non_ascii(self):
        """
        Test method to remove non-ascii characters from a string

        *Examples:*

        >>> remove_non_ascii('foo') # returns 'foo'
        >>> remove_non_ascii('foo 你好 bar') # returns 'foo  bar'
        >>> remove_non_ascii('foo bar 123') # returns 'foo bar 123'
        >>> remove_non_ascii('foo bar 123 �') # returns 'foo bar 123 '
        """
        self.assertEqual(stpr.remove_non_ascii("foo"), "foo")
        self.assertEqual(stpr.remove_non_ascii("foo 你好 bar"), "foo  bar")
        self.assertEqual(stpr.remove_non_ascii("foo bar 123"), "foo bar 123")
        self.assertEqual(stpr.remove_non_ascii("foo bar 123 �"), "foo bar 123 ")

    def test_remove_accents(self):
        """
        Test method to remove accents from a string

        *Examples:*

        >>> remove_accents('AéBíd') # returns 'AeBid'
        >>> remove_accents('AéBíd 你好') # returns 'AeBid 你好'
        >>> remove_accents('AéBíd 你好 123') # returns 'AeBid 你好 123'
        """
        self.assertEqual(stpr.remove_accents("AéBíd"), "AeBid")
        self.assertEqual(stpr.remove_accents("AéBíd 你好"), "AeBid 你好")
        self.assertEqual(stpr.remove_accents("AéBíd 你好 123"), "AeBid 你好 123")

    def test_capitalize(self):
        """
        Test method to capitalize a string

        *Examples:*

        >>> capitalize('foo') # returns 'Foo'
        >>> capitalize('foo bar') # returns 'Foo bar'
        >>> capitalize('foo bar 123') # returns 'Foo bar 123'
        """
        self.assertEqual(stpr.capitalize("foo"), "Foo")
        self.assertEqual(stpr.capitalize("foo bar"), "Foo bar")
        self.assertEqual(stpr.capitalize("foo bar 123"), "Foo bar 123")

    def test_capitalize_words(self):
        """
        Test method to capitalize words of a string

        *Examples:*

        >>> capitalize_words('foo') # returns 'Foo'
        >>> capitalize_words('foo bar') # returns 'Foo Bar'
        >>> capitalize_words('foo bar 123') # returns 'Foo Bar 123'
        """
        self.assertEqual(stpr.capitalize_words("foo"), "Foo")
        self.assertEqual(stpr.capitalize_words("foo bar"), "Foo Bar")
        self.assertEqual(stpr.capitalize_words("foo bar 123"), "Foo Bar 123")

    def test_escape(self):
        """
        Test method to escape a string

        *Examples:*

        >>> escape('https://www.python.org') # returns 'https://www\.python\.org'
        >>> escape('f[a-z]*') # returns 'f\[a\-z\]\*'
        """
        self.assertEqual(stpr.escape("https://www.python.org"), "https://www\.python\.org")
        self.assertEqual(stpr.escape("f[a-z]*"), "f\[a\-z\]\*")

    def test_unescape(self):
        """
        Test method to unescape a string

        *Examples:*

        >>> unescape('foo') # returns 'foo'
        >>> unescape('foo bar') # returns 'foo bar'
        >>> unescape('foo bar \\b' # returns 'foo bar \b'
        >>> unescape('foo \*bar\ 123 \a\p") # returns 'foo *bar 123 ap'
        """
        self.assertEqual(stpr.unescape("foo"), "foo")
        self.assertEqual(stpr.unescape("foo bar"), "foo bar")
        self.assertEqual(stpr.unescape("foo bar \\b"), "foo bar \b")
        self.assertEqual(stpr.unescape("foo \*bar\ 123 \-\p"), "foo *bar 123 -p")

    def test_remove_whitespace(self):
        """
        Test method to remove whitespace from a string

        *Examples:*

        >>> remove_whitespace('foo') # returns 'foo'
        >>> remove_whitespace('foo bar') # returns 'foobar'
        >>> remove_whitespace('foo bar 123')
        """
        self.assertEqual(stpr.remove_whitespace("foo"), "foo")
        self.assertEqual(stpr.remove_whitespace("foo bar"), "foobar")
        self.assertEqual(stpr.remove_whitespace("foo bar 123"), "foobar123")

    def test_remove_non_printable(self):
        """
        Test method to remove non-printable characters from a string

        *Examples:*

        >>> remove_non_printable('foo') # returns 'foo'
        >>> remove_non_printable('foo bar') # returns 'foo bar'
        >>> remove_non_printable('foo bar 123') # returns 'foo bar 123'
        >>> remove_non_printable('foo bar 123 \\x0C') # returns 'foo bar 123 '
        >>> remove_non_printable('foo bar 123 \\x0B') # returns 'foo bar 123 '
        """
        self.assertEqual(stpr.remove_non_printable("foo"), "foo")
        self.assertEqual(stpr.remove_non_printable("foo bar"), "foo bar")
        self.assertEqual(stpr.remove_non_printable("foo bar 123"), "foo bar 123")
        self.assertEqual(stpr.remove_non_printable("foo bar 123 \x0C"), "foo bar 123 ")
        self.assertEqual(stpr.remove_non_printable("foo bar 123 \x0B"), "foo bar 123 ")
