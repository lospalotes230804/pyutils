"""
This file contains functions for processing files.
"""

# Importing the required libraries
import os
import sys
import shutil
import datetime as dt
import src.utils.string.validate as stvl
from src.utils.file.validate import is_file, is_hidden, is_readonly  # , is_readonly, is_writable
from src.utils.file.info import get_parent_dir, get_filename, get_absolute_path
from src.utils.file.info import get_extension, get_filename, get_filename_w_ext
from src.utils.directory.validate import is_dir
from stat import S_IREAD

# Constants
DEFAULT_ENCODING = "utf-8"
DEFAULT_TIMESTAMP_FORMAT = "%Y%m%d-%H%M%S"

# Operations about existence / content

def create(path: str) -> bool:
    """
    Creates a file.

    *Examples:*

    >>> create('C:\\Users\\User\\Desktop\\file.txt') # creates the file

    :param path: The path to the file.
    :type path: str
    :return: True if the file was created, False otherwise.
    :rtype: bool
    """
    if not is_file(path):
        open(path, 'w+', encoding="UTF-8").close()
        return True
    return False

def delete(path: str) -> bool:
    """
    Deletes a file.

    *Examples:*

    >>> delete('C:\\Users\\User\\Desktop\\file.txt') # deletes the file

    :param path: The path to the file.
    :type path: str
    :return: True if the file was deleted, False otherwise.
    :rtype: bool
    """
    path = get_absolute_path(path)
    # if is_file(path) and not is_readonly(path) and is_writable(path):
    if is_file(path) and not is_readonly(path):
        os.remove(path)
        return True
    return False

def read(path: str) -> str:
    """
    Reads the content of a file.

    *Examples:*

    >>> read('C:\\Users\\User\\Desktop\\file.txt') # returns the content of the file as a string

    :param path: The path to the file.
    :type path: str
    :return: The content of the file as a string.
    :rtype: str
    """
    path = get_absolute_path(path)
    # if is_file(path) and is_readable(path):
    if is_file(path):
        return open(path, 'r+', encoding="utf-8").read()
    return False

def write(path: str, content: str) -> bool:
    """
    Writes content to a file.

    *Examples:*

    >>> write('C:\\Users\\User\\Desktop\\file.txt') # writes the content to the file

    :param path: The path to the file.
    :type path: str
    :return: True if the content was written to the file, False otherwise.
    :rtype: bool
    """
    path = get_absolute_path(path)
    # if is_file(path) and not is_readonly(path) and is_writable(path):
    if is_file(path) and not is_readonly(path):
        open(path, 'w+', encoding="utf-8").write(content)
        return True
    return False

def append(path: str, content: str) -> bool:
    """
    Appends content to a file.

    *Examples:*

    >>> append('C:\\Users\\User\\Desktop\\file.txt') # appends the content to the end of the file

    :param path: The path to the file.
    :type path: str
    :return: True if the content was appended to the file, False otherwise.
    :rtype: bool
    """
    path = get_absolute_path(path)
    # if is_file(path) and not is_readonly(path) and is_writable(path):
    if is_file(path) and not is_readonly(path):
        open(path, 'a+', encoding="utf-8").write(content)
        return True
    return False

def empty(path: str) -> bool:
    """
    Empties a file.

    *Examples:*

    >>> empty('C:\\Users\\User\\Desktop\\file.txt') # empties the file

    :param path: The path to the file.
    :type path: str
    :return: True if the file was emptied, False otherwise.
    :rtype: bool
    """
    path = get_absolute_path(path)
    # if is_file(path) and not is_readonly(path) and is_writable(path):
    if is_file(path) and not is_readonly(path):
        open(path, 'w+', encoding="utf-8").close()
        return True
    return False

def rename(path: str, new_path: str) -> str:
    """
    Method to rename file, return new path if success

    *Examples:*

    >>> rename('C:\\Users\\User\\Desktop\\file.txt', 'file2.txt') # renames the file

    :param path: The path to the file.
    :type path: str
    :param new_path: The new path to the file.
    :type new_path: str
    :return: The path to the renamed file.
    :rtype: str
    """
    path = get_absolute_path(path)

    if not stvl.is_path(new_path) and stvl.is_filename(new_path):
        new_path = get_parent_dir(path) + "\\" + new_path

    # if (is_file(path) and not is_readonly(path) and is_writable(path)
    if (is_file(path) and not is_readonly(path)
            and stvl.is_path(new_path) and not is_file(new_path)):
        os.rename(path, new_path)
    if is_file(new_path):
        return new_path

def copy(path: str, new_path: str) -> str:
    """
    Method to copy file, return new path if success

    *Examples:*

    >>> copy('C:\\Users\\User\\Desktop\\file.txt', 'C:\\Users\\User\\Desktop\\file2.txt')
        # returns 'C:\\Users\\User\\Desktop\\file2.txt' if the destination file does not exist
    >>> copy('C:\\Users\\User\\Desktop\\file.txt', 'C:\\Users\\User\\Desktop\\file2.txt')
        # returns 'C:\\Users\\User\\Desktop\\file2 (1).txt' if the destination file exists

    :param path: The path to the file to copy.
    :type path: str
    :param new_path: The path to the new file.
    :type new_path: str
    :return: The path to the copied file.
    :rtype: str
    """
    path = get_absolute_path(path)
    if is_file(new_path):
        new_path = get_duplicated_path(new_path)
    else:
        new_path = get_absolute_path(new_path)
    if (is_file(path)
        and stvl.is_path(new_path)
            and not is_file(new_path)):
        shutil.copy(path, new_path)
    if is_file(new_path):
        return new_path

def duplicate(path: str) -> str:
    """
    Method to duplicate file, return new path if success

    *Examples:*

    >>> duplicate('C:\\Users\\User\\Desktop\\file.txt') # returns 'C:\\Users\\User\\Desktop\\file (1).txt' if 'file (1).txt' does not exist
    >>> duplicate('C:\\Users\\User\\Desktop\\file.txt') # returns 'C:\\Users\\User\\Desktop\\file (2).txt' if 'file (1).txt' already exists

    :param path: The path to the file to duplicate.
    :type path: str
    :return: The path to the duplicated file.
    :rtype: str
    """
    path = get_absolute_path(path)
    new_path = get_duplicated_path(path)
    if is_file(path) and not is_file(new_path):
        new_path = get_duplicated_path(path)
        shutil.copy(path, new_path)
    if is_file(new_path):
        return new_path

def get_duplicated_path(path) -> str:
    """
    Method to get the a path so a file can be duplicated
    without overwriting the original file.

    If the new_path exists, add a sequential number to the original name
    , in a Windows style (1), (2), etc.

    *Examples:*

    >>> get_duplicated_path('C:\\Users\\User\\Desktop\\file.txt') # returns 'C:\\Users\\User\\Desktop\\file (1).txt'

    :param path: The path to an existing file.
    :type path: str
    :return: The path to be used as new_path for duplicating the file.
    :rtype: str
    """
    path1 = get_absolute_path(path)
    if is_file(path):
        # Check input parameters
        # Split parts of new_path
        path = os.path.dirname(path1)
        name = get_filename_w_ext(path1)
        extension = '.' + get_extension(path1)
        sequential_number = 1
        # If new_path exists, add a sequential number, in a Windows style (1), (2), etc.
        while os.path.exists(os.path.join(path, name + f" ({sequential_number})" + extension)):
            sequential_number += 1
        # Add sequential number to the name
        new_path = os.path.join(path, name + f" ({sequential_number})" + extension)
        return new_path

def archive(path: str) -> str:
    """
    Method to archive file, return new path if success
    1. Create a copy of the file with a timestamp
    2. Touch the original file so its modification time is newer than the copy

    *Examples:*

    >>> archive('C:\\Users\\User\\Desktop\\file.txt') # returns 'C:\\Users\\User\\Desktop\\file.txt.20210101-000000'

    :param path: The path to the file.
    :type path: str
    :return: The path to the archived file, with a timestamp in given format.
    :rtype: str
    """
    path = get_absolute_path(path)
    if is_file(path):
        # Get the timestamp
        timestamp = dt.datetime.now().strftime(DEFAULT_TIMESTAMP_FORMAT)
        new_name = get_filename(path) + "-" + timestamp + get_extension(path)
        new_path = os.path.join(get_parent_dir(path), new_name)
        # Create a copy of the file with a timestamp
        copy(path, new_path)
        # Touch the original file so its modification time is newer than the copy
        os.utime(path, None)
        if is_file(new_path):
            return new_path

def move(path, new_dir: str, overwrite=False) -> str:
    """
    Method to move file, return new path if success
    1. Check if new_path exists
    2. If exists and overwrite is True, delete new_path

    *Examples:*

    >>> move('C:\\Users\\User\\Desktop\\file.txt', 'C:\\Users\\User\\Documents\\') # returns 'C:\\Users\\User\\Documents\\file.txt'

    :param path: The path to the file to move.
    :param new_dir: The path to the directory to move the file to.
    :type path: str
    :return: The path to the moved file.
    :rtype: str
    """
    path = get_absolute_path(path)
    new_dir = get_absolute_path(new_dir)
    if is_file(path) and is_dir(new_dir):
        new_path = os.path.join(new_dir, get_filename(path) + get_extension(path))
        if is_file(new_path):
            if overwrite:
                delete(new_path)
            else:
                new_path = get_duplicated_path(new_path)
        shutil.move(path, new_path)
        return new_path

# Operations about setting attributes

def set_hidden(path: str) -> bool:
    """
    Method to hide file, return True if success

    *Examples:*

    >>> set_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns True

    :param path: The path to the file.
    :type path: str
    :return: True if the file was hidden successfully
    :rtype: bool
    """
    # if is_file(path) and not is_readonly(path) and is_writable(path):
    if is_file(path) and not is_readonly(path):
        if is_hidden(path):
            return True
        else:
            if sys.platform.startswith('win'):    # windows
                os.system("attrib +h " + path)
            else:                                 # linux
                # fusionate dir path + . + dir name
                os.rename(path, get_parent_dir(path) + "/." + get_filename(path))
            return is_hidden(path)
    return False

def set_visible(path: str) -> bool:
    """
    Method to unhide file, return True if success

    *Examples:*

    >>> set_visible('C:\\Users\\User\\Desktop\\file.txt') # returns True

    :param path: The path to the file.
    :type path: str
    :return: True if the file is set visible successfully
    :rtype: bool
    """
    # if is_file(path) and not is_readonly(path) and is_writable(path):
    if is_file(path) and not is_readonly(path):
        if not is_hidden(path):
            return True
        if sys.platform.startswith('win'):    # windows
            os.system("attrib -h " + path)
        else:                                 # linux
            # fusionate dir path + . + dir name
            os.rename(path, get_parent_dir(path) + "/" + get_filename(path)[1:])
        return not is_hidden(path)
    return False

def set_readonly(path: str) -> bool:
    """
    Method to set file as readonly, return True if success

    *Examples:*

    >>> set_readonly('C:\\Users\\User\\Desktop\\file.txt') # returns True

    :param path: The path to the file.
    :type path: str
    :return: True if the file was set as readonly successfully
    :rtype: bool
    """
    if is_file(path) and not is_readonly(path):
        os.chmod(path, S_IREAD)
        return is_readonly(path)
    return False
