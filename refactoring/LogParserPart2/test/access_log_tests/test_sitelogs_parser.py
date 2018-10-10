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

import unittest
from access_log.log_record import AccessLogRecord
from datetime import datetime
from access_log.date_helpers import custom_timezone


class SiteLoglineParserTest(unittest.TestCase):
    """BlogLoglineParserTest

    the parser converts from an access log record (a long, weird string) to
    a record that python can work with. This tests ensures we know how to
    parse them correctly.
    """

    sample = '111.118.240.191 [26/May/2013:22:45:47 -0500] "-" | Status=400 | Bytes Sent=0 | URL="-" | Agent="-" | Request_Time=5.839 | Upstream_Response_Time=- | Pipe=.'

    def setUp(self):
        self.record = AccessLogRecord(self.sample)

    def test_collects_ip(self):
        self.assertEqual(self.record.ip, '111.118.240.191')

    def test_collects_timestamp(self):
        self.assertEqual(self.record.date,
                         datetime(2013, 5, 26, 22, 45, 47,
                                  tzinfo=custom_timezone(-500)))

    def test_collects_command(self):
        self.assertEqual(self.record.request, "-")

    def test_collects_keywords(self):
        record = self.record
        self.assertEqual(record.status, '400')
        self.assertEqual(record.bytes_sent, '0')
        self.assertEqual(record.referer, '-')
        self.assertEqual(record.agent, '-')
        self.assertEqual(record.request_time, '5.839')
        self.assertEqual(record.upstream_response_time, '-')
        self.assertEqual(record.pipe, '.')

    def test_not_naive(self):
        self.assertFalse(self.record.is_naive_user())

    def test_is_naive_user(self):
        # Bad test: far more information than needed
        data = '0.0.0.0 [01/Jan/2013:00:00:00 +0000] "-" | Status=foo | Bytes Sent=foo | URL=foo | Agent="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"'
        record = AccessLogRecord(data)
        self.assertEqual(record.agent, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
        self.assertTrue(record.is_naive_user())
