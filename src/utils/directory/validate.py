"""
This file contains functions for validate directories.
"""

# Importing the required libraries
import os
import sys
from src.utils.string.validate import is_path as str_is_path
from .._regex import *

# Validations about existence / content

def exists(path: str) -> bool:
    """
    Method to check if the given directory path points to an existing directory

    *Examples:*

    >>> exists('C:\\Users\\User\\Desktop\\') # returns true if the directory exists

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory exists, False otherwise.
    """
    return str_is_path(path) and os.path.exists(path)

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

# Validations about properties

def is_hidden(path: str) -> bool:
    """
    Method to check if the given directory path points to a hidden directory

    *Examples:*

    >>> is_hidden('C:\\Users\\User\\Desktop\\') # returns true if the directory is hidden

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is hidden, False otherwise.
    """
    # check if directory is hidden for windows
    if sys.platform.startswith('win'):
        try:
            attrs = os.stat(path).st_file_attributes
            assert attrs != -1
            result = bool(attrs & 2)
        except (AttributeError, AssertionError):
            result = False
        return result
    # check if directory is hidden for linux
    elif sys.platform.startswith('linux'):
        return os.path.basename(path).startswith('.')

def is_visible(path: str) -> bool:
    """
    Method to check if the given directory path points to a visible directory

    *Examples:*

    >>> is_visible('C:\\Users\\User\\Desktop\\') # returns true if the directory is visible

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is visible, False otherwise.
    """
    return is_dir(path) and not is_hidden(path)

# def is_readonly(path: str) -> bool:
    """
    Method to check if the given directory path points to a readonly directory

    In Windows, when a directory (folder) is flagged as read-only, it has several implications and behaviors:

    - Files within the Read-Only Directory: By default, files within a read-only directory inherit the read-only attribute from the directory. This means that any new files created within the directory will also be marked as read-only.
    - File Modifications: If a file within a read-only directory is marked as read-only, it can typically still be read, but you cannot modify it or save changes to it unless you remove the read-only attribute from the file itself. To edit a read-only file, you often need to copy it to a different location, make the changes, and then save it.
    - Creating and Deleting Files: You can create new files within a read-only directory, but those files will also be marked as read-only by default. You can delete files from a read-only directory, provided you have the necessary permissions, but you may not be able to modify or replace them without changing the read-only attribute.
    - Directory Attributes: The read-only attribute on a directory can affect the behavior of some applications and scripts. Some software may check for this attribute when deciding whether to allow modifications within the directory.
    - Special Handling: Some backup and synchronization tools may treat read-only directories differently. For example, they might skip read-only directories during synchronization unless explicitly configured otherwise.
    - Security: The read-only attribute itself is not a robust security measure. It is a simple attribute that can be changed by users with appropriate permissions. It is not a substitute for proper access control and permissions management.
    - Compatibility: In some cases, having a read-only directory can affect the behavior of older or legacy software that doesn't handle read-only attributes gracefully.

    *Examples:*

    >>> is_readonly('C:\\Users\\User\\Desktop\\') # returns true if the directory is readonly

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is readonly, False otherwise.
    """
    # check if directory is readonly for windows
    # if sys.platform.startswith('win'):
    #     try:
    #         attrs = os.stat(path).st_file_attributes
    #         assert attrs != -1
    #         result = bool(attrs & 1)
    #     except (AttributeError, AssertionError):
    #         result = False
    #     return result
    # # check if directory is readonly for linux
    # elif sys.platform.startswith('linux'):
    #     return os.access(path, os.W_OK)

# def is_readable(path: str) -> bool:
    """
    Method to check if the given directory path points to a readable directory

    *Examples:*

    >>> is_readable('C:\\Users\\User\\Desktop\\') # returns true if the directory is readable

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is readable, False otherwise.
    """
    # return is_dir(path) and os.access(path, os.R_OK)

# def is_writable(path: str) -> bool:
    """
    Method to check if the given directory path points to a writable directory

    *Examples:*

    >>> is_writable('C:\\Users\\User\\Desktop\\') # returns true if the directory is writable

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is writable, False otherwise.
    """
    # return is_dir(path) and os.access(path, os.W_OK)

# def is_executable(path: str) -> bool:
    """
    Method to check if the given directory path points to a directory with executable permissions

    *Examples:*

    >>> is_executable('C:\\Users\\User\\Desktop\\') # returns true if the directory has executable permissions

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory has executable permissions, False otherwise.
    """
    # if is_dir(path):
    #     if sys.platform.startswith('linux'):  # Para Linux
    #         return os.access(path, os.X_OK)
    #     elif sys.platform.startswith('win'):  # Para Windows
    #         try:
    #             os.listdir(path)
    #             return True
    #         except PermissionError:
    #             return False

    # name = os.path.basename(os.path.abspath(filepath))
    # return name.startswith('.') or has_hidden_attribute(filepath)

    # if sys.platform.startswith('win'):
    #     return bool(os.stat(path).st_file_attributes
    #                 & win32com.FILE_ATTRIBUTE_HIDDEN)
    # else:
    #     return is_dir(path) and bool(HIDDEN_FILENAME_RE, os.path.basename(path))

# def is_writable(path: str) -> bool:
    """
    Method to check if the given directory path points to a directory with the user has writable permissions

    *Examples:*

    >>> is_writable('C:\\Users\\User\\Desktop\\') # returns true if the directory has writable permissions

    :param path: The path to the directory.
    :type path: str
    :return: True if the user has writable permissions on the directory, False otherwise.
    """
    # check if directory is writable for windows
    # if sys.platform.startswith('win'):
    #     try:
    #         attrs = os.stat(path).st_file_attributes
    #         assert attrs != -1
    #         result = bool(attrs & 1)
    #     except (AttributeError, AssertionError):
    #         result = False
    #     return result
    # # check if directory is writable for linux
    # elif sys.platform.startswith('linux'):
    #     return os.access(path, os.W_OK)



