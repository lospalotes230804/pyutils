"""
This file contains functions for validate directories.
"""

# Importing the required libraries
import os
import sys
import string.validate as str
import string.process as str
from .._regex import *

def exists(path: str) -> bool:
    """
    Method to check if the given directory path points to an existing directory

    *Examples:*

    >>> exists('C:\\Users\\User\\Desktop\\') # returns true if the directory exists

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory exists, False otherwise.
    """
    return str.is_path(path) and os.path.exists(path)

def is_dir(path) -> str:
    """
    Method to check if directory exists

    *Examples:*

    >>> is_dir('C:\\Users\\User\\Desktop\\') # returns true if the directory exists

    :return: 
    :rtype: bool
    """
    return exists(path) and os.path.isdir(path)

def is_empty(path: str) -> bool:
    """
    Method to check if the given directory path points to an empty directory

    *Examples:*

    >>> is_empty('C:\\Users\\User\\Desktop\\') # returns true if the directory is empty

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is empty, False otherwise.
    """
    return is_dir(path) and len(os.listdir(path)) == 0

def is_readable(path: str) -> bool:
    """
    Method to check if the given directory path points to a readable directory

    *Examples:*

    >>> is_readable('C:\\Users\\User\\Desktop\\') # returns true if the directory is readable

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is readable, False otherwise.
    """
    return is_dir(path) and os.access(path, os.R_OK)

def is_writable(path: str) -> bool:
    """
    Method to check if the given directory path points to a writable directory

    *Examples:*

    >>> is_writable('C:\\Users\\User\\Desktop\\') # returns true if the directory is writable

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is writable, False otherwise.
    """
    return is_dir(path) and os.access(path, os.W_OK)

def is_executable(path: str) -> bool:
    """
    Method to check if the given directory path points to an executable directory

    *Examples:*

    >>> is_executable('C:\\Users\\User\\Desktop\\') # returns true if the directory is executable

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is executable, False otherwise.
    """
    return is_dir(path) and os.access(path, os.X_OK)

def is_hidden(path: str) -> bool:
    """
    Method to check if the given directory path points to a hidden directory

    *Examples:*

    >>> is_hidden('C:\\Users\\User\\Desktop\\') # returns true if the directory is hidden

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is hidden, False otherwise.
    """
    if sys.platform.startswith('win'):
        return bool(os.stat(path).st_file_attributes & os.stat.FILE_ATTRIBUTE_HIDDEN)
    else:
        return is_dir(path) and bool(HIDDEN_FILENAME_RE, os.path.basename(path))

