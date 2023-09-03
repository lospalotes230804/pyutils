"""
This file contains functions for processing directories.
"""

# Importing the required libraries
import os
import sys
import shutil
import src.utils.string.validate as str
from .validate import is_dir, is_empty, is_hidden, is_visible  # , is_readonly, is_writable
from .info import get_absolute_path, get_parent_dir, get_name
from stat import S_IREAD, S_IWRITE

# Constants
DEFAULT_TIMESTAMP_FORMAT = "%Y%m%d-%H%M%S"

# Operations about existence / content

def create(path: str) -> bool:
    """
    Method to create the directory, if not exists.

    *Examples:*

    >>> create('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory was created successfully. False otherwise.
    :rtype: bool
    """
    if str.is_path(path) and not is_dir(path):
        os.mkdir(path)
        return is_dir(path)
    return False

def delete(path: str) -> bool:
    """
    Method to delete the directory, if exists.
    If is not empty, empty it first.

    *Examples:*

    >>> delete('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory was deleted successfully. False otherwise.
    :rtype: bool
    """
    # if is_dir(path) and is_writable(path):
    if is_dir(path):
        try:
            shutil.rmtree(path, onerror=lambda func, path, _: (os.chmod(path, S_IWRITE), func(path)))
        except Exception as e:
            pass
        return not is_dir(path)
    return False

def empty(path: str) -> bool:
    """
    Method to empty the directory, if exists.

    *Examples:*

    >>> empty('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory was emptied successfully. False otherwise.
    :rtype: bool
    """
    # if is_dir(path) and is_writable(path):
    if is_dir(path):
        try:
            # Loop through all items in the directory
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                # If it's a file and remove it
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                # If it's a directory and remove it recursively
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
        except Exception as e:
            pass
        return is_empty(path)
    return False

def rename(path: str, new_path: str) -> str:
    """
    Method to rename the directory, if exists.

    *Examples:*

    >>> rename('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\new_directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :param new_path: The new path to the directory.
    :type new_path: str
    :return: The path to the renamed directory, if success. None otherwise.
    :rtype: str
    """
    # if is_dir(path) and is_writable(path):
    if is_dir(path):
        if is_dir(new_path):
            new_path = get_duplicated_path(new_path)
        os.rename(path, new_path)
        if is_dir(new_path):
            return new_path

def copy(path: str, new_path: str) -> str:
    """
    Method to copy dir, return True if success
    If copied dir exists rename it with timestamp

    *Examples:*

    >>> copy('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\new_directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :param new_path: The new path to the directory.
    :type overwrite: bool
    :return: The path to the copied directory, if success. None otherwise.
    :rtype: str
    """
    # if is_dir(path) and is_writable(path):
    if is_dir(path):
        if is_dir(new_path):
            new_path = get_duplicated_path(new_path)
        shutil.copytree(path, new_path)
        if is_dir(new_path):
            return new_path

def duplicate(path: str) -> str:
    """
    Method to duplicate dir, return new path if success
    If duplicated dir exists rename it with timestamp

    *Examples:*

    >>> duplicate('C:\\Users\\User\\Desktop\\directory') # returns 'C:\\Users\\User\\Desktop\\directory_20201231-235959'

    :param path: The path to the directory.
    :type path: str
    :return: The path to the duplicated directory, if success. None otherwise.
    :rtype: str
    """
    if is_dir(path):
        new_path = get_duplicated_path(path)
        if copy(path, new_path) and is_dir(new_path):
            return new_path

def get_duplicated_path(path) -> str:
    """
    Method to get a duplicated path
    If the path is duplicated add a sequential number to the original name, in a Windows style (1), (2), etc.

    *Examples:*

    >>> get_duplicated_path('C:\\Users\\User\\Desktop\\directory') # returns 'C:\\Users\\User\\Desktop\\directory (1)'

    :param path: The path to an existing directory.
    :type path: str
    :return: The path to be used as new_path for duplicating the directory.
    :rtype: str
    """
    path1 = get_absolute_path(path)
    path = os.path.dirname(path)
    name = os.path.basename(path)
    if is_dir(path):
        # Check input parameters
        # Split parts of the new_path
        path = os.path.dirname(path1)
        name = os.path.basename(path1)
        sequential_number = 1
        # If new_path exists, add a sequential number, in a Windows style (1), (2), etc.
        while os.path.exists(os.path.join(path, name + f" ({sequential_number})")):
            sequential_number += 1
        # Add sequential number to the name
        new_path = os.path.join(path, name + f" ({sequential_number})")
        return new_path

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
    :return: True if the directory was moved successfully. False otherwise.
    :rtype: bool
    """
    # if (is_dir(path) and is_writable(path)
    if (is_dir(path)
            and not is_dir(new_path)):
        if copy(path, new_path):
            delete(path)
            return is_dir(new_path)
    return False

def set_hidden(path: str) -> bool:
    """
    Method to hide dir, return True if success

    *Examples:*

    >>> set_hidden('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is set hidden successfully. False otherwise.
    :rtype: bool
    """
    # if is_dir(path) and is_writable(path):
    if is_dir(path):
        if is_hidden(path):
            return True
        else:
            if sys.platform.startswith('win'):    # windows
                os.system("attrib +h " + path)
            else:                                 # linux
                # fusionate dir path + . + dir name
                os.rename(path, get_parent_dir(path) + "/." + get_name(path))
        return is_hidden(path)
    return False

def set_visible(path: str) -> bool:
    """
    Method to unhide dir, return True if success

    *Examples:*

    >>> set_visible('C:\\Users\\User\\Desktop\\directory') # returns True

    :param path: The path to the directory.
    :type path: str
    :return: True if the directory is set visible successfully. False otherwise.
    :rtype: bool
    """
    # if is_dir(path) and is_writable(path):
    if is_dir(path):
        if not is_hidden(path):
            return True
        else:
            if sys.platform.startswith('win'):    # windows
                os.system("attrib -h " + path)
            else:                                 # linux
                # fusionate dir path + . + dir name
                os.rename(path, get_parent_dir(path) + "/" + get_name(path)[1:])
        return is_visible(path)
    return False
