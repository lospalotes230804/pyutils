"""
This file contains functions for obtaining information about strings.
"""

# Importing the required libraries
import re
from .validate import is_string

# Get information about a string

def get_length(string: str) -> int:
    """
    Gets the length of a string.

    *Examples:*

    >>> get_length('foo') # returns 3
    >>> get_length('foo bar') # returns 7
    >>> get_length('foo bar foo') # returns 11

    :param string: The string.
    :type string: str
    :return: The length of the string.
    """
    if is_string(string):
        return len(string)
    
def get_chars(string: str) -> list:
    """
    Gets the characters of a string.

    *Examples:*

    >>> get_chars('foo') # returns ['f', 'o', 'o']
    >>> get_chars('foo bar') # returns ['f', 'o', 'o', ' ', 'b', 'a', 'r']
    >>> get_chars('foo bar foo') # returns ['f', 'o', 'o', ' ', 'b', 'a', 'r', ' ', 'f', 'o', 'o']

    :param string: The string.
    :type string: str
    :return: The characters of the string.
    """
    if is_string(string):
        return list(string)
    
def get_words(string: str) -> list:
    """
    Gets the words of a string.

    *Examples:*

    >>> get_words('foo bar') # returns ['foo', 'bar']
    >>> get_words('foo bar foo') # returns ['foo', 'bar', 'foo']

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

    >>> get_lines('foo\\nbar') # returns ['foo', 'bar']
    >>> get_lines('foo\\nbar\\nfoo') # returns ['foo', 'bar', 'foo']

    :param string: The string.
    :type string: str
    :return: The lines of the string.
    """
    if is_string(string):
        return string.splitlines()
    
def get_alphabetic(string: str) -> str:
    """
    Gets the alphabetic characters of a string.

    *Examples:*

    >>> get_alphabetic_chars('foo') # returns ['f', 'o', 'o']
    >>> get_alphabetic_chars('foo bar') # returns ['f', 'o', 'o', 'b', 'a', 'r']
    >>> get_alphabetic_chars('foo bar foo') # returns ['f', 'o', 'o', 'b', 'a', 'r', 'f', 'o', 'o']
        
    :param string: The string.
    :type string: str
    :return: The alphabetic characters of the string.
    """
    if is_string(string):
        return list(re.sub(r'[^a-zA-Z]', '', string))
    
def get_alphanumeric(string: str) -> str:
    """
    Gets the alphanumeric characters of a string.

    *Examples:*

    >>> get_alphanumeric_chars('foo') # returns ['f', 'o', 'o']
    >>> get_alphanumeric_chars('foo bar') # returns ['f', 'o', 'o', 'b', 'a', 'r']
    >>> get_alphanumeric_chars('foo bar 123') # returns ['f', 'o', 'o', 'b', 'a', 'r', '1', '2', '3']

    :param string: The string.
    :type string: str
    :return: The alphanumeric characters of the string.
    """
    if is_string(string):
        return list(re.sub(r'[^a-zA-Z0-9]', '', string))

