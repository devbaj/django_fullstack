from django.db import models
import re
import bcrypt

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
            errors["pw"] = "Passwords must be at least 8 characters long and contain 1 uppercase, 1 lowercase, and 1 number"
        if postData["pw"] != postData["pw-conf"]:
            errors["pw_match"] = "Passwords do not match!"
        return errors
    def add_user(self, postData):
        pw_hash = bcrypt.hashpw(postData["pw"].encode(), bcrypt.gensalt())
        new_user = User.objects.create(
            first_name = postData["fname"],
            last_name = postData["lname"],
            username = postData["username"],
            email = postData["email"],
            pw_hash = pw_hash
        )
        return new_user
    def is_original(self, key, value):
        matches = User.objects.filter(**{key:value})
        if len(matches) != 0:
            return False
        return True
    def login(self, postData):
        attempt = User.objects.filter(username=postData["username"])
        if len(attempt) != 1:
            return False
        if bcrypt.checkpw(postData["pw"].encode(), attempt[0].pw_hash.encode()):
            return True
        return False
    def get_id(self, postData):
        user = User.objects.get(username=postData["username"])
        return user.id

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManager()