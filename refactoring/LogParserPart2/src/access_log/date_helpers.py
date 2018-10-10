# ***************************************************************************
# Copyright (c) 2018, Industrial Logic, Inc., All Rights Reserved.
#
# This code is the exclusive property of Industrial Logic, Inc. It may ONLY be
# used by students during Industrial Logic's workshops or by individuals
# who are being coached by Industrial Logic on a project.
#
# This code may NOT be copied or used for any other purpose without the prior
# written consent of Industrial Logic, Inc.
# ****************************************************************************

from datetime import tzinfo, timedelta

"""date_helper

We need a little help processing dates from the access logs.

MONTHS:
    Here we have a list of month abbreviations mapped to month numbers,

custom_timezone(offset):
    Create a time zone out of a numeric offset of the form used
    by the access log (-500 means UTC minus 5 hours).

"""
MONTHS = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}


def delta_from_offset(offset):
    sign = offset > 0 and 1 or -1
    offset = abs(offset)
    return timedelta(hours=(offset / 100 * sign),
                     minutes=(offset % 100 * sign))


def custom_timezone(offset):

    class Custom_timezone(tzinfo):
        def utcoffset(self, dt):
            return delta_from_offset(offset)

        def tzname(self, dt):
            return "GMT" + offset

        def dst(self, dt):
            return timedelta(0)

    return Custom_timezone()
