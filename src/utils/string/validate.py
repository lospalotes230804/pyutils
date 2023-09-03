"""
This file contains functions for validate strings.
"""

# Importing the required libraries
import json
import re
import dateutil.parser as dtp
from typing import Any, Optional, List
from .._regex import *
from ..errors import InvalidInputError

# Basic string validations

def is_string(obj: Any) -> bool:
    """
    Checks if the given string is a string.

    *Examples:*

    >>> is_string('foo') # returns true
    >>> is_string(b'foo') # returns false

    :param obj: Object to test.
    :return: True if string, false otherwise.
    """
    return isinstance(obj, str)

def is_full_string(input_string: str) -> bool:
    """
    Check if a string is not empty (it must contains at least one non space character).

    *Examples:*

    >>> is_full_string(None) # returns false
    >>> is_full_string('') # returns false
    >>> is_full_string(' ') # returns false
    >>> is_full_string('hello') # returns true

    :param input_string: String to check.
    :type input_string: str
    :return: True if not empty, false otherwise.
    """
    return is_string(input_string) and input_string.strip() != ''

def is_empty(input_string: str) -> bool:
    """
    Check if a string is empty (it must contains only spaces).

    *Examples:*

    >>> is_empty(None) # returns false
    >>> is_empty('') # returns true
    >>> is_empty(' ') # returns true
    >>> is_empty('hello') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if empty, false otherwise.
    """
    return is_string(input_string) and input_string.strip() == ''

def is_multiline(input_string: str) -> bool:
    """
    Check if a string is multiline.

    *Examples:*

    >>> is_multiline('hello') # returns false
    >>> is_multiline('hello\\nworld') # returns true
    >>> is_multiline('hello\\rworld') # returns true
    >>> is_multiline('hello\\r\\nworld') # returns true

    :param input_string: String to check.
    :type input_string: str
    :return: True if multiline, false otherwise.
    """
    return is_full_string(input_string) and re.search(r'[\r\n]', input_string)

def is_alpha(input_string: str) -> bool:
    """
    Check if a string is alphabetic.

    *Examples:*

    >>> is_alpha('hello') # returns true
    >>> is_alpha('hello123') # returns false
    >>> is_alpha('hello Camión') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if alphabetic, false otherwise.
    """
    return is_full_string(input_string) and input_string.isalpha()

def is_alphanumeric(input_string: str) -> bool:
    """
    Check if a string is alphanumeric.

    *Examples:*

    >>> is_alphanumeric('hello') # returns true
    >>> is_alphanumeric('hello123') # returns true
    >>> is_alphanumeric('hello 123') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if alphanumeric, false otherwise.
    """
    return is_full_string(input_string) and input_string.isalnum()

# Validation of strings containing data types (int, float, bool, datetime, ...)

def is_number(input_string: str) -> bool:
    """
    Checks if a string is a valid number.

    The number can be a signed (eg: +1, -2, -3.3)
    or unsigned (eg: 1, 2, 3.3) integer or double
    or use the "scientific notation" (eg: 1e5).

    *Examples:*

    >>> is_number('42') # returns true
    >>> is_number('19,99') # returns true
    >>> is_number('-9,12') # returns true
    >>> is_number('1e3') # returns true
    >>> is_number('1 2 3') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if the string represents a number, false otherwise
    """
    if not isinstance(input_string, str):
        raise InvalidInputError(input_string)

    return NUMBER_RE.match(input_string) is not None

def is_integer(input_string: str) -> bool:
    """
    Checks whether the given string represents an integer or not.
    An integer may be signed or unsigned or use a "scientific notation".
    DISCLAIMER: Localised to the Spanish format (decimal separator is comma)

    *Examples:*

    >>> is_integer('42') # returns true
    >>> is_integer('42.0') # returns true
    >>> is_integer('42,01') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if integer, false otherwise
    """
    # ',' and 'e' are not allowed
    return (is_number(input_string)
            and ',' not in input_string
            and 'e' not in input_string)

def is_decimal(input_string: str) -> bool:
    """
    Checks whether the given string represents a decimal or not.

    A decimal may be signed or unsigned or use a "scientific notation".

    *Examples:*

    >>> is_integer('42') # returns false
    >>> is_integer('42.0') # returns false
    >>> is_integer('42,01') # returns true

    :param input_string: String to check
    :type input_string: str
    :return: True if integer, false otherwise
    """
    return is_number(input_string) and ',' in input_string

def is_datetime(input_string: str, first) -> bool:
    """
    Checks whether the given string represents a datetime or not.

    *Examples:*
    
    >>> is_datetime('2018-01-01 12:00:00') # returns true
    >>> is_datetime('25/01/2018 12:00') # returns true
    >>> is_datetime('25/1/2018 12:30:00') # returns true

    >>> is_datetime('2018-01-01') # returns false
    >>> is_datetime('1/25/2018') # returns false
    >>> is_datetime('1/1/2018 12:99') # returns false
    >>> is_datetime('25/1/2018 12:99') # returns false
    >>> is_datetime('25/01/2018 12:00:99') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if datetime, false otherwise
    """
    return is_full_string(input_string) and dtp.is_parseable(input_string)

# def test_is_date(self):

# def test_is_time(self):

def is_bool(input_string: str) -> bool:
    """
    Checks whether the given string represents a boolean or not.

    *Examples:*

    >>> is_bool('true') # returns true
    >>> is_bool('false') # returns true
    >>> is_bool('True') # returns true
    >>> is_bool('False') # returns true
    >>> is_bool('yes') # returns true
    >>> is_bool('no') # returns true
    >>> is_bool('1') # returns true
    >>> is_bool('0') # returns true
    >>> is_bool('Si') # returns false
    >>> is_bool('sí') # returns false
    >>> is_bool('No') # returns false
    >>> is_bool('') # returns false
    >>> is_bool('foo') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if boolean, false otherwise
    """
    return (is_full_string(input_string) and input_string.lower() in
            ('true', 'false', 'yes', 'no', 'si', 'sí', 'no', '1', '0'))

# Validation of strings containing specific strings (paths, filenames, urls, ...)

def is_path(input_string: str) -> bool:
    """
    Checks whether the given string represents a path or not.

    *Examples:*

    >>> is_path('C:\\Users\\') # returns true
    >>> is_path('C:/Users/') # returns true
    >>> is_path('C:\\Users\\file.txt') # returns true
    >>> is_path('C:/Users/file.txt') # returns true

    :param input_string: String to check
    :type input_string: str
    :return: True if path, false otherwise
    """
    return (is_full_string(input_string)
            and PATH_RE.search(input_string) is not None)

def is_filename(input_string: str) -> bool:
    """
    Checks whether the given string represents a filename or not.

    *Examples:*

    >>> is_filename('file.txt') # returns true
    >>> is_filename('file.txt.bak') # returns true
    >>> is_filename('file') # returns true

    :param input_string: String to check
    :type input_string: str
    :return: True if filename, false otherwise
    """
    return is_full_string(input_string) and FILENAME_RE.match(input_string) is not None

def is_url(input_string: str) -> bool:
    """
    Checks whether the given string represents a URL or not.

    *Examples:*

    >>> is_url('https://www.google.com') # returns true
    >>> is_url('http://www.google.com') # returns true
    >>> is_url('www.google.com') # returns true
    >>> is_url('google.com') # returns true
    >>> is_url('google') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if URL, false otherwise
    """
    return is_full_string(input_string) and URL_RE.match(input_string) is not None

def is_ip(input_string: str) -> bool:
    """
    Checks whether the given string represents an IP address or not.

    *Examples:*

    >>> is_ip('192.168.15.1') # returns true

    :param input_string: String to check
    :type input_string: str
    :return: True if IP address, false otherwise
    """
    return is_full_string(input_string) and IP_V4_RE.match(input_string) is not None

def is_hostname(input_string: str) -> bool:
    """
    Checks whether the given string represents a hostname or not.

    *Examples:*

    >>> is_hostname('www.google.com') # returns true
    >>> is_hostname('google.com') # returns true
    >>> is_hostname('google') # returns true

    :param input_string: String to check
    :type input_string: str
    :return: True if hostname, false otherwise
    """
    return (is_full_string(input_string)
            and HOSTNAME_RE.match(input_string) is not None)

def is_domain(input_string: str) -> bool:
    """
    Checks whether the given string represents a domain or not.

    *Examples:*

    >>> is_domain('www.google.com') # returns true
    >>> is_domain('google.com') # returns true
    >>> is_domain('google') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if domain, false otherwise
    """
    return is_full_string(input_string) and DOMAIN_RE.match(input_string) is not None

def is_email(input_string: str) -> bool:
    """
    Checks whether the given string represents an email or not.

    *Examples:*

    >>> is_email('example@example.com') # returns true
    >>> is_email('exa.mple@example.com.es') # returns true
    >>> is_email('exa-mple@example.com.es') # returns true

    >>> is_email('example@example') # returns false
    >>> is_email('example') # returns false
    >>> is_email('example@') # returns false
    >>> is_email('@example.com') # returns false

    :param input_string: String to check
    :type input_string: str
    :return: True if email, false otherwise
    """
    return is_full_string(input_string) and EMAIL_RE.match(input_string) is not None

def is_password(input_string: str) -> bool:
    """
    Checks whether the given string represents a password or not.

    *Examples:*

    >>> is_password('123456') # returns true
    >>> is_password('<wq1234$·$89eTRe') # returns true
    >>> is_password('TkO2&4$%^=dHTY89&%') # returns true

    :param input_string: String to check
    :type input_string: str
    :return: True if password, false otherwise
    """
    return is_full_string(input_string) and PASSWORD_RE.match(input_string) is not None

# Validation of strings containing data structures (json, csv, xml, ...)

def is_json(input_string: str) -> bool:
    """
    Checks whether the given string represents a JSON or not.

    *Examples:*

    >>> is_json('{"foo": "bar"}') # returns true
    >>> is_json('{"foo": "bar", "bar": "foo"}') # returns true
    >>> is_json('{"name": "Peter"}') # returns true
    >>> is_json('[1, 2, 3]') # returns true
    >>> is_json('{nope}') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if json, false otherwise
    """
    if is_full_string(input_string) and JSON_RE.match(input_string) is not None:
        try:
            return isinstance(json.loads(input_string), (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass

    return False

def is_csv(input_string: str) -> bool:
    """
    Checks whether the given string represents a CSV or not.

    *Examples:*

    >>> is_csv('foo,bar') # returns true
    >>> is_csv('foo,bar,foo') # returns true
    >>> is_csv('foo;bar;foo;bar') # returns true
    >>> is_csv('foo;bar;foo;bar;foo') # returns true
    >>> is_csv('foo;bar;foo;bar;foo;bar') # returns true
    >>> is_csv('foo|bar|foo|bar|foo|bar|foo') # returns true

    :param input_string: String to check.
    :type input_string: str
    :return: True if csv, false otherwise
    """
    return is_full_string(input_string) and CSV_RE.match(input_string) is not None

def is_xml(input_string: str) -> bool:
    """
    Checks whether the given string represents an XML or not.

    *Examples:*

    >>> is_xml('<foo>bar</foo>') # returns true
    >>> is_xml('<foo>bar</foo><bar>foo</bar>') # returns true
    >>> is_xml('<foo>bar</foo><bar attr="asdf">foo</bar>') # returns true
    >>> is_xml('<foo>bar</bar>') # returns true

    :param input_string: String to check.
    :type input_string: str
    :return: True if xml, false otherwise
    """
    return is_full_string(input_string) and XML_RE.match(input_string) is not None


