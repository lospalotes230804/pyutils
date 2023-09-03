"""
This file contains functions for obtaining information about a directory.
"""

# Importing the required libraries
import os
import sys
import datetime as dt
import src.utils.file.info as fil
from src.utils.file.validate import is_file
from .validate import is_dir, is_hidden  # , is_writable

# Get information about a directory

def get_size(path: str) -> int:
    """
    Gets the size of a directory in bytes.

    *Examples:*

    >>> get_size('C:\\Users\\User\\Desktop\\') # returns 1024

    :param path: The path to the directory.
    :type path: str
    :return: The size of the directory in bytes.
    :rtype: int
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
    :rtype: str
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
    :rtype: str
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
    :rtype: str
    """
    if is_dir(path):
        return os.path.abspath(path)

def get_parent_dir(path: str) -> str:
    """
    Gets the directory path of a directory.

    *Examples:*

    >>> get_dir_path('C:\\Users\\User\\Desktop\\') # returns 'C:\\Users\\User\\'

    :param path: The path to the directory.
    :type path: str
    :return: The directory path of the directory.
    :rtype: str
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
    :rtype: dt.datetime
    """
    if is_dir(path):
        return dt.datetime.fromtimestamp(os.path.getctime(path))

def get_modification_datetime(path: str) -> dt.datetime:
    """
    Gets the modification time of a directory.

    *Examples:*

    >>> get_modification_time('C:\\Users\\User\\Desktop\\') # returns 1612345678.0

    :param path: The path to the directory.
    :type path: str
    :return: The modification time of the directory.
    :rtype: dt.datetime
    """
    if is_dir(path):
        return dt.datetime.fromtimestamp(os.path.getmtime(path))

def get_access_datetime(path: str) -> dt.datetime:
    """
    Gets the access time of a directory.

    *Examples:*

    >>> get_access_time('C:\\Users\\User\\Desktop\\') # returns 1612345678.0

    :param path: The path to the directory.
    :type path: str
    :return: The access time of the directory.
    :rtype: dt.datetime
    """
    if is_dir(path):
        return dt.datetime.fromtimestamp(os.path.getatime(path))

def get_owner(path: str) -> str:
    """
    Gets the owner of a directory.

    @TODO: It works for Windows. Needed testing for other SOs.

    *Examples:*

    >>> get_owner('C:\\Users\\User\\Desktop\\') # returns 'User'

    :param path: The path to the directory.
    :type path: str
    :return: The owner of the directory.
    :rtype: str
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
    Gets the groups of the user who owns the directory.
    Get the owner of a directory first with get_owner()
    and then get all the groups of that user.

    @TODO: This function doesn't work as expected (only tested in Windows).

    *Examples:*

    >>> get_group('C:\\Users\\User\\Desktop\\') # returns 'User'

    :param path: The path to the directory.
    :type path: str
    :return: The group of the directory.
    :rtype: str
    """
    if is_dir(path):
        # os.getgrouplist() returns a list of group ids for a user
        if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            import grp
            return grp.getgrgid(os.stat(path).st_gid).gr_name
        elif sys.platform.startswith('win'):
            import win32security
            # Get the owner of a directory first with get_owner()
            sd = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner()
            # Get all the groups of that user.
            name, domain, type = win32security.LookupAccountSid(None, owner_sid)

def get_contents(directory, hidden=False):
    """
    Gets the contents of a directory.
    Recursively gets the contents of the subdirectories.
    Returns a list with the relative paths of directories and files.

    @TODO: This function doesn't work as expected (only tested in Windows).

    *Examples:*

    >>> get_content('C:\\Users\\User\\Desktop\\', hidden=True) # returns [
            'test_dir_inside',
            'test_hidden_dir_inside',
            'test_file_inside.txt',
            'test_hidden_file_inside.txt',
            'test_dir_inside\\test_file_inside.txt',
            'test_hidden_dir_inside\\test_hidden_file_inside.txt'
        ]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory.
    :rtype: list
    """
    contents = []
    for root, dirs, files in os.walk(directory):
        if not hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]
        for dir in dirs:
            contents.append(os.path.join(os.path.relpath(root), dir))
        for file in files:
            contents.append(os.path.join(os.path.relpath(root), file))
    return contents

def get_contents_with_size(path: str, hidden=False) -> list:
    """
    Gets the content of a directory with the size of each file.

    *Examples:*

    >>> get_content_with_size('C:\\Users\\User\\Desktop\\') # returns [('file1.txt', 1024), ('file2.txt', 1024), ('file3.txt', 1024)]
    >>> get_content_with_size('C:\\Users\\User\\Desktop\\', hidden=True) # returns [('file1.txt', 1024), ('file2.txt', 1024), ('file3.txt', 1024), ('.file4.txt', 1024)]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory with the size of each file.
    :rtype: list
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

def get_contents_with_size_type(path: str, hidden=False) -> list:
    """
    Gets the content of a directory with the size and type of each file.

    *Examples:*

    >>> get_content_with_size_type('C:\\Users\\User\\Desktop\\') # returns [('file1.txt', 1024, 'txt'), ('file2.txt', 1024, 'txt'), ('file3.txt', 1024, 'txt')]
    >>> get_content_with_size_type('C:\\Users\\User\\Desktop\\', hidden=True) # returns [('file1.txt', 1024, 'txt'), ('file2.txt', 1024, 'txt'), ('file3.txt', 1024, 'txt'), ('.file4.txt', 1024, 'txt')]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory with the size and type of each file.
    :rtype: list
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

def get_contents_with_size_type_date(path: str, hidden=False) -> list:
    """
    Gets the content of a directory with the size, type and date of each file.

    *Examples:*

    >>> get_content_with_size_type_date('C:\\Users\\User\\Desktop\\') # returns [('file1.txt', 1024, 'txt', 1612345678.0), ('file2.txt', 1024, 'txt', 1612345678.0), ('file3.txt', 1024, 'txt', 1612345678.0)]
    >>> get_content_with_size_type_date('C:\\Users\\User\\Desktop\\', hidden=True) # returns [('file1.txt', 1024, 'txt', 1612345678.0), ('file2.txt', 1024, 'txt', 1612345678.0), ('file3.txt', 1024, 'txt', 1612345678.0), ('.file4.txt', 1024, 'txt', 1612345678.0)]

    :param path: The path to the directory.
    :param hidden: Whether to include hidden files or not.
    :type path: str
    :return: The content of the directory with the size, type and date of each file.
    :rtype: list
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
