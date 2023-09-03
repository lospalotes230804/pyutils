"""
This file contains functions for validate files.
"""

# Importing the required libraries
import os
import sys
import stat
import sqlite3
import src.utils.string.validate as stvl 

# Validations about existence / content

def exists(path: str) -> bool:
    """
    Method to check if the given file path points to an existing file.

    *Examples:*

    >>> exists('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file exists

    :param path: The path to the file.
    :type path: str
    :return: True if the file exists, False otherwise.
    """
    return stvl.is_path(path) and os.path.exists(path)

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

# Validations about properties

def is_hidden(path: str) -> bool:
    """
    Checks if the given file path points to a hidden file.

    *Examples:*

    >>> is_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is hidden

    :param path: The path to the file.
    :type path: str
    :return: True if the file is hidden, False otherwise.
    """
    # check if file is hidden for windows
    if sys.platform.startswith('win'):
        return (is_file(path) and
                bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN))
    # check if file is hidden for linux
    elif sys.platform.startswith('linux'):
        return (is_file(path) and
                os.path.basename(path).startswith('.'))

def is_visible(path: str) -> bool:
    """
    Checks if the given file path points to a visible file.

    *Examples:*

    >>> is_visible('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is visible

    :param path: The path to the file.
    :type path: str
    :return: True if the file is visible, False otherwise.
    """
    return is_file(path) and not is_hidden(path)

def is_readonly(path: str) -> bool:
    """
    Checks if the given file path points to a readonly file.
    Cross-platform function.

    *Examples:*

    >>> is_readonly('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is readonly

    :param path: The path to the file.
    :type path: str
    :return: True if the file is readonly, False otherwise.
    """
    # check if file is readonly for windows
    if sys.platform.startswith('win'):
        return (is_file(path) and
                bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_READONLY))
    # check if file is readonly for linux
    elif sys.platform.startswith('linux'):
        return (is_file(path) and
                not os.access(path, os.W_OK))

# def is_readable(path: str) -> bool:
    """
    Checks if the given file path points to a readable file.

    *Examples:*

    >>> is_readable('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is readable

    :param path: The path to the file.
    :type path: str
    :return: True if the file is readable, False otherwise.
    """
    return is_file(path) and os.access(path, os.R_OK)

# def is_writable(path: str) -> bool:
    """
    Checks if the given file path points to a writable file.

    *Examples:*

    >>> is_writable('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is writable

    :param path: The path to the file.
    :type path: str
    :return: True if the file is writable, False otherwise.
    """
    # return is_file(path) and os.access(path, os.W_OK)

# def is_executable(path: str) -> bool:
    """
    Checks if the given file path points to an executable file.

    *Examples:*

    >>> is_executable('C:\\Users\\User\\Desktop\\file.txt') # returns true if the file is executable

    :param path: The path to the file.
    :type path: str
    :return: True if the file is executable, False otherwise.
    """
    # return is_file(path) and os.access(path, os.W_OK)

    # if is_file(path):
    #     if sys.platform.startswith('linux'):  # Para Linux
    #         return os.access(path, os.X_OK)
    #     elif sys.platform.startswith('win'):  # Para Windows
    #         try:
    #             with open(path, 'rb') as file:
    #                 file.read(0)
    #             return True
    #         except PermissionError:
    #             return False

# Validations about content type

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
            and os.path.splitext(path) == '.json'
            and stvl.is_json(open(path, 'r+').read()))

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
            and os.path.splitext(path) == '.csv'
            and stvl.is_csv(open(path, 'r+').read()))

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
            and os.path.splitext(path) == '.xml'
            and stvl.is_xml(open(path, 'r+').read()))

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
            and os.path.splitext(path) == '.sqlite'
            and stvl.is_sqlite(open(path, 'r+').read())):
        try:
            conn = sqlite3.connect(path)
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"ERROR: loading SQLite DB file '{path}':\n{str(e)}")
            return False


