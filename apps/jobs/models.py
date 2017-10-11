# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

class jobPoster(models.Manager):
    def validator(self, post_data):
        errors = []

        return errors

    def create_job(self, post_data):
        new_job = self.create(
            job_title=post_data['job_title'],
            job_descp=post_data['job_descp'],
            post_date =post_data['post_date']
            )
        return new_job

class addJob(models.Model):
    job_title = models.CharField(max_length = 255)
    job_descp = models.CharField(max_length = 500)
    post_date = models.DateField(auto_now_add = True)
    objects = jobPoster()