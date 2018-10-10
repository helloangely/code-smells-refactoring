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

class RecordStreamProcessor:
    def __init__(self, record_stream, aggregators=None):
        if aggregators is None:
            aggregators = []
        self._record_stream = record_stream
        self._record_count = 0
        self._aggregators = aggregators

    def process(self):
        for record in self._record_stream:
            self._record_count += 1
            for aggregator in self._aggregators:
                aggregator.add(record)

    def get_record_count(self):
        return self._record_count

    # Dynamic magic patching...
    def __getattr__(self, name):
        for aggregator in self._aggregators:
            if hasattr(aggregator, name):
                return getattr(aggregator, name)
        raise AttributeError(name)
