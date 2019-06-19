# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=100,verbose_name='full name')
    age=models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    date_of_birth=models.DateTimeField(default=timezone.now,blank=True)
    