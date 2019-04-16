from django.db import models
import re


# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# email validation - must follow standard email format
PW_REGEX = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')
# password validation - must be at least 8 char, have 1 number, 1 lowercase, 1 uppercase

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["fname"]) < 2 or len(postData["lname"]) < 2:
            errors["name"] = "Both names must be at least 2 characters long."
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email address."
        if not PW_REGEX.match(postData["pw"]):
            errors["pw"] = "Passwords must be at least 8 characters long."
        if postData["pw"] != postData["conf_pw"]:
            errors["pw_match"] = "Passwords do not match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
