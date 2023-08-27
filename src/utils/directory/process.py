"""
This file contains functions for processing directories.
"""

# Importing the required libraries
import os
import sys
import shutil
import ntpath
import datetime as dt
import utils.string.validate as str
import utils.file.validate as fil
from utils.directory.validate import is_dir, is_empty, is_writable
from utils.directory.info import get_absolute_path

# Constants
DEFAULT_TIMESTAMP_FORMAT = "%Y%m%d-%H%M%S"

# Basic file operations


def create(path: str) -> bool:
    """
    Method to create the directory, if not exists.

    *Examples:*

    >>> create('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory was created successfully
    """
    if str.is_path(path) and not is_dir(path):
        os.mkdir(path)
        return is_dir(path)


def delete(path: str) -> bool:
    """
    Method to delete the directory, if exists.
    If is not empty, empty it first.

    *Examples:*

    >>> delete('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory was deleted successfully
    """
    if str.is_path(path) and is_dir(path) and is_writable(path):
        if is_empty(path):
            os.rmdir(path)
        else:
            empty(path)
            os.rmdir(path)
        return not is_dir(path)


def empty(path: str) -> bool:
    """
    Method to empty the directory, if exists.

    *Examples:*

    >>> empty('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory was emptied successfully
    """
    if str.is_path(path) and is_dir(path) and is_writable(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        return is_empty(path)


def rename(path: str, new_path: str) -> bool:
    """
    Method to rename the directory, if exists.

    *Examples:*

    >>> rename('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\new_directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :param new_path: The new path to the directory.
    :type new_path: str
    :return: True if the directory was renamed successfully
    """
    if (str.is_path(path) and is_dir(path)
            and is_writable(path) and not is_dir(new_path)):
        os.rename(path, new_path)
        return is_dir(new_path)


def copy(path: str, new_path: str) -> bool:
    """
    Method to copy dir, return True if success
    If copied dir exists rename it with timestamp

    *Examples:*

    >>> copy('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\new_directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :param new_path: The new path to the directory.
    :type overwrite: bool
    :return: True if the directory was copied successfully
    """
    if str.is_path(path) and is_dir(path) and is_writable(path):
        if is_dir(new_path):
            new_path = get_duplicated_path(new_path)
        shutil.copytree(path, new_path)
        return is_dir(new_path)


def duplicate(path: str) -> str:
    """
    Method to duplicate dir, return new path if success
    If duplicated dir exists rename it with timestamp

    *Examples:*

    >>> duplicate('C:\\Users\\User\\Desktop\\directory') # returns 'C:\\Users\\User\\Desktop\\directory_20201231-235959'

    :param path: The path to the directory.
    :type path: str
    :return: The path to the duplicated directory.
    """
    if str.is_path(path) and is_dir(path) and is_writable(path):
        new_path = get_duplicated_path(path)
        return copy(path, new_path)


def get_duplicated_path(path_to_duplicate) -> str:
    """
    Method to get a duplicated path, if exists.
    If the path is duplicated add a sequential number to the original name, in a Windows style (1), (2), etc.

    *Examples:*

    >>> get_duplicated_path('C:\\Users\\User\\Desktop\\directory') # returns 'C:\\Users\\User\\Desktop\\directory (1)'

    :param path: The path to the directory.
    :type path: str
    :return: The duplicated path.
    """
    # Set new_path
    if sys.platform.startswith('win'):
        path = ntpath.dirname(path_to_duplicate)
        name1 = ntpath.basename(path_to_duplicate)
    else:
        path = os.path.dirname(path_to_duplicate)
        name1 = os.path.basename(path_to_duplicate)
    n = 1
    # If new_path exists, add a sequential number, in a Windows style (1), (2), etc.
    # If "nuevo nombre (1)" exists, try with "nuevo nombre (2)", etc.
    # Ends with (n)
    if name1.endswith(" (" + str(n) + ")"):
        # Get sequential number
        n = int(name1.split(" (")[-1].split(")")[0])
        # Get name without sequential number
        name2 = name1.split(" (")[0].strip()
        while name1.endswith(" (" + str(n) + ")"):
            n += 1
        new_name = os.path.join(path, f"{name2} ({n})")
        return new_name
    # Doesn't end with (n)
    else:
        new_name = os.path.join(path, f"{name1} ({1})")
        return new_name


def move(path, new_path: str) -> bool:
    """
    Method to move dir, return new path if success
    If moved dir exists rename it with timestamp

    *Examples:*

    >>> move('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\new_directory') # returns 'C:\\Users\\User\\Desktop\\new_directory\\directory'

    :param path: The path to the directory.
    :type path: str
    :param new_path: The new dir path to the directory.
    :type new_path: str
    :return: True if the directory was moved successfully
    """
    if (str.is_path(path) and is_dir(path)
            and is_writable(path) and not is_dir(new_path)):
        if copy(path, new_path):
            delete(path)
            return is_dir(new_path)
