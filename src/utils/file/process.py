"""
This file contains functions for processing files.
"""

# Importing the required libraries
import os
import shutil
import datetime as dt
import utils.string.validate as str
import utils.directory.validate as dir
from utils.file.validate import is_file
from utils.file.info import get_absolute_path, get_parent_dir, get_extension, get_name

# Constants
DEFAULT_ENCODING = "utf-8"
DEFAULT_TIMESTAMP_FORMAT = "%Y%m%d-%H%M%S"

# Basic file operations

def create(path: str) -> bool:
    """
    Creates a file.

    *Examples:*

    >>> create('C:\\Users\\User\\Desktop\\file.txt') # creates the file

    :param path: The path to the file.
    :type path: str
    :return: True if the file was created, False otherwise.
    """
    path = get_absolute_path(path)
    if not is_file(path):
        open(path, 'w', DEFAULT_ENCODING).close()
        return True

def delete(path: str) -> bool:
    """
    Deletes a file.

    *Examples:*

    >>> delete('C:\\Users\\User\\Desktop\\file.txt') # deletes the file

    :param path: The path to the file.
    :type path: str
    :return: True if the file was deleted, False otherwise.
    """
    path = get_absolute_path(path)
    if is_file(path):
        os.remove(path)
        return True

def read(path: str) -> str:
    """
    Reads the content of a file.

    *Examples:*

    >>> read('C:\\Users\\User\\Desktop\\file.txt') # returns the content of the file as a string

    :param path: The path to the file.
    :type path: str
    :return: The content of the file as a string.
    """
    path = get_absolute_path(path)
    if is_file(path):
        return open(path, 'r', DEFAULT_ENCODING).read()

def write(path: str, content: str) -> bool:
    """
    Writes content to a file.

    *Examples:*

    >>> write('C:\\Users\\User\\Desktop\\file.txt') # writes the content to the file

    :param path: The path to the file.
    :type path: str
    :return: True if the content was written to the file, False otherwise.
    """
    path = get_absolute_path(path)
    if is_file(path):
        open(path, 'w', DEFAULT_ENCODING).write(content)
        return True

def append(path: str, content: str) -> bool:
    """
    Appends content to a file.

    *Examples:*

    >>> append('C:\\Users\\User\\Desktop\\file.txt') # appends the content to the end of the file

    :param path: The path to the file.
    :type path: str
    :return: True if the content was appended to the file, False otherwise.
    """
    path = get_absolute_path(path)
    if is_file(path):
        open(path, 'a', DEFAULT_ENCODING).write(content)
        return True

def empty(path: str) -> bool:
    """
    Empties a file.

    *Examples:*

    >>> empty('C:\\Users\\User\\Desktop\\file.txt') # empties the file

    :param path: The path to the file.
    :type path: str
    :return: True if the file was emptied, False otherwise.
    """
    path = get_absolute_path(path)
    if is_file(path):
        open(path, 'w', DEFAULT_ENCODING).close()
        return True

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
    """
    path = get_absolute_path(path)
    new_path = get_absolute_path(new_path)
    if (is_file(path)
        and str.is_path(new_path)
            and not is_file(new_path)):
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
    """
    path = get_absolute_path(path)
    if is_file(new_path):
        new_path = get_duplicated_path(new_path)
    else:
        new_path = get_absolute_path(new_path)
    if (is_file(path)
        and str.is_path(new_path)
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
    Method to get duplicated path of a file.
    If the path is duplicated add a sequential number to the original name, in a Windows style (1), (2), etc.

    *Examples:*

    >>> get_duplicated_path('C:\\Users\\User\\Desktop\\file.txt') # returns 'C:\\Users\\User\\Desktop\\file (1).txt'

    :param path: The path to the file.
    :type path: str
    :return: The path with the duplicated name, to be used as new_path if copying or moving the file.
    """
    # Check input parameters
    path1 = get_absolute_path(path)
    # Split parts of new_path
    path = os.path.dirname(path1)
    name = os.path.basename(path1)
    extension = os.path.splitext(name)[1]
    sequential_number = 1
    # If new_path exists, add a sequential number, in a Windows style (1), (2), etc.
    while os.path.exists(os.path.join(path, name + f" ({sequential_number})" + extension)):
        sequential_number += 1
    # Add sequential number to the name
    return os.path.join(path, name + f" ({sequential_number})" + extension)

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
    """
    path = get_absolute_path(path)
    if is_file(path):
        # Get the timestamp
        timestamp = dt.datetime.now().strftime(DEFAULT_TIMESTAMP_FORMAT)
        new_name = get_name(path) + "-" + timestamp + get_extension(path)
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
    """
    path = get_absolute_path(path)
    new_dir = get_absolute_path(new_dir)
    if is_file(path) and str.is_dir(new_dir):
        new_path = os.path.join(new_dir, get_name(path) + get_extension(path))
        if is_file(new_path):
            if overwrite:
                delete(new_path)
            else:
                new_path = get_duplicated_path(new_path)
        shutil.move(path, new_path)
        return new_path

# def display_info(path: str) -> bool:
