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

from industriallogic.example.employee import Employee
from industriallogic.example.job import Job


class Programmer(Employee):
            
    def _responsibilities(self):
        return [Job.PROGRAM, Job.TEST, Job.INTEGRATE, Job.DESIGN]
