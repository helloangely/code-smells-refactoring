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
from industriallogic.example.job import Job
from industriallogic.example.manager import Manager
from industriallogic.example.programmer import Programmer


class EmployeeTest(unittest.TestCase):

    def test_no_jobs_performed(self):
        self.dead_beat = Manager()
        self.assertEquals(0, self.dead_beat.jobs_completed_count())
        self.assertEquals(0, self.dead_beat.jobs_skipped_count())

    def test_three_jobs_performed_none_skipped_by_manager(self):
        self.productive_manager = Manager()
        self.productive_manager.perform_job(Job.MANAGE)
        self.productive_manager.perform_job(Job.MARKET)
        self.productive_manager.perform_job(Job.SELL)
        self.assertEquals(3, self.productive_manager.jobs_completed_count())
        self.assertEquals(0, self.productive_manager.jobs_skipped_count())

    def test_one_job_done_one_job_skipped_by_manager(self):
        self.unbusy_manager = Manager()
        self.unbusy_manager.perform_job(Job.TEST)
        self.unbusy_manager.perform_job(Job.SELL)
        self.assertEquals(1, self.unbusy_manager.jobs_completed_count())
        self.assertEquals(1, self.unbusy_manager.jobs_skipped_count())

    def test_no_jobs_done(self):
        self.dead_beat = Programmer()
        self.assertEquals(0, self.dead_beat.jobs_completed_count())
        self.assertEquals(0, self.dead_beat.jobs_skipped_count())

    def test_three_jobs_performed_none_skipped_by_programmer(self):
        self.productive_programmer = Programmer()
        self.productive_programmer.perform_job(Job.TEST)
        self.productive_programmer.perform_job(Job.PROGRAM)
        self.productive_programmer.perform_job(Job.INTEGRATE)
        self.assertEquals(3, self.productive_programmer.jobs_completed_count())
        self.assertEquals(0, self.productive_programmer.jobs_skipped_count())

    def test_one_job_done_one_job_skipped_by_programmer(self):
        self.unbusy_programmer = Programmer()
        self.unbusy_programmer.perform_job(Job.TEST)
        self.unbusy_programmer.perform_job(Job.SELL)
        self.assertEquals(1, self.unbusy_programmer.jobs_completed_count())
        self.assertEquals(1, self.unbusy_programmer.jobs_skipped_count())


if __name__ == '__main__':
    unittest.main()
