# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Tweet(models.Model):
   author = models.CharField(max_length=150)
   content = models.CharField(max_length=140)
   date_and_time = models.DateTimeField(default=datetime.now)



