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

"""
RecordStreamer : Base class which clients will use.

Those deriving from this class could be network/database/filesystem
record-streamers
"""
from access_log.log_record import AccessLogRecord


class RecordStreamer:
    def __init__(self, raw_record_stream, halt_on_error=False):
        self._raw_record_stream = raw_record_stream
        self._halt_on_error = halt_on_error

    def __iter__(self):
        for raw_record in self._raw_record_stream:
            try:
                yield self._process(raw_record)
            except:
                if self._halt_on_error:
                    raise BaseException(raw_record)

    def _process(self, raw_record):
        pass  # Classes extending this base class should over-ride
              # appropriately


class FileRecordStreamer(RecordStreamer):

    def __init__(self, filepath, halt_on_error=False):
        self.file = open(filepath)
        RecordStreamer.__init__(self, self.file, halt_on_error)

    def _process(self, raw_record):
        return AccessLogRecord(raw_record)
