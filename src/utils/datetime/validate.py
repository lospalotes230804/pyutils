"""
This file contains functions for datetime validation.
Inspired by
https://github.com/dateutil/dateutil/blob/master/src/dateutil/parser/_parser.py
https://dateutil.readthedocs.io/en/stable/examples.html#parse-examples
"""

# Importing the required libraries
import dateutil.parser as dtp
from datetime import datetime
from src.utils.string.validate import is_string


def parse(input_string: str) -> datetime:
    """
    Parses a string into a datetime object.

    *Examples*:

    ISO format, without separators:
    >>> parse("20030925T104941.5-0300") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=tzoffset(None, -10800))
    >>> parse("20030925T104941-0300") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, tzinfo=tzoffset(None, -10800))
    >>> parse("20030925T104941") # returns datetime.datetime(2003, 9, 25, 10, 49, 41)
    >>> parse("20030925T1049") # returns datetime.datetime(2003, 9, 25, 10, 49)
    >>> parse("20030925T10") # returns datetime.datetime(2003, 9, 25, 10, 0)
    >>> parse("20030925") # returns datetime.datetime(2003, 9, 25, 0, 0)

    Everything together:

    >>> parse("199709020900") # returns datetime.datetime(1997, 9, 2, 9, 0)
    >>> parse("19970902090059") # returns datetime.datetime(1997, 9, 2, 9, 0, 59)

    Different date orderings:

    >>> parse("2003-09-25") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("2003-Sep-25") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("25-Sep-2003") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("Sep-25-2003") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("09-25-2003") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("25-09-2003") # returns datetime.datetime(2003, 9, 25, 0, 0)

    Check some ambiguous dates:
    >>> parse("10-09-2003") # returns datetime.datetime(2003, 10, 9, 0, 0)
    >>> parse("10-09-2003", dayfirst=True) # returns datetime.datetime(2003, 9, 10, 0, 0)
    >>> parse("10-09-03") # returns datetime.datetime(2003, 10, 9, 0, 0)
    >>> parse("10-09-03", yearfirst=True) # returns datetime.datetime(2010, 9, 3, 0, 0)

    Other date separators are allowed:

    >>> parse("2003.Sep.25") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("2003/09/25") # returns datetime.datetime(2003, 9, 25, 0, 0)

    Even with spaces:

    >>> parse("2003 Sep 25") # returns datetime.datetime(2003, 9, 25, 0, 0)
    >>> parse("2003 09 25") # returns datetime.datetime(2003, 9, 25, 0, 0)

    Hours with letters work:

    >>> parse("10h36m28.5s", default=DEFAULT) # returns datetime.datetime(2003, 9, 25, 10, 36, 28, 500000)
    >>> parse("01s02h03m", default=DEFAULT) # returns datetime.datetime(2003, 9, 25, 2, 3, 1)
    >>> parse("01h02m03", default=DEFAULT) # returns datetime.datetime(2003, 9, 25, 1, 2, 3)
    >>> parse("01h02", default=DEFAULT) # returns datetime.datetime(2003, 9, 25, 1, 2)
    >>> parse("01h02s", default=DEFAULT) # returns datetime.datetime(2003, 9, 25, 1, 0, 2)

    Timezones work too:

    >>> parse("2003-09-25T10:49:41.5-03:00") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=tzoffset(None, -10800))
    >>> parse("2003-09-25T10:49:41-03:00") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, tzinfo=tzoffset(None, -10800))
    >>> parse("2003-09-25T10:49:41") # returns datetime.datetime(2003, 9, 25, 10, 49, 41)
    >>> parse("2003-09-25T10:49") # returns datetime.datetime(2003, 9, 25, 10, 49)
    >>> parse("2003-09-25T10") # returns datetime.datetime(2003, 9, 25, 10, 0)
    >>> parse("2003-09-25") # returns datetime.datetime(2003, 9, 25, 0, 0)

    >>> parse("2003-09-25T10:49:41.5Z") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=tzutc())
    >>> parse("2003-09-25T10:49:41Z") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, tzinfo=tzutc())
    >>> parse("2003-09-25T10:49Z") # returns datetime.datetime(2003, 9, 25, 10, 49, tzinfo=tzutc())
    >>> parse("2003-09-25T10Z") # returns datetime.datetime(2003, 9, 25, 10, 0, tzinfo=tzutc())
    >>> parse("2003-09-25Z") # returns datetime.datetime(2003, 9, 25, 0, 0, tzinfo=tzutc())

    :param input_string: String to parse
    :return: datetime object
    """
    return dtp.parse(input_string)

def is_parseable(input_string: str) -> bool:
    """
    Checks if a string is parseable into a datetime object.
    If it is not parseable, it returns False.
    If it is parseable, it returns True.

    *Examples*:

    >>> is_parseable("20030925T104941.5-0300") # returns True
    >>> is_parseable("20030925T104941-0300") # returns True

    :param input_string: String to parse
    :return: True if the string is parseable, False otherwise.
    :rtype: bool
    """
    try:
        dt_object = parse(input_string)
        return isinstance(dt_object, datetime)
    except ValueError as e:
        print(e)
        return False
    
def str_to_datetime(input_string) -> datetime:
    """
    Converts a string into a datetime object.
    If it is not parseable, it returns None.
    
    *Examples*:

    >>> str_to_datetime("20030925T104941.5-0300") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=tzoffset(None, -10800))
    >>> str_to_datetime("20030925T104941-0300") # returns datetime.datetime(2003, 9, 25, 10, 49, 41, tzinfo=tzoffset(None, -10800))
    >>> str_to_datetime("20030925T104941") # returns datetime.datetime(2003, 9, 25, 10, 49, 41)
    >>> str_to_datetime("20030925T1049") # returns datetime.datetime(2003, 9, 25, 10, 49)

    :param input_string: String to parse
    :return: datetime object
    :rtype: datetime
    """
    if is_string(input_string):
        try:
            dt_object = parse(input_string)
            if isinstance(dt_object, datetime):
                return dt_object
            else:
                return None
        except ValueError as e:
            print(e)
            return None
    
def is_datetime(object) -> bool:
    """
    Checks if an object is a datetime object.

    *Examples*:

    >>> is_datetime(datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_datetime(datetime(2000, 12, 31, 23, 59, 59)) # returns True
    >>> is_datetime("2000-12-31T23:59:59") # returns False

    :param object: object to check
    :return: True if the object is a datetime object, False otherwise.
    :rtype: bool
    """
    try:
        return isinstance(object, datetime)
    except ValueError as e:
        print(e)
        return False

def is_future(date: datetime) -> bool:
    """
    Checks if a datetime object is in the future.

    *Examples*:

    >>> is_future(datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_future(datetime(2000, 12, 31, 23, 59, 59)) # returns False

    :param date: datetime object
    :return: True if the date is in the future, False otherwise.
    :rtype: bool
    """
    if is_datetime(date):
        return date > datetime.now()
    else:
        return False

def is_past(date: datetime) -> bool:
    """
    Checks if a datetime object is in the past.

    *Examples*:

    >>> is_past(datetime(2090, 12, 31, 23, 59, 59)) # returns False
    >>> is_past(datetime(2000, 12, 31, 23, 59, 59)) # returns True

    :param date: datetime object
    :return: True if the date is in the past, False otherwise.
    :rtype: bool
    """
    if is_datetime(date):
        return date < datetime.now()
    else:
        return False
    
def is_today(date: datetime) -> bool:
    """
    Checks if a string is parseable into a datetime object.
    If it is not parseable, it returns False.
    If it is parseable, it returns True.

    *Examples*:

    >>> is_today(datetime(2090, 12, 31, 23, 59, 59)) # returns False
    >>> is_today(datetime(2000, 12, 31, 23, 59, 59)) # returns False
    >>> is_today(datetime.now()) # returns True

    :param date: datetime object
    :return: True if the date is today, False otherwise.
    :rtype: bool
    """
    if is_datetime(date):
        return date.date() == datetime.now().date()
    else:
        return False

def is_business_day(date: datetime) -> bool:
    """
    Checks if a datetime object is a business day.
    A business day is a weekday that is not a holiday.

    *Examples*:

    >>> is_business_day(datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_business_day(datetime(2000, 12, 31, 23, 59, 59)) # returns True
    >>> is_business_day(datetime.now()) # returns True

    :param date: datetime object
    :return: True if the date is a business day, False otherwise.
    :rtype: bool
    """
    if is_datetime(date):
        return date.weekday() < 5
    else:
        return False

def is_same_day(date1: datetime, date2: datetime) -> bool:
    """
    Checks if two datetime objects are the same day.

    *Examples*:

    >>> is_same_day(datetime(2090, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_same_day(datetime(2000, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns False
    >>> is_same_day(datetime.now(), datetime.now()) # returns True

    :param date1: datetime object
    :param date2: datetime object
    :return: True if the dates are the same day, False otherwise.
    :rtype: bool
    """
    if is_datetime(date1) and is_datetime(date2):
        return date1.date() == date2.date()
    else:
        return False

def is_same_week(date1: datetime, date2: datetime) -> bool:
    """
    Checks if two datetime objects are the same week.

    *Examples*:

    >>> is_same_week(datetime(2090, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_same_week(datetime(2000, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns False
    >>> is_same_week(datetime.now(), datetime.now()) # returns True

    :param date1: datetime object
    :param date2: datetime object
    :return: True if the dates are the same week, False otherwise.
    :rtype: bool
    """
    if is_datetime(date1) and is_datetime(date2):
        return date1.isocalendar()[1] == date2.isocalendar()[1]
    else:
        return False
    
def is_same_month(date1: datetime, date2: datetime) -> bool:
    """
    Checks if two datetime objects are the same month.

    *Examples*:

    >>> is_same_month(datetime(2090, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_same_month(datetime(2000, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns False
    >>> is_same_month(datetime.now(), datetime.now()) # returns True

    :param date1: datetime object
    :param date2: datetime object
    :return: True if the dates are the same month, False otherwise.
    :rtype: bool
    """
    if is_datetime(date1) and is_datetime(date2):
        return date1.month == date2.month
    else:
        return False
    
def is_same_year(date1: datetime, date2: datetime) -> bool:
    """
    Checks if two datetime objects are the same year.

    *Examples*:

    >>> is_same_year(datetime(2090, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_same_year(datetime(2000, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns False
    >>> is_same_year(datetime.now(), datetime.now()) # returns True

    :param date1: datetime object
    :param date2: datetime object
    :return: True if the dates are the same year, False otherwise.
    :rtype: bool
    """
    if is_datetime(date1) and is_datetime(date2):
        return date1.year == date2.year
    else:
        return False

def is_valid_range(date1: datetime, date2: datetime) -> bool:
    """
    Checks if two datetime objects are a valid range.
    A valid range is a range where the first date is before the second date.

    *Examples*:

    >>> is_valid_range(datetime(2090, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_valid_range(datetime(2000, 12, 31, 23, 59, 59), datetime(2090, 12, 31, 23, 59, 59)) # returns True
    >>> is_valid_range(datetime.now(), datetime.now()) # returns True
    >>> is_valid_range(datetime(2090, 12, 31, 23, 59, 59), datetime(2000, 12, 31, 23, 59, 59)) # returns False

    :param date1: datetime object
    :param date2: datetime object
    :return: True if the dates are a valid range, False otherwise.
    :rtype: bool
    """
    if is_datetime(date1) and is_datetime(date2):
        return date1 < date2
    else:
        return False
    
# def check_format(datetime_string: str, format: str) -> bool:
    # """
    # Checks if the given datetime string matches the specified format string.
    # It returns True if the datetime string matches the format, and False otherwise. 



