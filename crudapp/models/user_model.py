import bcrypt
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    """ User model  that store basic details of user"""
    ROLE_CHOICES = [(1, "Admin"), (2, "User")]

    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    cell_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = 'cell_number'

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))


    def __str__(self):
        """ name of each user """
        return self.name
