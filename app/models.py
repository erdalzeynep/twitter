# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


class Tweet(models.Model):
    author = models.CharField(max_length=150)
    content = models.CharField(max_length=140, null=False, blank=False)
    date_and_time = models.DateTimeField(default=datetime.now)
