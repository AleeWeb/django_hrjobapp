# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class addJobs(models.Model):
    job_title = models.CharField(max_length = 255)
    job_descp = models.CharField(max_length = 500)
    post_date = models.DateTimeField(auto_now_add = True)