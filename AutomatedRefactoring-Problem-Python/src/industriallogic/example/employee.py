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


class Employee(object):
    def __init__(self):
        self._jobs_skipped = 0
        self._jobs_completed = 0
        self.jobs = []

    def jobs_completed_count(self):
        return self._jobs_completed

    def jobs_skipped_count(self):
        return self._jobs_skipped

    def perform_job(self, job):
        if job in self._responsibilities():
            self._jobs_completed += 1
        else:
            self._jobs_skipped += 1

    def _responsibilities(self):
        raise NotImplementedError
