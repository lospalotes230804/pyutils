"""
This file contains functions for datetime validation.
Inspired by
"""

# Importing the required libraries
from datetime import datetime
from .validate import is_datetime

DEFAULT_TIME_FORMAT = '%H:%M:%S'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Get information about a datetime

def get_timestamp(date: datetime) -> int:
    """
    Gets the timestamp of a datetime.

    *Examples:*

    >>> get_timestamp(dt.datetime(2020, 1, 1)) # returns 1577836800

    :param date: The datetime to get the timestamp of.
    :type date: dt.datetime
    :return: The timestamp of the datetime.
    :rtype: int
    """
    if is_datetime(date):
        return int(date.timestamp())
    else:
        return None

def get_time(date: datetime, format=DEFAULT_TIME_FORMAT) -> str:
    """
    Gets the time of a datetime.

    *Examples:*

    >>> get_time(dt.datetime(2020, 1, 1)) # returns '00:00:00'

    :param date: The datetime to get the time of.
    :type date: dt.datetime
    :return: The time of the datetime.
    :rtype: str
    """
    if is_datetime(date):
        return date.strftime('%H:%M:%S')
    else:
        return None
    
def get_date(date: datetime, format=DEFAULT_DATE_FORMAT) -> str:
    """
    Gets the date of a datetime.

    *Examples:*

    >>> get_date(dt.datetime(2020, 1, 1)) # returns '2020-01-01'

    :param date: The datetime to get the date of.
    :type date: dt.datetime
    :return: The date of the datetime.
    :rtype: str
    """
    if is_datetime(date):
        return date.strftime('%Y-%m-%d')
    else:
        return None

def get_timezone(date: datetime) -> str:
    """
    Gets the timezone of a datetime.

    *Examples:*

    >>> get_timezone(dt.datetime(2020, 1, 1)) # returns 'UTC'

    :param date: The datetime to get the timezone of.
    :type date: dt.datetime
    :return: The timezone of the datetime.
    :rtype: str
    """
    if is_datetime(date):
        return date.tzname()
    else:
        return None

def get_age(date: datetime) -> int:
    """
    Calculates the age in years based on a given date.

    *Examples*:

    >>> get_age(datetime(2000, 12, 31, 23, 59, 59)) # returns 23
    >>> get_age(datetime(2090, 12, 31, 23, 59, 59)) # returns -67

    :param date: datetime object
    :return: age in years
    :rtype: int
    """
    if is_datetime(date):
        return datetime.now().year - date.year
    else:
        return 0

def get_season(date: datetime) -> str:
    """
    Gets the season of a datetime.

    *Examples:*

    >>> get_season(dt.datetime(2020, 1, 1)) # returns 'winter'

    :param date: The datetime to get the season of.
    :type date: dt.datetime
    :return: The season of the datetime.
    :rtype: str
    """
    if is_datetime(date):
        if date.month in (12, 1, 2):
            return 'winter'
        elif date.month in (3, 4, 5):
            return 'spring'
        elif date.month in (6, 7, 8):
            return 'summer'
        elif date.month in (9, 10, 11):
            return 'autumn'

def get_quarter(date: datetime) -> int:
    """
    Calculates the quarter of a given date.

    *Examples*:

    >>> get_quarter(datetime(2000, 12, 31, 23, 59, 59)) # returns 4
    >>> get_quarter(datetime(2090, 12, 31, 23, 59, 59)) # returns 4

    :param date: datetime object
    :return: quarter
    :rtype: int
    """
    if is_datetime(date):
        return (date.month - 1) // 3 + 1
    else:
        return 0
    
def get_day_of_year(date: datetime) -> int:
    """
    Calculates the day of the year of a given date.

    *Examples*:

    >>> get_day_of_year(datetime(2000, 12, 31, 23, 59, 59)) # returns 366
    >>> get_day_of_year(datetime(2090, 12, 31, 23, 59, 59)) # returns 365

    :param date: datetime object
    :return: day of the year
    :rtype: int
    """
    if is_datetime(date):
        return date.timetuple().tm_yday
    else:
        return 0
