from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 2:
            errors["title"] = "Title must be at least 2 characters."
        if len(postData["network"]) < 3:
            errors["network"] = "Network must be at least 3 characters."
        if len(postData["desc"]) < 10:
            errors["desc"] = "Description must be at least 10 characters."
        if len(postData["release_date"]) > 0 and datetime.strptime(postData["release_date"], '%Y-%m-%d') > datetime.today() :
            errors["release_date"] = "Invalid release date."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()