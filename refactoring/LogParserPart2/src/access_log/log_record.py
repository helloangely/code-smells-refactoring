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

import re
import csv
from datetime import datetime
from access_log.date_helpers import custom_timezone, MONTHS


class AccessLogRecord(object):

    def __init__(self, input):
        mainlog_pattern = '([0-9.]+) \[([^]]*)] "([^"]+)" \| (.*)'
        bloglog_pattern = '([0-9.]+) ([^\s]+) - \[([^]]*)] (.*)'

        match_data = re.match(mainlog_pattern, input)
        if match_data:
            self._process_mainlog_record(match_data)
        else:
            match_data = re.match(bloglog_pattern, input)
            self._process_bloglog_record(match_data)
        self.request_uri = self.get_request_path(self.request)

    def _process_mainlog_record(self, match_data):
        self.ip = match_data.group(1)
        self.date = self._make_date_from_match(match_data.group(2))
        self.request = match_data.group(3)
        self._set_mainlog_attributes(match_data.group(4))

    def _set_mainlog_attributes(self, name_value_pairs):
        for field in name_value_pairs.split('|'):
            (original_name, original_value) = field.split("=",1)
            name = self._convert_fieldname_to_attributename(original_name)
            value = original_value.strip().strip('"')
            setattr(self, name, value)

    def _convert_fieldname_to_attributename(self, original_name):
        name = re.sub('\W+','_', original_name.strip().lower())
        if name == 'url':
            name = 'referer'
        return name

    def _process_bloglog_record(self, match_data):
        self.ip = match_data.group(1)
        self.date = self._make_date_from_match(match_data.group(3))
        self._set_bloglog_attributes(match_data.group(4))

    def _set_bloglog_attributes(self, attributes):
        parsed_record = csv.DictReader(
            [attributes], 
            delimiter=' ',
            quotechar='"',
            fieldnames=["request", "status", "bytes_sent",
                        "referer", "agent"])
        for item in parsed_record:
            for field_key in item:
                setattr(self, field_key, item[field_key].strip().strip('"'))


    date_pattern = '(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+) ([+-]?\d+)'

    def _make_date_from_match(self, date):
        date_match = re.match(self.date_pattern, date)
        year = int(date_match.group(3))
        month = MONTHS[date_match.group(2)]
        day = int(date_match.group(1))
        hour = int(date_match.group(4))
        minutes = int(date_match.group(5))
        seconds = int(date_match.group(6))
        tz_offset = int(date_match.group(7))
        tz = custom_timezone(tz_offset)
        return datetime(year, month, day, hour, minutes, seconds, tzinfo=tz)

    def get_request_path(self, log_substring):
        m = log_substring.split()
        if len(m) > 1:
            return m[1]
        return '-'

    def is_naive_user(self):
        return "msie" in self.agent.lower()
