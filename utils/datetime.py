"""
This file contains functions for text processing.
Inspired in
https://github.com/dateutil/dateutil/blob/master/src/dateutil/parser/_parser.py
https://dateutil.readthedocs.io/en/stable/examples.html#parse-examples
"""

# Importing the required libraries
import os
import sys
from datetime import *
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dateutil.parser import *
from dateutil.tz import *
from datetime import *


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
    return parse(input_string)

def is_parseable(input_string: str) -> bool:
    """
    Checks if a string is parseable into a datetime object.
    If it is not parseable, it returns False.
    If it is parseable, it returns True.
    """

    try:
        object = parse(input_string)
        if object is not None and isinstance(object, datetime):
            return True
        else:
            return False
    except:
        return False
    

