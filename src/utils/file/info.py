"""
This file contains functions for file manipulation.
"""

# Importing the required libraries
import os
import sys
import chardet
import datetime as dt
from src.utils.file.validate import is_file

# Get information about a file

def get_size(path: str) -> int:
    """
    Gets the size of a file in bytes.

    *Examples:*

    >>> get_size('C:\\Users\\User\\Desktop\\file.txt') # returns 1024

    :param path: The path to the file.
    :type path: str
    :return: The size of the file in bytes.
    :rtype: int
    """
    if is_file(path):
        return os.path.getsize(path)

def get_filename(path: str) -> str:
    """
    Gets the name of a file.

    *Examples:*

    >>> get_name('C:\\Users\\User\\Desktop\\file.txt') # returns 'file.txt'

    :param path: The path to the file.
    :type path: str
    :return: The name of the file.
    :rtype: str
    """
    return os.path.basename(path)

def get_filename_w_ext(path: str) -> str:
    """
    Gets the name of a file without the extension.

    *Examples:*

    >>> get_name('C:\\Users\\User\\Desktop\\file.txt') # returns 'file'

    :param path: The path to the file.
    :type path: str
    :return: The name of the file without the extension.
    """
    return os.path.splitext(os.path.basename(path))[0]

def get_relative_path(path: str) -> str:
    """
    Gets the relative path of a file.

    *Examples:*

    >>> get_relative_path('C:\\Users\\User\\Desktop\\file.txt') # returns 'file.txt'

    :param path: The path to the file.
    :type path: str
    :return: The relative path of the file.
    :rtype: str
    """
    return os.path.relpath(path)

def get_absolute_path(path: str) -> str:
    """
    Gets the absolute path of a file.

    *Examples:*

    >>> get_absolute_path('file.txt') # returns 'C:\\Users\\User\\Desktop\\file.txt'

    :param path: The path to the file.
    :type path: str
    :return: The absolute path of the file.
    :rtype: str
    """
    return os.path.abspath(path)

def get_parent_dir(path: str) -> str:
    """
    Gets the directory path of a file.

    *Examples:*

    >>> get_dir_path('C:\\Users\\User\\Desktop\\file.txt') # returns 'C:\\Users\\User\\Desktop'

    :param path: The path to the file.
    :type path: str
    :return: The directory path of the file.
    :rtype: str
    """
    return os.path.dirname(path)

def get_extension(path: str) -> str:
    """
    Gets the extension of a file.

    *Examples:*

    >>> get_extension('C:\\Users\\User\\Desktop\\file.txt') # returns 'txt'

    :param path: The path to the file.
    :type path: str
    :return: The extension of the file.
    :rtype: str
    """
    return os.path.splitext(path)[1][1:]

def get_creation_datetime(path: str) -> dt.datetime:
    """
    Gets the creation datetime of a file.

    *Examples:*

    >>> get_creation_datetime('C:\\Users\\User\\Desktop\\file.txt') # returns '2020-01-01 00:00:00'

    :param path: The path to the file.
    :type path: str
    :return: The creation datetime of the file.
    :rtype: dt.datetime
    """
    # return creation time in datetime format
    if is_file(path):
        return dt.datetime.fromtimestamp(os.path.getctime(path))

def get_modification_datetime(path: str) -> dt.datetime:
    """
    Gets the modification datetime of a file.

    *Examples:*

    >>> get_modification_datetime('C:\\Users\\User\\Desktop\\file.txt') # returns '2020-01-01 00:00:00'

    :param path: The path to the file.
    :type path: str
    :return: The modification datetime of the file.
    :rtype: dt.datetime
    """
    if is_file(path):
        return dt.datetime.fromtimestamp(os.path.getmtime(path))

def get_access_datetime(path: str) -> dt.datetime:
    """
    Gets the access datetime of a file.

    *Examples:*

    >>> get_access_datetime('C:\\Users\\User\\Desktop\\file.txt') # returns '2020-01-01 00:00:00'

    :param path: The path to the file.
    :type path: str
    :return: The access datetime of the file.
    :rtype: dt.datetime
    """
    if is_file(path):
        return dt.datetime.fromtimestamp(os.path.getatime(path))

def get_owner(path: str) -> str:
    """
    Gets the user who owns the file.

    @TODO: It works for Windows. Needed testing for other SOs.

    *Examples:*

    >>> get_owner('C:\\Users\\User\\Desktop\\file.txt') # returns 'User'

    :param path: The path to the file.
    :type path: str
    :return: The owner of the file.
    :rtype: str
    """
    if is_file(path):
        if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            import pwd
            return pwd.getpwuid(os.stat(path).st_uid).pw_name
        elif sys.platform.startswith('win'):
            import win32security
            sd = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner()
            name, domain, type = win32security.LookupAccountSid(None, owner_sid)
            return name

def get_group(path: str) -> str:
    """
    Gets the group of a file (only for Unix)
    Get the owner of a directory first with get_owner()
    and then get all the groups of that user.

    @TODO: This function doesn't work as expected (only tested in Windows).

    *Examples:*

    >>> get_group('C:\\Users\\User\\Desktop\\file.txt') # returns 'User'

    :param path: The path to the file.
    :type path: str
    :return: The group of the file.
    :rtype: str
    """
    if is_file(path):
        if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            import grp
            return grp.getgrgid(os.stat(path).st_gid).gr_name
        elif sys.platform.startswith('win'):
            import win32security
            sd = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner()
            name, domain, type = win32security.LookupAccountSid(None, owner_sid)
            return name

def get_encoding(path: str) -> str:
    """
    Gets the encoding of a file.
    @TODO: Doesn't work as expected. Fix this function.

    *Examples:*

    >>> get_encoding('C:\\Users\\User\\Desktop\\file.txt') # returns 'utf-8'

    :param path: The path to the file.
    :type path: str
    :return: The encoding of the file.
    :rtype: str
    """
    if is_file(path):
        return chardet.detect(open(path, 'r', encoding='utf-8').read().encode())['encoding']


