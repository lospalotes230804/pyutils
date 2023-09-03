"""
This file contains the test cases for the datetime module
"""

# Importing the required libraries
from datetime import datetime, timedelta, timezone
from unittest import TestCase
import src.utils.datetime.validate as dtvl
import src.utils.datetime.info as dtin


class TestDateTimeCase(TestCase):
    """
    Test class for testing directory functions
    """

    def test_parse(self):
        """
        Method to test parse function

        *Examples*:

        >>> parse("20030925T104941.5-0300") # returns datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=timezone(timedelta(seconds=-10800)))
        >>> parse("20030925T104941-0300") # returns datetime(2003, 9, 25, 10, 49, 41, tzinfo=timezone(timedelta(seconds=-10800)))
        >>> parse("20030925T104941") # returns datetime(2003, 9, 25, 10, 49, 41)
        >>> parse("20030925T1049") # returns datetime(2003, 9, 25, 10, 49)
        >>> parse("20030925T10") # returns datetime(2003, 9, 25, 10, 0)
        >>> parse("20030925") # returns datetime(2003, 9, 25, 0, 0)
        """
        self.assertEqual(dtvl.parse("20030925T104941.5-0300"), datetime(2003, 9, 25, 10,
                         49, 41, 500000, tzinfo=timezone(timedelta(seconds=-10800))))
        self.assertEqual(dtvl.parse("20030925T104941-0300"), datetime(2003, 9, 25,
                         10, 49, 41, tzinfo=timezone(timedelta(seconds=-10800))))
        self.assertEqual(dtvl.parse("20030925T104941"), datetime(2003, 9, 25, 10, 49, 41))
        self.assertEqual(dtvl.parse("20030925T1049"), datetime(2003, 9, 25, 10, 49))
        self.assertEqual(dtvl.parse("20030925T10"), datetime(2003, 9, 25, 10, 0))
        self.assertEqual(dtvl.parse("20030925"), datetime(2003, 9, 25, 0, 0))

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

        >>> is_datetime(datetime(2000, 12, 31, 23, 59, 59)) # returns True
        >>> is_datetime("2000-12-31T23:59:59") # returns False
        """
        self.assertTrue(dtvl.is_datetime(datetime(2000, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_datetime("2000-12-31T23:59:59"))

    def test_is_future(self):
        """
        Method to test is_future function

        *Examples*:

        >>> is_future(datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_future(datetime(2000, 12, 31, 23, 59, 59)) # returns False
        """
        self.assertTrue(dtvl.is_future(datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_future(datetime(2000, 12, 31, 23, 59, 59)))

    def test_is_past(self):
        """
        Method to test is_past function

        *Examples*:

        >>> is_past(datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_past(datetime(2000, 12, 31, 23, 59, 59)) # returns True
        """
        self.assertFalse(dtvl.is_past(datetime(2090, 12, 31, 23, 59, 59)))
        self.assertTrue(dtvl.is_past(datetime(2000, 12, 31, 23, 59, 59)))

    def test_is_today(self):
        """
        Method to test is_today function

        *Examples*:

        >>> is_today(datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_today(datetime.now()) # returns True
        """
        self.assertFalse(dtvl.is_today(datetime(2090, 12, 31, 23, 59, 59)))
        self.assertTrue(dtvl.is_today(datetime.now()))

    def test_is_business_day(self):
        """
        Method to test is_business_day function

        *Examples*:

        >>> is_business_day(datetime(2023, 09, 03, 23, 59, 59)) # returns False
        >>> is_business_day(datetime.now()) # returns True
        """
        self.assertFalse(dtvl.is_business_day(datetime(2023, 9, 3, 23, 59, 59)))

    def test_is_same_day(self):
        """
        Method to test is_same_day function

        *Examples*:

        >>> is_same_day(datetime(2090, 12, 31, 23, 59, 59),
                        datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_same_day(datetime(2000, 12, 31, 23, 59, 59),
                        datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_same_day(datetime.now(), datetime.now()) # returns True
        """
        self.assertTrue(dtvl.is_same_day(datetime(2090, 12, 31, 23, 59, 59),
                                         datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_day(datetime(2000, 12, 31, 23, 59, 59),
                                          datetime(2090, 12, 31, 23, 59, 59)))
        self.assertTrue(dtvl.is_same_day(datetime.now(), datetime.now()))

    def test_is_same_week(self):
        """
        Method to test is_same_week function

        *Examples*:

        >>> is_same_week(datetime(2022, 12, 30, 23, 59, 59),
                         datetime(2090, 12, 28, 23, 59, 59)) # returns True
        >>> is_same_week(datetime(2022, 12, 30, 23, 59, 59),
                         datetime(2022, 12, 15, 23, 59, 59)) # returns False
        >>> is_same_week(datetime.now(), datetime.now()) # returns True
        """
        self.assertTrue(dtvl.is_same_week(datetime(2022, 12, 30, 23, 59, 59),
                                          datetime(2090, 12, 28, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_week(datetime(2022, 12, 30, 23, 59, 59),
                                           datetime(2022, 12, 15, 23, 59, 59)))

    def test_is_same_month(self):
        """
        Method to test is_same_month function

        *Examples*:
    
        >>> is_same_month(datetime(2023, 12, 30, 23, 59, 59),
                          datetime(2023, 12, 10, 23, 59, 59)) # returns True
        >>> is_same_month(datetime(2023, 12, 30, 23, 59, 59),
                          datetime(2023, 11, 30, 23, 59, 59)) # returns False
        """
        self.assertTrue(dtvl.is_same_month(datetime(2023, 12, 30, 23, 59, 59),
                                           datetime(2023, 12, 10, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_month(datetime(2023, 12, 30, 23, 59, 59),
                                            datetime(2023, 11, 30, 23, 59, 59)))
        self.assertTrue(dtvl.is_same_month(datetime.now(), datetime.now()))

    def test_is_same_year(self):
        """
        Method to test is_same_year function

        *Examples*:

        >>> is_same_year(datetime(2090, 12, 31, 23, 59, 59),
                         datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_same_year(datetime(2000, 12, 31, 23, 59, 59),
                         datetime(2090, 12, 31, 23, 59, 59)) # returns False
        >>> is_same_year(datetime.now(), datetime.now()) # returns True
        """
        self.assertTrue(dtvl.is_same_year(datetime(2090, 12, 31, 23, 59, 59),
                                          datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_same_year(datetime(2000, 12, 31, 23, 59, 59),
                                           datetime(2090, 12, 31, 23, 59, 59)))

    def test_is_valid_range(self):
        """
        Method to test is_valid_range function

        *Examples*:

        >>> is_valid_range(datetime(2000, 12, 31, 23, 59, 59),
                           datetime(2090, 12, 31, 23, 59, 59)) # returns True
        >>> is_valid_range(datetime(2090, 12, 31, 23, 59, 59),
                           datetime(2000, 12, 31, 23, 59, 59)) # returns False
        """
        self.assertTrue(dtvl.is_valid_range(datetime(2000, 12, 31, 23, 59, 59),
                                            datetime(2090, 12, 31, 23, 59, 59)))
        self.assertFalse(dtvl.is_valid_range(datetime(2090, 12, 31, 23, 59, 59),
                                             datetime(2000, 12, 31, 23, 59, 59)))

    def test_is_leap_year(self):
        """
        Method to test is_leap_year function

        *Examples*:

        >>> is_leap_year(2000) # returns True
        >>> is_leap_year(2001) # returns False
        >>> is_leap_year(2004) # returns True
        """
        self.assertTrue(dtvl.is_leap_year(2000))
        self.assertFalse(dtvl.is_leap_year(2001))
        self.assertTrue(dtvl.is_leap_year(2004))

    # Information functions

    def test_get_timestamp(self):
        """
        Method to test get_timestamp function

        *Examples*:

        >>> get_timestamp(datetime(2020, 1, 1)) # returns 1577833200
        """
        self.assertEqual(dtin.get_timestamp(datetime(2020, 1, 1)), 1577833200)

    def test_get_time(self):
        """
        Method to test get_time function

        *Examples*:

        >>> get_time(datetime(2020, 1, 1)) # returns '00:00:00'
        """
        self.assertEqual(dtin.get_time(datetime(2020, 1, 1)), '00:00:00')

    def test_get_date(self):
        """
        Method to test get_date function

        *Examples*:

        >>> get_date(datetime(2020, 1, 1)) # returns '2020-01-01'
        """
        self.assertEqual(dtin.get_date(datetime(2020, 1, 1)), '2020-01-01')

    def test_get_timezone(self):
        """
        Method to test get_timezone function

        *Examples*:

        >>> get_timezone(datetime(2020, 1, 1)) # returns None
        >>> get_timezone(datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=1)))) # returns 'UTC+01:00'
        """
        self.assertEqual(dtin.get_timezone(datetime(2020, 1, 1)), None)
        self.assertEqual(dtin.get_timezone(datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=1)))), 'UTC+01:00')

    def test_get_age(self):
        """
        Method to test get_age function

        *Examples*:

        >>> get_age(datetime(2000, 12, 31, 23, 59, 59)) # returns 23
        >>> get_age(datetime(2090, 12, 31, 23, 59, 59)) # returns -67
        """
        self.assertEqual(dtin.get_age(datetime(2000, 12, 31, 23, 59, 59)), 23)
        self.assertEqual(dtin.get_age(datetime(2090, 12, 31, 23, 59, 59)), -67)

    def test_get_season(self):
        """
        Method to test get_season function

        *Examples*:

        >>> get_season(datetime(2020, 1, 1)) # returns 'winter'
        """
        self.assertEqual(dtin.get_season(datetime(2020, 1, 1)), 'winter')

    def test_get_quarter(self):
        """
        Method to test get_quarter function

        *Examples*:

        >>> get_quarter(datetime(2020, 1, 1)) # returns 1
        """
        self.assertEqual(dtin.get_quarter(datetime(2020, 1, 1)), 1)

    def test_get_dat_of_year(self):
        """
        Method to test get_of_year function

        *Examples*:

        >>> get_day_of_year(datetime(2020, 1, 1)) # returns 1
        """
        self.assertEqual(dtin.get_day_of_year(datetime(2020, 1, 1)), 1)

    # Processing functions
