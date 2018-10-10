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

from collections import defaultdict


class AgentAggregator():
    def __init__(self):
        self._agents_dict = defaultdict(lambda: 0)

    def add(self, record):
        if 'msie' in record.agent.lower():
            self._agents_dict['msie'] += 1
        elif 'chrome' in record.agent.lower():
            self._agents_dict['chrome'] += 1
        elif 'firefox' in record.agent.lower():
            self._agents_dict['firefox'] += 1
        else:
            self._agents_dict['others'] += 1

    def browser_count_for(self, browserkey):
        return self._agents_dict[browserkey]


class StatusURLAggregator():
    def __init__(self):
        self._status_uri_dict = defaultdict(lambda: defaultdict(lambda: 0))

    def add(self, record):
        self._status_uri_dict[record.status][record.request_uri] += 1

    def url_count_for_status(self, url, status):
        return self._status_uri_dict[status][url]
