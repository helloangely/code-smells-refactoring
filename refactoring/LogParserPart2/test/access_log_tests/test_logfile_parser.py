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
from access_log.streamers.record_streamer import FileRecordStreamer
from access_log.record_stream_processor import RecordStreamProcessor
from access_log.aggregators import StatusURLAggregator, AgentAggregator


class BlogLogFileParserTest(unittest.TestCase):
    def setUp(self):
        self.reporter = RecordStreamProcessor(FileRecordStreamer('data/blog_access.log'),
                                              [StatusURLAggregator(), AgentAggregator()])
        self.reporter.process()

    def test_parses_all_lines(self):
        self.assertEquals(8553, self.reporter.get_record_count())

    def test_parses_records_correctly(self):
        self.assertEquals(91,
                          self.reporter.url_count_for_status('/blog/workplacesafety/', '200'))
        self.assertEquals(3431,self.reporter.browser_count_for('chrome'))


class SiteLogFileParserTest(unittest.TestCase):
    def setUp(self):
        self.reporter = RecordStreamProcessor(FileRecordStreamer('data/site_access.log'),
                                              [StatusURLAggregator(), AgentAggregator()])
        self.reporter.process()

    def test_parses_all_lines(self):
        self.assertEquals(22332, self.reporter.get_record_count())

    def test_parses_records_correctly(self):
        self.assertEquals(199,
                          self.reporter.url_count_for_status('/handle_moi?Drama=LoginPizza', '200'))
        self.assertEquals(3576, self.reporter.browser_count_for('msie'))
