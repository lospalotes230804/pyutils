"""
This file contains functions for validate files.
"""

# Importing the required libraries
import os
import sqlite3
import stat
import sys
import json
import utils.string.validate as str
import utils.string.process as str
from utils.file.process import read
from utils.file.info import get_extension
from typing import Any, Optional, List
from .._regex import *
from ..errors import InvalidInputError
# if Unix, import pwd module
if sys.platform.startswith('linux'):
    import pwd
    import grp

# Simple validations => basic name & path operations

def exists(path: str) -> bool:
    """
    Method to check if the given file path points to an existing file.

    *Examples:*

    >>> exists('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file exists

    :param path: The path to the file.
    :type path: str
    :return: True if the file exists, False otherwise.
    """
    return str.is_path(path) and os.path.exists(path)

def is_file(path: str) -> bool:
    """
    Checks if the given file path points to an existing file.

    *Examples:*

    >>> is_file('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file exists

    :param path: The path to the file.
    :type path: str
    :return: True if the file exists, False otherwise.
    """
    return exists(path) and os.path.isfile(path)

def is_empty(path: str) -> bool:
    """
    Checks if the given file path points to an empty file.

    *Examples:*

    >>> is_empty('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is empty

    :param path: The path to the file.
    :type path: str
    :return: True if the file is empty, False otherwise.
    """
    return is_file(path) and os.path.getsize(path) == 0

def is_readable(path: str) -> bool:
    """
    Checks if the given file path points to a readable file.

    *Examples:*

    >>> is_readable('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is readable

    :param path: The path to the file.
    :type path: str
    :return: True if the file is readable, False otherwise.
    """
    return is_file(path) and os.access(path, os.R_OK)

def is_writable(path: str) -> bool:
    """
    Checks if the given file path points to a writable file.

    *Examples:*

    >>> is_writable('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is writable

    :param path: The path to the file.
    :type path: str
    :return: True if the file is writable, False otherwise.
    """
    return is_file(path) and os.access(path, os.W_OK)

def is_executable(path: str) -> bool:
    """
    Checks if the given file path points to an executable file.

    *Examples:*

    >>> is_executable('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is executable

    :param path: The path to the file.
    :type path: str
    :return: True if the file is executable, False otherwise.
    """
    return is_file(path) and os.access(path, os.X_OK)

def is_hidden(path: str) -> bool:
    """
    Checks if the given file path points to a hidden file.

    *Examples:*

    >>> is_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is hidden

    :param path: The path to the file.
    :type path: str
    :return: True if the file is hidden, False otherwise.
    """
    if sys.platform.startswith('win'):
        return (is_file(path) and
                bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN))
    elif sys.platform.startswith('linux'):
        # check if file is hidden in linux
        return (is_file(path) and
                os.path.basename(path).startswith('.'))

def is_json(path: str) -> bool:
    """
    Checks if the given file path points to a json file.

    *Examples:*

    >>> is_json('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is a json file

    :param path: The path to the file.
    :type path: str
    :return: True if the file is a json file, False otherwise.
    """
    return (is_file(path)
            and get_extension(path) == '.json'
            and str.is_json(read(path)))

def is_csv(path: str) -> bool:
    """
    Checks if the given file path points to a csv file.

    *Examples:*

    >>> is_csv('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is a csv file

    :param path: The path to the file.
    :type path: str
    :return: True if the file is a csv file, False otherwise.
    """
    return (is_file(path)
            and get_extension(path) == '.csv'
            and str.is_csv(read(path)))

def is_xml(path: str) -> bool:
    """
    Checks if the given file path points to a xml file.

    *Examples:*

    >>> is_xml('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is a xml file

    :param path: The path to the file.
    :type path: str
    :return: True if the file is a xml file, False otherwise.
    """
    return (is_file(path)
            and get_extension(path) == '.xml'
            and str.is_xml(read(path)))

def is_sqlite(path: str) -> bool:
    """
    Checks if the given file path points to a sqlite file.

    *Examples:*

    >>> is_sqlite('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is a sqlite file

    :param path: The path to the file.
    :type path: str
    :return: True if the file is a sqlite file, False otherwise.
    """
    if (is_file(path)
            and get_extension(path) == '.sqlite'
            and str.is_sqlite(read(path))):
        try:
            conn = sqlite3.connect(path)
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"ERROR: loading SQLite DB file '{path}':\n{str(e)}")
            return False

# # def is_image(path: str) -> bool:
