"""
This file for testing the utility class at utils\directory\
"""

# Importing the required libraries
import os
import datetime as dt
from unittest import TestCase
import src.utils.file.process as flpr
import src.utils.directory.info as drin
import src.utils.directory.validate as drvl
import src.utils.directory.process as drpr
# import src.utils.datetime.validate as dtvl

# Initialize test constant variables
current_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(current_dir, "test_dir")
test_dir_inside = os.path.join(test_dir, "test_dir_inside")
test_file_inside = os.path.join(test_dir, "test_file_inside.txt")
test_file_inside_inside = os.path.join(test_dir_inside, "test_file_inside.txt")
test_hidden_dir_inside = os.path.join(test_dir, "test_hidden_dir_inside")
test_hidden_file_inside = os.path.join(test_dir, "test_hidden_file_inside.txt")
test_hidden_file_inside_inside = os.path.join(test_hidden_dir_inside, "test_hidden_file_inside.txt")

class TestDirCase(TestCase):
    """
    Test class for testing directory functions
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

        # create a dir inside the directory
        drpr.create(test_dir_inside)

        # create a file inside the directory
        flpr.create(test_file_inside)
        flpr.write(test_file_inside, "test")
        flpr.create(test_file_inside_inside)
        flpr.write(test_file_inside_inside, "test")

        # create a hidden dir inside the directory
        drpr.create(test_hidden_dir_inside)
        drpr.set_hidden(test_hidden_dir_inside)

        # create a hidden file inside the directory
        flpr.create(test_hidden_file_inside)
        flpr.write(test_hidden_file_inside, "test")
        flpr.set_hidden(test_hidden_file_inside)

        # create a hidden file inside the hidden directory
        flpr.create(test_hidden_file_inside_inside)
        flpr.write(test_hidden_file_inside_inside, "test")
        flpr.set_hidden(test_hidden_file_inside_inside)

    # Directory validation functions

    def test_exists(self):
        """
        Method to test exists function

        *Examples:*

        >>> exists('C:\\Users\\User\\Desktop\\directory') # returns True if the directory exists
        >>> exists('C:\\Users\\User\\Desktop\\directory') # returns False if the directory does not exists
        """
        # Test exists function
        self.assertTrue(drvl.exists(test_dir))
        self.assertFalse(drvl.exists(os.path.join(test_dir, "test_dir_not_exists")))

    def test_is_dir(self):
        """
        Method to test is_dir function

        *Examples:*

        >>> is_dir('C:\\Users\\User\\Desktop\\directory') # returns True
        >>> is_dir('C:\\Users\\User\\Desktop\\directory\\test_file.txt') # returns False
        """
        # Test is_dir function
        self.assertTrue(drvl.is_dir(test_dir))
        self.assertFalse(drvl.is_dir(os.path.join(test_dir, test_file_inside)))

    def test_is_empty(self):
        """
        Method to test is_empty function

        *Examples:*

        >>> is_empty('C:\\Users\\User\\Desktop\\directory') # returns True if the directory is empty
        >>> is_empty('C:\\Users\\User\\Desktop\\directory') # returns False if the directory is not empty
        """
        self.assertFalse(drvl.is_empty(test_dir))
        drpr.empty(test_dir)
        self.assertTrue(drvl.is_empty(test_dir))

    def test_is_hidden_or_not(self):
        """
        Method to test is_hidden function

        *Examples:*

        >>> is_hidden('C:\\Users\\User\\Desktop\\directory') # returns True if the directory is hidden
        >>> is_hidden('C:\\Users\\User\\Desktop\\directory') # returns False if the directory is not hidden
        """
        self.assertTrue(drvl.is_hidden(test_hidden_dir_inside))
        self.assertFalse(drvl.is_hidden(test_dir_inside))

    # Information functions

    def test_get_size(self):
        """
        Method to test get_size function

        *Examples:*

        >>> get_size('C:\\Users\\User\\Desktop\\directory') # returns 0 if the directory is empty
        >>> get_size('C:\\Users\\User\\Desktop\\directory') # returns 1024 if the directory is not empty
        """
        self.assertEqual(drin.get_size(test_dir), 8)

    def test_get_name(self):
        """
        Method to test get_name function

        *Examples:*

        >>> get_name('C:\\Users\\User\\Desktop\\directory') # returns 'directory'
        """
        self.assertEqual(drin.get_name(test_dir), "test_dir")

    def test_get_relative_path(self):
        """
        Method to test get_relative_path function

        *Examples:*

        >>> get_relative_path('C:\\Users\\User\\Desktop\\directory') # returns 'directory'
        """
        self.assertEqual(drin.get_relative_path(test_dir), os.path.join(os.path.basename(current_dir), "test_dir"))

    def test_get_absolute_path(self):
        """
        Method to test get_absolute_path function

        *Examples:*

        >>> get_absolute_path('C:\\Users\\User\\Desktop\\directory') # returns 'directory'
        """
        self.assertEqual(drin.get_absolute_path(test_dir), os.path.join(current_dir, "test_dir"))

    def test_get_parent_dir(self):
        """
        Method to test get_parent_dir function

        *Examples:*

        >>> get_parent_dir('C:\\Users\\User\\Desktop\\directory') # returns 'C:\\Users\\User\\Desktop'
        """
        self.assertEqual(drin.get_parent_dir(test_dir), os.path.dirname(test_dir))

    def test_get_contents(self):
        """
        Method to test get_contents function

        *Examples:*

        >>> get_content('C:\\Users\\User\\Desktop\\')              # returns ['file.txt', '\\dir_inside\file.txt']
        >>> get_content('C:\\Users\\User\\Desktop\\', hidden=True) # returns ['file.txt', 'hidden_file.txt', 'hidden_dir', '\\dir_inside\file.txt', '\\dir_inside\hidden_file.txt']
        """
        # Test get_contents function with hidden files and directories
        dir_contents = drin.get_contents(test_dir, True)
        self.assertEqual(dir_contents, [
            os.path.join(test_dir, "test_file_inside.txt"),
            os.path.join(test_dir, "test_hidden_dir_inside"),
            os.path.join(test_dir, "test_hidden_file_inside.txt"),
            os.path.join(test_dir, "test_dir_inside"),
            os.path.join(test_dir, "test_dir_inside\\test_file_inside.txt"),
            os.path.join(test_dir, "test_hidden_dir_inside\\test_hidden_file_inside.txt")
        ])

    def test_get_creation_datetime(self):
        """
        Method to test get_creation_datetime function

        *Examples:*

        >>> get_creation_datetime('C:\\Users\\User\\Desktop\\directory') # returns datetime.datetime(2019, 1, 1, 0, 0, 0)
        """
        # Check that creation time is with the last 10 secons from now
        self.assertTrue(drin.get_creation_datetime(test_dir) - dt.datetime.now() < dt.timedelta(seconds=10))

    def test_get_modification_datetime(self):
        """
        Method to test get_modification_datetime function

        *Examples:*

        >>> get_modification_datetime('C:\\Users\\User\\Desktop\\directory') # returns datetime.datetime(2019, 1, 1, 0, 0, 0)
        """
        # Check that creation time is with the last 10 secons from now
        self.assertTrue(drin.get_modification_datetime(test_dir) - dt.datetime.now() < dt.timedelta(seconds=10))

    def test_get_access_datetime(self):
        """
        Method to test get_access_datetime function

        *Examples:*

        >>> get_access_datetime('C:\\Users\\User\\Desktop\\directory') # returns datetime.datetime(2019, 1, 1, 0, 0, 0)
        """
        # Check that creation time is with the last 10 secons from now
        self.assertTrue(drin.get_access_datetime(test_dir) - dt.datetime.now() < dt.timedelta(seconds=10))

    def test_get_owner(self):
        """
        Method to test get_owner function

        *Examples:*

        >>> get_owner('C:\\Users\\User\\Desktop\\directory') # returns 'User'
        """
        self.assertEqual(drin.get_owner(test_dir), os.getlogin())


    # Processing functions

    def test_create(self):
        """
        Method to test create function

        *Examples:*

        >>> create('C:\\Users\\User\\Desktop\\directory') # returns True if the directory was created successfully
        >>> create('C:\\Users\\User\\Desktop\\directory') # returns False if the directory was not created successfully
        """
        # Test create function
        self.assertTrue(drpr.create((test_dir_inside.replace("\\test_dir_inside", "\\test_dir_inside_2"))))

    def test_delete(self):
        """
        Method to test delete function

        *Examples:*

        >>> delete('C:\\Users\\User\\Desktop\\directory') # returns True if the directory was deleted successfully
        >>> delete('C:\\Users\\User\\Desktop\\directory') # returns False if the directory was not deleted successfully
        """
        # Test delete function
        self.assertTrue(drpr.delete((test_dir_inside)))

    def test_empty(self):
        """
        Method to test empty function

        *Examples:*

        >>> empty('C:\\Users\\User\\Desktop\\directory') # returns True if emptied successfully
        >>> empty('C:\\Users\\User\\Desktop\\directory') # returns False if not emptied successfully
        """
        # Test empty function
        self.assertTrue(drpr.empty((test_dir_inside)))

    def test_rename(self):
        """
        Method to test rename function

        *Examples:*

        >>> rename('C:\\Users\\User\\Desktop\\directory', 'new_name') # returns True if renamed successfully
        >>> rename('C:\\Users\\User\\Desktop\\directory', 'new_name') # returns False if not renamed successfully
        """
        # Test rename function
        self.assertEqual(drpr.rename(test_dir_inside, test_dir_inside.replace("\\test_dir_inside", "\\test_dir_inside_renamed")),
                         os.path.join(test_dir, "test_dir_inside_renamed"))

    def test_copy(self):
        """
        Method to test copy function

        *Examples:*

        >>> copy('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\directory') # returns True if copied successfully
        >>> copy('C:\\Users\\User\\Desktop\\directory', 'C:\\Users\\User\\Desktop\\directory') # returns False if not copied successfully
        """
        # Test copy function
        self.assertTrue(drpr.copy(test_dir_inside, test_dir_inside.replace("\\test_dir_inside", "\\test_dir_inside_copied")))

    def test_duplicate(self):
        """
        Method to test duplicate function

        *Examples:*

        >>> duplicate('C:\\Users\\User\\Desktop\\directory') # returns True if duplicated successfully
        >>> duplicate('C:\\Users\\User\\Desktop\\directory') # returns False if not duplicated successfully
        """
        # Test duplicate function
        self.assertTrue(drpr.duplicate(test_dir_inside))
        self.assertTrue(drpr.duplicate(test_dir_inside))

    # def test_move(self):

    def test_set_hidden(self):
        """
        Method to test set_hidden function

        *Examples:*

        >>> set_hidden('C:\\Users\\User\\Desktop\\directory') # returns True if the directory was hidden successfully
        >>> set_hidden('C:\\Users\\User\\Desktop\\directory') # returns False if the directory was not hidden successfully
        """
        self.assertTrue(drpr.set_hidden(test_dir_inside))

    def test_set_visible(self):
        """
        Method to test set_visible function

        *Examples:*

        >>> set_hidden('C:\\Users\\User\\Desktop\\directory') # returns True if the directory was hidden successfully
        >>> set_hidden('C:\\Users\\User\\Desktop\\directory') # returns False if the directory was not hidden successfully
        """
        self.assertTrue(drvl.is_hidden(test_hidden_dir_inside))
        self.assertTrue(drpr.set_visible(test_hidden_dir_inside))
        self.assertFalse(drvl.is_hidden(test_hidden_dir_inside))

    def test_set_readonly(self):
        """
        Method to test set_readonly function

        *Examples:*

        >>> set_readonly('C:\\Users\\User\\Desktop\\directory') # returns True if the directory was set as readonly successfully
        >>> set_readonly('C:\\Users\\User\\Desktop\\directory') # returns False if the directory was not set as readonly successfully
        """
        self.assertTrue(drvl.is_writable(test_dir_inside))
        # self.assertTrue(drpr.set_readonly(test_dir_inside))



