"""
This file contains functions for obtaining information about a directory.
"""

# Importing the required libraries
import os
import sys
import datetime as dt
import utils.file.info as fil
from utils.directory.validate import is_dir, is_hidden
from utils.directory.info import get_absolute_path, get_dir_path, get_name

# Get information about a directory


def get_size(path: str) -> int:
    """
    Gets the size of a directory in bytes.

    *Examples:*

    >>> get_size('C:\\Users\\User\\Desktop\\') # returns 1024

    :param path: The path to the directory.
    :type path: str
    :return: The size of the directory in bytes.
    """
    if is_dir(path):
        return sum(os.path.getsize(os.path.join(path, f)) for f in os.listdir(path))


def get_name(path: str) -> str:
    """
    Gets the name of a directory.

    *Examples:*

    >>> get_name('C:\\Users\\User\\Desktop\\') # returns 'Desktop'

    :param path: The path to the directory.
    :type path: str
    :return: The name of the directory.
    """
    if is_dir(path):
        return os.path.basename(path)


def get_relative_path(path: str) -> str:
    """
    Gets the relative path of a directory.

    *Examples:*

    >>> get_relative_path('C:\\Users\\User\\Desktop\\') # returns 'Desktop'

    :param path: The path to the directory.
    :type path: str
    :return: The relative path of the directory.
    """
    if is_dir(path):
        return os.path.relpath(path)


def get_absolute_path(path: str) -> str:
    """
    Gets the absolute path of a directory.

    *Examples:*

    >>> get_absolute_path('Desktop') # returns 'C:\\Users\\User\\Desktop\\'

    :param path: The path to the directory.
    :type path: str
    :return: The absolute path of the directory.
    """
    if is_dir(path):
        return os.path.abspath(path)


def get_dir_path(path: str) -> str:
    """
    Gets the directory path of a directory.

    *Examples:*

    >>> get_dir_path('C:\\Users\\User\\Desktop\\') # returns 'C:\\Users\\User\\'

    :param path: The path to the directory.
    :type path: str
    :return: The directory path of the directory.
    """
    if is_dir(path):
        return os.path.dirname(path)


def get_creation_datetime(path: str) -> dt.datetime:
    """
    Gets the creation time of a directory.

    *Examples:*

    >>> get_creation_time('C:\\Users\\User\\Desktop\\') # returns 1612345678.0

    :param path: The path to the directory.
    :type path: str
    :return: The creation time of the directory.
    """
    if is_dir(path):
        return os.path.getctime(path)


def get_modification_datetime(path: str) -> dt.datetime:
    """
    Gets the modification time of a directory.

    *Examples:*

    >>> get_modification_time('C:\\Users\\User\\Desktop\\') # returns 1612345678.0

    :param path: The path to the directory.
    :type path: str
    :return: The modification time of the directory.
    """
    if is_dir(path):
        return os.path.getmtime(path)


def get_access_datetime(path: str) -> dt.datetime:
    """
    Gets the access time of a directory.

    *Examples:*

    >>> get_access_time('C:\\Users\\User\\Desktop\\') # returns 1612345678.0

    :param path: The path to the directory.
    :type path: str
    :return: The access time of the directory.
    """
    if is_dir(path):
        return os.path.getatime(path)


def get_owner(path: str) -> str:
    """
    Gets the owner of a directory.

    *Examples:*

    >>> get_owner('C:\\Users\\User\\Desktop\\') # returns 'User'

    :param path: The path to the directory.
    :type path: str
    :return: The owner of the directory.
    """
    if is_dir(path):
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
    Gets the group of a directory.

    *Examples:*

    >>> get_group('C:\\Users\\User\\Desktop\\') # returns 'User'

    :param path: The path to the directory.
    :type path: str
    :return: The group of the directory.
    """
    if is_dir(path):
        if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            import grp
            return grp.getgrgid(os.stat(path).st_gid).gr_name
        elif sys.platform.startswith('win'):
            import win32security
            sd = win32security.GetFileSecurity(path, win32security.GROUP_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorGroup()
            name, domain, type = win32security.LookupAccountSid(None, owner_sid)
            return name


def get_content(path: str, hidden=False) -> list:
    """
    Gets the content of a directory.

    *Examples:*

    >>> get_content('C:\\Users\\User\\Desktop\\') # returns ['file1.txt', 'file2.txt', 'file3.txt']
    >>> get_content('C:\\Users\\User\\Desktop\\', hidden=True) # returns ['file1.txt', 'file2.txt', 'file3.txt', '.file4.txt']

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory.
    """
    # if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    #     if hidden:
    #         return os.listdir(path)
    #     else:
    #         return [x for x in os.listdir(path) if not x.startswith('.')]
    # elif sys.platform.startswith('win'):
    #     if hidden:
    #         return os.listdir(path)
    #     else:
    #         return [x for x in os.listdir(path) if not x.startswith('.')]
    if is_dir(path):
        tree = []
        if hidden:   # all content (hidden and not hidden)
            for root, dirs, files in os.walk(path):
                tree.append(root)
                for d in dirs:
                    tree.append(d)
                for f in files:
                    tree.append(f)

        else:        # all non-hidden content
            for root, dirs, files in os.walk(path):
                if not is_hidden(root):
                    tree.append(root)
                for d in dirs:
                    if not is_hidden(d):
                        tree.append(d)
                for f in files:
                    if not is_hidden(f):
                        tree.append(f)
        return tree


def get_content_with_size(path: str, hidden=False) -> list:
    """
    Gets the content of a directory with the size of each file.

    *Examples:*

    >>> get_content_with_size('C:\\Users\\User\\Desktop\\') # returns [('file1.txt', 1024), ('file2.txt', 1024), ('file3.txt', 1024)]
    >>> get_content_with_size('C:\\Users\\User\\Desktop\\', hidden=True) # returns [('file1.txt', 1024), ('file2.txt', 1024), ('file3.txt', 1024), ('.file4.txt', 1024)]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory with the size of each file.
    """
    if is_dir(path):
        tree = []
        if hidden:   # all content (hidden and not hidden)
            for root, dirs, files in os.walk(path):
                tree.append(root)
                for d in dirs:
                    tree.append(d,
                                get_size(d))
                for f in files:
                    tree.append((f,
                                 fil.get_size(f)))

        else:        # all non-hidden content
            for root, dirs, files in os.walk(path):
                if not is_hidden(root):
                    tree.append(root)
                for d in dirs:
                    if not is_hidden(d):
                        tree.append(d,
                                    get_size(d))
                for f in files:
                    if not is_hidden(f):
                        tree.append((f,
                                     fil.get_size(f)))
        return tree


def get_content_with_size_type(path: str, hidden=False) -> list:
    """
    Gets the content of a directory with the size and type of each file.

    *Examples:*

    >>> get_content_with_size_type('C:\\Users\\User\\Desktop\\') # returns [('file1.txt', 1024, 'txt'), ('file2.txt', 1024, 'txt'), ('file3.txt', 1024, 'txt')]
    >>> get_content_with_size_type('C:\\Users\\User\\Desktop\\', hidden=True) # returns [('file1.txt', 1024, 'txt'), ('file2.txt', 1024, 'txt'), ('file3.txt', 1024, 'txt'), ('.file4.txt', 1024, 'txt')]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory with the size and type of each file.
    """
    if is_dir(path):
        tree = []
        if hidden:   # all content (hidden and not hidden)
            for root, dirs, files in os.walk(path):
                tree.append(root)
                for d in dirs:
                    tree.append(d,
                                get_size(d),
                                None)
                for f in files:
                    tree.append((f,
                                 fil.get_size(f),
                                 fil.get_extension(f)))

        else:        # all non-hidden content
            for root, dirs, files in os.walk(path):
                if not is_hidden(root):
                    tree.append(root)
                for d in dirs:
                    if not is_hidden(d):
                        tree.append(d,
                                    get_size(d),
                                    None)
                for f in files:
                    if not is_hidden(f):
                        tree.append((f,
                                     fil.get_size(f),
                                     fil.get_extension(f)))
        return tree


def get_content_with_size_type_date(path: str, hidden=False) -> list:
    """
    Gets the content of a directory with the size, type and date of each file.

    *Examples:*

    >>> get_content_with_size_type_date('C:\\Users\\User\\Desktop\\') # returns [('file1.txt', 1024, 'txt', 1612345678.0), ('file2.txt', 1024, 'txt', 1612345678.0), ('file3.txt', 1024, 'txt', 1612345678.0)]
    >>> get_content_with_size_type_date('C:\\Users\\User\\Desktop\\', hidden=True) # returns [('file1.txt', 1024, 'txt', 1612345678.0), ('file2.txt', 1024, 'txt', 1612345678.0), ('file3.txt', 1024, 'txt', 1612345678.0), ('.file4.txt', 1024, 'txt', 1612345678.0)]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory with the size, type and date of each file.
    """
    if is_dir(path):
        tree = []
        if hidden:   # all content (hidden and not hidden)
            for root, dirs, files in os.walk(path):
                tree.append(root)
                for d in dirs:
                    tree.append(d,
                                get_size(d),
                                None,
                                get_creation_datetime(d))
                for f in files:
                    tree.append((f,
                                 fil.get_size(f),
                                 fil.get_extension(f),
                                 fil.get_creation_datetime(f)))

        else:        # all non-hidden content
            for root, dirs, files in os.walk(path):
                if not is_hidden(root):
                    tree.append(root)
                for d in dirs:
                    if not is_hidden(d):
                        tree.append(d,
                                    get_size(d),
                                    None,
                                    get_creation_datetime(d))
                for f in files:
                    if not is_hidden(f):
                        tree.append((f,
                                     fil.get_size(f),
                                     fil.get_extension(f),
                                     fil.get_creation_datetime(f)))
        return tree


# def get_content_recursive
