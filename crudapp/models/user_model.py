from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ User model  that store basic details of user"""
    ROLE_CHOICES = [(1, "Admin"), (2, "User")]

    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    name = models.CharField(max_length=255)
    cell_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """ name of each user """
        return self.name
