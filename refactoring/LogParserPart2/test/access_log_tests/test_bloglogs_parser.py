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


class BlogLoglineParserTest(unittest.TestCase):
    """BlogLoglineParserTest

    the parser converts from a blog-access-log record (a long, weird string) to
    a record that python can work with. This tests ensures we know how to
    parse them correctly.
    """

    sample = '66.249.85.184 www.industriallogic.com - [16/Jun/2013:06:25:43 +0000] "GET / HTTP/1.1" 200 16044 "-" "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0 Google (+https://developers.google.com/+/web/snippet/)"'

    def setUp(self):
        self.record = AccessLogRecord(self.sample)

    def test_collects_ip(self):
        self.assertEqual(self.record.ip, '66.249.85.184')

    def test_collects_timestamp(self):
        self.assertEqual(self.record.date, datetime(2013, 6, 16, 6, 25, 43,
                                                    tzinfo=custom_timezone(0)))

    def test_collects_command(self):
        self.assertEqual(self.record.request, "GET / HTTP/1.1")

    def test_parses_request_uri(self):
        record = self.record
        self.assertEqual(record.request_uri, '/')

    def test_collects_keywords(self):
        record = self.record
        self.assertEqual(record.status, '200')
        self.assertEqual(record.bytes_sent, '16044')
        self.assertEqual(record.referer, '-')
        self.assertEqual(record.agent, 'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0 Google (+https://developers.google.com/+/web/snippet/)')

    def test_not_naive(self):
        self.assertFalse(self.record.is_naive_user())

    def test_is_naive_user(self):
        data = '64.207.157.149 industriallogic.com - [16/Jun/2013:06:29:23 +0000] "HEAD / HTTP/1.1" 301 0 "http://agilescout.com" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"'
        record = AccessLogRecord(data)
        self.assertEqual(record.agent, "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)")
        self.assertTrue(record.is_naive_user())
