"""
This file for testing the utility class at utils\file\
"""

# Importing the required libraries
import os
import datetime as dt
from unittest import TestCase
import src.utils.file.validate as flvl
import src.utils.file.info as flin
import src.utils.file.process as flpr
import src.utils.directory.validate as drvl
import src.utils.directory.process as drpr
# Initialize test constant variables
current_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(current_dir, "test_dir")
test_file_inside = os.path.join(test_dir, "test_file_inside.txt")
test_new_file_inside = os.path.join(test_dir, "test_new_file_inside.txt")
test_file_inside_readonly = os.path.join(test_dir, "test_file_inside_readonly.txt")
test_hidden_file_inside = os.path.join(test_dir, "test_hidden_file_inside.txt")

class TestFileCase(TestCase):
    """
    Test class for testing file functions
    """

    @classmethod
    def setUp(self):
        """
        Method to setup the test
        """
        # Delete previously created test assets
        self.delete_test_assets(self)

        # Create test assets
        self.create_test_assets(self)

        print('setUp method called!!')

    @classmethod
    def tearDown(self):
        """
        Method to clean the test
        """
        # Delete all created test assets
        self.delete_test_assets(self)

        print('tearDown method called!!')

    def delete_test_assets(self):
        """
        Method to delete test assets
        """
        # Delete all created test assets
        # Delete test_dir if exists, empty it first
        drpr.delete(test_dir)

    def create_test_assets(self):
        """
        Method to create all test assets
        """

        # now create it
        drpr.create(test_dir)

        # create a file inside the directory
        flpr.create(test_file_inside)
        flpr.write(test_file_inside, "test")

        # create a hidden file inside the directory
        flpr.create(test_hidden_file_inside)
        flpr.write(test_hidden_file_inside, "test")
        flpr.set_hidden(test_hidden_file_inside)

        # create a readonly file inside the directory
        flpr.create(test_file_inside_readonly)
        flpr.write(test_file_inside_readonly, "test")
        flpr.set_readonly(test_file_inside_readonly)

    # File validation functions

    def test_exists(self):
        """
        Method to test if the given file path points to an existing file

        *Examples:*

        >>> flvl.exists("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file exists
        >>> flvl.exists("C:\\Users\\user\\Desktop\\test") # returns false if the file does not exist
        """
        self.assertTrue(flvl.exists(test_file_inside))
        flpr.delete(test_file_inside)
        self.assertFalse(flvl.exists(test_file_inside))

    def test_is_file(self):
        """
        Method to test if the given file path points to a file

        *Examples:*

        >>> flvl.is_file("C:\\Users\\user\\Desktop\\test.txt") # returns true if the path points to a file
        >>> flvl.is_file("C:\\Users\\user\\Desktop\\test") # returns false if the path does not point to a file
        """
        self.assertTrue(flvl.is_file(test_file_inside))
        self.assertFalse(flvl.is_file(test_dir))

    def test_is_empty(self):
        """
        Method to test if the given file path points to an empty file

        *Examples:*

        >>> flvl.is_empty("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file is empty
        >>> flvl.is_empty("C:\\Users\\user\\Desktop\\test.txt") # returns false if the file is not empty
        """
        self.assertFalse(flvl.is_empty(test_file_inside))
        flpr.empty(test_file_inside)
        self.assertTrue(flvl.is_empty(test_file_inside))

    def test_is_hidden_visible(self):
        """
        Method to test if the given file path points to a hidden file

        *Examples:*

        >>> flvl.is_hidden("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file is hidden
        >>> flvl.is_hidden("C:\\Users\\user\\Desktop\\test") # returns false if the file is not hidden
        """
        self.assertFalse(flvl.is_hidden(test_file_inside))
        self.assertTrue(flvl.is_hidden(test_hidden_file_inside))

    def test_is_readonly_or_not(self):
        """
        Method to test if the given file path points to a readonly file

        *Examples:*

        >>> flvl.is_readonly("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file is readonly
        >>> flvl.is_readonly("C:\\Users\\user\\Desktop\\test") # returns false if the file is not readonly
        """
        self.assertFalse(flvl.is_readonly(test_file_inside))
        self.assertTrue(flvl.is_readonly(test_file_inside_readonly))

    # def test_is_readable(self):
        """
        Method to test if the given file path points to a readable file

        *Examples:*

        >>> flvl.is_readable("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file is readable
        >>> flvl.is_readable("C:\\Users\\user\\Desktop\\test") # returns false if the file is not readable
        """
        # self.assertTrue(flvl.is_readable(test_file_inside))
        # self.assertTrue(flvl.is_writable(test_file_inside))
        # flpr.set_readable(test_file_inside)
        # self.assertFalse(flvl.is_readable(test_file_inside))

    # def test_is_writable(self):
        """
        Method to test if the given file path points to a writable file

        *Examples:*

        >>> flvl.is_writable("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file is writable
        >>> flvl.is_writable("C:\\Users\\user\\Desktop\\test") # returns false if the file is not writable
        """
        # self.assertTrue(flvl.is_writable(test_file_inside))
        # flpr.set_readonly(test_file_inside)
        # self.assertFalse(flvl.is_writable(test_file_inside))

    # def test_is_executable(self):
        """
        Method to test if the given file path points to an executable file

        *Examples:*

        >>> flvl.is_executable("C:\\Users\\user\\Desktop\\test.txt") # returns true if the file is executable
        >>> flvl.is_executable("C:\\Users\\user\\Desktop\\test") # returns false if the file is not executable
        """
        # self.assertFalse(flvl.is_executable(test_file_inside))

    # Information functions

    def test_get_size(self):
        """
        Method to test get_size function

        *Examples:*

        >>> get_size('C:\\Users\\User\\Desktop\\file.txt') # returns the size of the file in bytes
        """
        self.assertEqual(flin.get_size(test_file_inside), 4)

    def test_get_name(self):
        """
        Method to test get_name function

        *Examples:*

        >>> get_name('C:\\Users\\User\\Desktop\\file.txt') # returns the name of the file
        """
        self.assertEqual(flin.get_filename(test_file_inside), "test_file_inside.txt")

    def test_get_relative_path(self):
        """
        Method to test get_relative_path function

        *Examples:*

        >>> get_relative_path('C:\\Users\\User\\Desktop\\file.txt') # returns the relative path of the file
        """
        self.assertEqual(flin.get_relative_path(test_file_inside), "tests\\test_dir\\test_file_inside.txt")

    def test_get_absolute_path(self):
        """
        Method to test get_absolute_path function

        *Examples:*

        >>> get_absolute_path('C:\\Users\\User\\Desktop\\file.txt') # returns the absolute path of the file
        """
        self.assertEqual(flin.get_absolute_path(test_file_inside), test_file_inside)

    def test_get_parent_dir(self):
        """
        Method to test get_parent_dir function

        *Examples:*

        >>> get_parent_dir('C:\\Users\\User\\Desktop\\file.txt') # returns the parent directory of the file
        """
        self.assertEqual(flin.get_parent_dir(test_file_inside), test_dir)

    def test_get_extension(self):
        """
        Method to test get_extension function

        *Examples:*

        >>> get_extension('C:\\Users\\User\\Desktop\\file.txt') # returns the extension of the file
        """
        self.assertEqual(flin.get_extension(test_file_inside), "txt")

    def test_get_creation_datetime(self):
        """
        Method to test get_creation_datetime function

        *Examples:*

        >>> get_creation_datetime('C:\\Users\\User\\Desktop\\file.txt') # returns the creation datetime of the file
        """
        # Check that creation time is with the last 10 secons from now
        self.assertTrue(flin.get_creation_datetime(test_file_inside) - dt.datetime.now() < dt.timedelta(seconds=10))

    def test_get_modification_datetime(self):
        """
        Method to test get_modification_datetime function

        *Examples:*

        >>> get_modification_datetime('C:\\Users\\User\\Desktop\\file.txt') # returns the modification datetime of the file
        """
        # Check that modification time is with the last 10 secons from now
        self.assertTrue(flin.get_modification_datetime(test_file_inside) - dt.datetime.now() < dt.timedelta(seconds=10))

    def test_get_access_datetime(self):
        """
        Method to test get_access_datetime function

        *Examples:*

        >>> get_access_datetime('C:\\Users\\User\\Desktop\\file.txt') # returns the access datetime of the file
        """
        # Check that access time is with the last 10 secons from now
        self.assertTrue(flin.get_access_datetime(test_file_inside) - dt.datetime.now() < dt.timedelta(seconds=10))

    def test_get_owner(self):
        """
        Method to test get_owner function

        *Examples:*

        >>> get_owner('C:\\Users\\User\\Desktop\\file.txt') # returns the owner of the file
        """
        self.assertEqual(flin.get_owner(test_file_inside), os.getlogin())

    def test_get_group(self):
        """
        Method to test get_group function

        *Examples:*

        >>> get_group('C:\\Users\\User\\Desktop\\file.txt') # returns the group of the file
        """
        self.assertEqual(flin.get_group(test_file_inside), os.getlogin())

    # def test_get_encoding(self):

    # Processing functions

    def test_create(self):
        """
        Method to test create function

        *Examples:*

        >>> create('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was created successfully
        >>> create('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not created successfully
        """
        self.assertTrue(flpr.create(test_new_file_inside))

    def test_delete(self):
        """
        Method to test delete function

        *Examples:*

        >>> delete('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was deleted successfully
        >>> delete('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not deleted successfully
        """
        self.assertTrue(flpr.delete(test_file_inside))

    def test_empty(self):
        """
        Method to test empty function

        *Examples:*

        >>> empty('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was emptied successfully
        >>> empty('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not emptied successfully
        """
        self.assertTrue(flpr.empty(test_file_inside))

    def test_read(self):
        """
        Method to test read function

        *Examples:*

        >>> read('C:\\Users\\User\\Desktop\\file.txt') # returns the contents of the file
        """
        self.assertEqual(flpr.read(test_file_inside), "test")

    def test_write(self):
        """
        Method to test write function

        *Examples:*

        >>> write('C:\\Users\\User\\Desktop\\file.txt', 'test') # returns True if the file was written successfully
        >>> write('C:\\Users\\User\\Desktop\\file.txt', 'test') # returns False if the file was not written successfully
        """
        flpr.write(test_file_inside, "test2")
        self.assertEqual(flpr.read(test_file_inside), "test2")

    def test_rename(self):
        """
        Method to test rename function

        *Examples:*

        >>> rename('C:\\Users\\User\\Desktop\\file.txt', 'file2.txt') # returns True if the file was renamed successfully
        >>> rename('C:\\Users\\User\\Desktop\\file.txt', 'file2.txt') # returns False if the file was not renamed successfully
        """
        new_file_path = flpr.rename(test_file_inside, "test_file_inside2.txt")
        self.assertEqual(new_file_path, os.path.join(test_dir, "test_file_inside2.txt"))

    def test_copy(self):
        """
        Method to test copy function

        *Examples:*

        >>> copy('C:\\Users\\User\\Desktop\\file.txt', 'C:\\Users\\User\\Desktop\\file2.txt') # returns True if the file was copied successfully
        >>> copy('C:\\Users\\User\\Desktop\\file.txt', 'C:\\Users\\User\\Desktop\\file2.txt') # returns False if the file was not copied successfully
        """
        new_file_path = flpr.copy(test_file_inside, os.path.join(test_dir, "test_file_inside2.txt"))
        self.assertEqual(new_file_path, os.path.join(test_dir, "test_file_inside2.txt"))

    def test_duplicate(self):
        """
        Method to test duplicate function

        *Examples:*

        >>> duplicate('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was duplicated successfully
        >>> duplicate('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not duplicated successfully
        """
        new_file_path = flpr.duplicate(test_file_inside)
        self.assertEqual(new_file_path, os.path.join(test_dir, "test_file_inside (1).txt"))
        new_file_path = flpr.duplicate(test_file_inside)
        self.assertEqual(new_file_path, os.path.join(test_dir, "test_file_inside (2).txt"))

    # def test_move(self):

    def test_set_hidden(self):
        """
        Method to test set_hidden function

        *Examples:*

        >>> set_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was hidden successfully
        >>> set_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not hidden successfully
        """
        self.assertTrue(flpr.set_hidden(test_file_inside))

    def test_set_visible(self):
        """
        Method to test set_visible function

        *Examples:*

        >>> set_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was made visible successfully
        >>> set_hidden('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not made visible successfully
        """
        self.assertTrue(flpr.set_visible(test_hidden_file_inside))

    def test_set_readonly(self):
        """
        Method to test set_readonly function

        *Examples:*

        >>> set_readonly('C:\\Users\\User\\Desktop\\file.txt') # returns True if the file was made readonly successfully
        >>> set_readonly('C:\\Users\\User\\Desktop\\file.txt') # returns False if the file was not made readonly successfully
        """
        self.assertTrue(flpr.set_readonly(test_file_inside))
