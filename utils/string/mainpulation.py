"""
This file contains functions for text manipulation.
Inspired in
https://github.com/daveoncode/python-string-utils/blob/master/string_utils/validation.py
"""

# Importing the required libraries
import os
import sys
import json
import re

from .._regex import *
from ..errors import InvalidInputError

# Adding project path to the sys.path
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.string.validation import is_string


class __StringFormatter:
    """
    Class to format a string by applying the following basic grammar and formatting rules:

    - String cannot start or end with spaces
    - The first letter in the string and the ones after a dot, an exclamation or a question mark must be uppercase
    - String cannot have multiple sequential spaces, empty lines or punctuation (except for "?", "!" and ".")
    - Arithmetic operators (+, -, /, \\*, =) must have one, and only one space before and after themselves
    - One, and only one space should follow a dot, a comma, an exclamation or a question mark
    - Text inside double quotes cannot start or end with spaces, but one, and only one space must come first and \
    after quotes (foo" bar"baz -> foo "bar" baz)
    - Text inside round brackets cannot start or end with spaces, but one, and only one space must come first and \
    after brackets ("foo(bar )baz" -> "foo (bar) baz")
    - Percentage sign ("%") cannot be preceded by a space if there is a number before ("100 %" -> "100%")
    - Saxon genitive is correct ("Dave' s dog" -> "Dave's dog")

    *Examples:*

    >>> __StringFormatter(' unprettified string ,, like this one,will be"prettified" .it\\' s awesome! ').format()
    >>> # -> 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    
    """

    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        self.input_string = input_string

    def __uppercase_first_char(self, regex_match):
        return regex_match.group(0).upper()

    def __remove_duplicates(self, regex_match):
        return regex_match.group(1)[0]

    def __uppercase_first_letter_after_sign(self, regex_match):
        match = regex_match.group(1)
        return match[:-1] + match[2].upper()

    def __ensure_right_space_only(self, regex_match):
        return regex_match.group(1).strip() + ' '

    def __ensure_left_space_only(self, regex_match):
        return ' ' + regex_match.group(1).strip()

    def __ensure_spaces_around(self, regex_match):
        return ' ' + regex_match.group(1).strip() + ' '

    def __remove_internal_spaces(self, regex_match):
        return regex_match.group(1).strip()

    def __fix_saxon_genitive(self, regex_match):
        return regex_match.group(1).replace(' ', '') + ' '

    # generates a placeholder to inject temporary into the string, it will be replaced with the original
    # value at the end of the process
    @staticmethod
    def __placeholder_key():
        return '$' + uuid4().hex + '$'

    def format(self) -> str:
        # map of temporary placeholders
        placeholders = {}
        out = self.input_string

        # looks for url or email and updates placeholders map with found values
        placeholders.update({self.__placeholder_key(): m[0] for m in URLS_RE.findall(out)})
        placeholders.update({self.__placeholder_key(): m for m in EMAILS_RE.findall(out)})

        # replace original value with the placeholder key
        for p in placeholders:
            out = out.replace(placeholders[p], p, 1)

        out = PRETTIFY_RE['UPPERCASE_FIRST_LETTER'].sub(self.__uppercase_first_char, out)
        out = PRETTIFY_RE['DUPLICATES'].sub(self.__remove_duplicates, out)
        out = PRETTIFY_RE['RIGHT_SPACE'].sub(self.__ensure_right_space_only, out)
        out = PRETTIFY_RE['LEFT_SPACE'].sub(self.__ensure_left_space_only, out)
        out = PRETTIFY_RE['SPACES_AROUND'].sub(self.__ensure_spaces_around, out)
        out = PRETTIFY_RE['SPACES_INSIDE'].sub(self.__remove_internal_spaces, out)
        out = PRETTIFY_RE['UPPERCASE_AFTER_SIGN'].sub(self.__uppercase_first_letter_after_sign, out)
        out = PRETTIFY_RE['SAXON_GENITIVE'].sub(self.__fix_saxon_genitive, out)
        out = out.strip()

        # restore placeholder keys with their associated original value
        for p in placeholders:
            out = out.replace(p, placeholders[p], 1)

        return out
    
# Simple manipulations => basic string operations

def remove_accents(input_string: str) -> str:
    """
    Removes accents from a string.
    """
    return unidecode.unidecode(input_string)

def remove_non_ascii(input_string: str) -> str:
    """
    Removes non-ascii characters from a string.
    """
    return "".join(i for i in input_string if ord(i) < 128)

# String manipulations => formatting

def capitalize(input_string: str) -> str:
    """
    Capitalizes a string.
    """
    return input_string.capitalize()

def capitalize_words(input_string: str) -> str:
    """
    Capitalizes all words in a string.
    """
    return " ".join([capitalize(word) for word in input_string.split(" ")])

def escape(input_string: str) -> str:
    """
    Escapes a string.
    """
    return re.escape(input_string)

def unescape(input_string: str) -> str:
    """
    Unescapes a string.
    """
    return bytes(input_string, "utf-8").decode("unicode_escape")

def remove_whitespace(input_string: str) -> str:
    """
    Removes all whitespace from a string.
    """
    return "".join(input_string.split())

def remove_zero_width(input_string: str) -> str:
    """
    Removes all zero width characters from a string.
    """
    return "".join([char for char in input_string if ord(char) > 32])

def remove_invisible(input_string: str) -> str:
    """
    Removes all invisible characters from a string.
    """
    return "".join([char for char in input_string if ord(char) > 32])


# String manipulations => JSON

def json_wrapper(input_string: str) -> str:
    """
    Wraps a string with square brackets or curly braces if it is not already wrapped.
    """
    if JSON_WRAPPER_RE.match(input_string):
        return input_string
    else:
        return "[{}]".format(input_string)
    
def json_unwrapper(input_string: str) -> str:
    """
    Unwraps a string from square brackets or curly braces if it is wrapped.
    """
    return JSON_WRAPPER_RE.match(input_string).group(1)

def json_to_dict(input_string: str) -> dict:
    """
    Converts a JSON string to a dictionary.
    """
    return json.loads(json_unwrapper(input_string))

def json_to_list(input_string: str) -> list:
    """
    Converts a JSON string to a list.
    """
    return json.loads(json_unwrapper(input_string))

# String manipulations => HTML

def html_tag_only(input_string: str) -> str:
    """
    Removes all text from a string, leaving only HTML tags.
    """
    return HTML_TAG_ONLY_RE.sub("", input_string)

def html_to_text(input_string: str) -> str:
    """
    Converts HTML to plain text.
    """
    return html2text.html2text(input_string)

def strip_html(input_string: str, keep_tag_content: bool = False) -> str:
    """
    Remove html code contained into the given string.

    *Examples:*

    >>> strip_html('test: <a href="foo/bar">click here</a>') # returns 'test: '
    >>> strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) # returns 'test: click here'

    :param input_string: String to manipulate.
    :type input_string: str
    :param keep_tag_content: True to preserve tag content, False to remove tag and its content too (default).
    :type keep_tag_content: bool
    :return: String with html removed.
    """
    if not sv.is_string(input_string):
        raise InvalidInputError(input_string)

    r = HTML_TAG_ONLY_RE if keep_tag_content else HTML_RE

    return r.sub('', input_string)

# String manipulations => prettify

def prettify(input_string: str) -> str:
    """
    Reformat a string by applying the following basic grammar and formatting rules:

    - String cannot start or end with spaces
    - The first letter in the string and the ones after a dot, an exclamation or a question mark must be uppercase
    - String cannot have multiple sequential spaces, empty lines or punctuation (except for "?", "!" and ".")
    - Arithmetic operators (+, -, /, \\*, =) must have one, and only one space before and after themselves
    - One, and only one space should follow a dot, a comma, an exclamation or a question mark
    - Text inside double quotes cannot start or end with spaces, but one, and only one space must come first and \
    after quotes (foo" bar"baz -> foo "bar" baz)
    - Text inside round brackets cannot start or end with spaces, but one, and only one space must come first and \
    after brackets ("foo(bar )baz" -> "foo (bar) baz")
    - Percentage sign ("%") cannot be preceded by a space if there is a number before ("100 %" -> "100%")
    - Saxon genitive is correct ("Dave' s dog" -> "Dave's dog")

    *Examples:*

    >>> prettify(' unprettified string ,, like this one,will be"prettified" .it\\' s awesome! ')
    >>> # -> 'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    :param input_string: String to manipulate
    :return: Prettified string.
    """
    formatted = __StringFormatter(input_string).format()
    return formatted
