"""
This file contains the test cases for the datetime module
"""

# Importing the required libraries
import datetime as dt
from unittest import TestCase
import src.utils.datetime.validate as dtvl


class TestDateTimeCase(TestCase):
    """
    Test class for testing directory functions
    """

    def test_parse(self):
        """
        Method to test parse function

        *Examples*:

        >>> parse("20030925T104941.5-0300") # returns datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=dt.timezone(dt.timedelta(seconds=-10800)))
        >>> parse("20030925T104941-0300") # returns datetime(2003, 9, 25, 10, 49, 41, tzinfo=dt.timezone(dt.timedelta(seconds=-10800)))
        >>> parse("20030925T104941") # returns datetime(2003, 9, 25, 10, 49, 41)
        >>> parse("20030925T1049") # returns datetime(2003, 9, 25, 10, 49)
        >>> parse("20030925T10") # returns datetime(2003, 9, 25, 10, 0)
        >>> parse("20030925") # returns datetime(2003, 9, 25, 0, 0)
        """
        self.assertEqual(dtvl.parse("20030925T104941.5-0300"), dt.datetime(2003, 9, 25, 10,
                         49, 41, 500000, tzinfo=dt.timezone(dt.timedelta(seconds=-10800))))
        self.assertEqual(dtvl.parse("20030925T104941-0300"), dt.datetime(2003, 9, 25,
                         10, 49, 41, tzinfo=dt.timezone(dt.timedelta(seconds=-10800))))
        self.assertEqual(dtvl.parse("20030925T104941"), dt.datetime(2003, 9, 25, 10, 49, 41))
        self.assertEqual(dtvl.parse("20030925T1049"), dt.datetime(2003, 9, 25, 10, 49))
        self.assertEqual(dtvl.parse("20030925T10"), dt.datetime(2003, 9, 25, 10, 0))
        self.assertEqual(dtvl.parse("20030925"), dt.datetime(2003, 9, 25, 0, 0))

    def test_is_parseable(self):
        """
        Method to test is_parseable function
        *Examples*:
        >>> is_parseable("20030925T104941.5-0300") # returns True
        >>> is_parseable("20030925T104941-0300") # returns True
        >>> is_parseable("invalid_datetime") # returns False
        """
        self.assertTrue(dtvl.is_parseable("20030925T104941.5-0300"))
        self.assertTrue(dtvl.is_parseable("20030925T104941-0300"))
        self.assertFalse(dtvl.is_parseable("invalid_datetime"))

    def test_is_datetime(self):
        """
        Method to test is_datetime function

        *Examples*:

        >>> is_datetime(dt.datetime(2000, 12, 31, 23, 59, 59)) # returns True
        >>> is_datetime("2000-12-31T23:59:59") # returns False
        """
        self.assertTrue(dtvl.is_datetime(dt.datetime(2000, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_datetime("2000-12-31T23:59:59"))

    def test_is_future(self):
        """
        Method to test is_future function

        *Examples*:

        >>> is_future(dt.datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_future(dt.datetime(2000, 12, 31, 23, 59, 59)) # returns False
        """
        self.assertTrue(dtvl.is_future(dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_future(dt.datetime(2000, 12, 31, 23, 59, 59)))

    def test_is_past(self):
        """
        Method to test is_past function

        *Examples*:

        >>> is_past(dt.datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_past(dt.datetime(2000, 12, 31, 23, 59, 59)) # returns True
        """
        self.assertFalse(dtvl.is_past(dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertTrue(dtvl.is_past(dt.datetime(2000, 12, 31, 23, 59, 59)))

    def test_is_today(self):
        """
        Method to test is_today function

        *Examples*:

        >>> is_today(dt.datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_today(datetime.now()) # returns True
        """
        self.assertFalse(dtvl.is_today(dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertTrue(dtvl.is_today(dt.datetime.now()))

    def test_is_business_day(self):
        """
        Method to test is_business_day function

        *Examples*:

        >>> is_business_day(dt.datetime(2023, 09, 03, 23, 59, 59)) # returns False
        >>> is_business_day(datetime.now()) # returns True
        """
        self.assertFalse(dtvl.is_business_day(dt.datetime(2023, 9, 3, 23, 59, 59)))

    def test_is_same_day(self):
        """
        Method to test is_same_day function

        *Examples*:

        >>> is_same_day(dt.datetime(2090, 12, 31, 23, 59, 59),
                        dt.datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_same_day(dt.datetime(2000, 12, 31, 23, 59, 59),
                        dt.datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_same_day(datetime.now(), datetime.now()) # returns True
        """
        self.assertTrue(dtvl.is_same_day(dt.datetime(2090, 12, 31, 23, 59, 59),
                                         dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_day(dt.datetime(2000, 12, 31, 23, 59, 59),
                                          dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertTrue(dtvl.is_same_day(dt.datetime.now(), dt.datetime.now()))

    def test_is_same_week(self):
        """
        Method to test is_same_week function

        *Examples*:

        >>> is_same_week(dt.datetime(2022, 12, 30, 23, 59, 59),
                         dt.datetime(2090, 12, 28, 23, 59, 59)) # returns True
        >>> is_same_week(dt.datetime(2022, 12, 30, 23, 59, 59),
                         dt.datetime(2022, 12, 15, 23, 59, 59)) # returns False
        >>> is_same_week(datetime.now(), datetime.now()) # returns True
        """
        self.assertTrue(dtvl.is_same_week(dt.datetime(2022, 12, 30, 23, 59, 59),
                                          dt.datetime(2090, 12, 28, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_week(dt.datetime(2022, 12, 30, 23, 59, 59),
                                           dt.datetime(2022, 12, 15, 23, 59, 59)))

    def test_is_same_month(self):
        """
        Method to test is_same_month function

        *Examples*:
    
        >>> is_same_month(dt.datetime(2023, 12, 30, 23, 59, 59),
                          dt.datetime(2023, 12, 10, 23, 59, 59)) # returns True
        >>> is_same_month(dt.datetime(2023, 12, 30, 23, 59, 59),
                          dt.datetime(2023, 11, 30, 23, 59, 59)) # returns False
        """
        self.assertTrue(dtvl.is_same_month(dt.datetime(2023, 12, 30, 23, 59, 59),
                                           dt.datetime(2023, 12, 10, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_month(dt.datetime(2023, 12, 30, 23, 59, 59),
                                            dt.datetime(2023, 11, 30, 23, 59, 59)))
        self.assertTrue(dtvl.is_same_month(dt.datetime.now(), dt.datetime.now()))

    def test_is_same_year(self):
        """
        Method to test is_same_year function

        *Examples*:

        >>> is_same_year(dt.datetime(2090, 12, 31, 23, 59, 59),
                         dt.datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_same_year(dt.datetime(2000, 12, 31, 23, 59, 59),
                         dt.datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_same_year(datetime.now(), datetime.now()) # returns True
        """
        self.assertTrue(dtvl.is_same_year(dt.datetime(2090, 12, 31, 23, 59, 59),
                                          dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_year(dt.datetime(2000, 12, 31, 23, 59, 59),
                                           dt.datetime(2090, 12, 31, 23, 59, 59)))

    def test_is_valid_range(self):
        """
        Method to test is_valid_range function

        *Examples*:

        >>> is_valid_range(dt.datetime(2000, 12, 31, 23, 59, 59),
                           dt.datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_valid_range(dt.datetime(2090, 12, 31, 23, 59, 59),
                           dt.datetime(2000, 12, 31, 23, 59, 59)) # returns False
        """
        self.assertTrue(dtvl.is_valid_range(dt.datetime(2000, 12, 31, 23, 59, 59),
                                            dt.datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_valid_range(dt.datetime(2090, 12, 31, 23, 59, 59),
                                             dt.datetime(2000, 12, 31, 23, 59, 59)))



