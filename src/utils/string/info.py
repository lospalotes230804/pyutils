"""
This file contains functions for obtaining information about strings.
"""

# Importing the required libraries
import re
from utils.string.validate import is_string

# Get information about a string

def get_length(string: str) -> int:
    """
    Gets the length of a string.

    *Examples:*

    >>> get_length('Hello World!') # returns 12

    :param string: The string.
    :type string: str
    :return: The length of the string.
    """
    if is_string(string):
        return len(string)
    
def get_words(string: str) -> list:
    """
    Gets the words of a string.

    *Examples:*

    >>> get_words('Hello World!') # returns ['Hello', 'World']

    :param string: The string.
    :type string: str
    :return: The words of the string.
    """
    if is_string(string):
        return re.findall(r'\w+', string)
    
def get_lines(string: str) -> list:
    """
    Gets the lines of a string.

    *Examples:*

    >>> get_lines('Hello World!') # returns ['Hello World!']

    :param string: The string.
    :type string: str
    :return: The lines of the string.
    """
    if is_string(string):
        return string.splitlines()
    
def get_chars(string: str) -> list:
    """
    Gets the characters of a string.

    *Examples:*

    >>> get_characters('Hello World!') # returns ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

    :param string: The string.
    :type string: str
    :return: The characters of the string.
    """
    if is_string(string):
        return list(string)
    
def get_alphabetic_chars(string: str) -> str:
    """
    Gets the alphabetic characters of a string.

    *Examples:*

    >>> get_alphabetic('Hello World!') # returns 'HelloWorld'

    :param string: The string.
    :type string: str
    :return: The alphabetic characters of the string.
    """
    if is_string(string):
        return re.sub(r'[^a-zA-Z]', '', string)
    
def get_alphanumeric_chars(string: str) -> str:
    """
    Gets the alphanumeric characters of a string.

    *Examples:*

    >>> get_alphanumeric('Hello World!') # returns 'HelloWorld'

    :param string: The string.
    :type string: str
    :return: The alphanumeric characters of the string.
    """
    if is_string(string):
        return re.sub(r'[^a-zA-Z0-9]', '', string)

