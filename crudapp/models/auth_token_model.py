from django.db import models
from django.utils import timezone



class AccessToken(models.Model):
    """ This model is used for the  add access token details"""

    token = models.CharField(max_length=512, unique=True)
    token_time_limit = models.IntegerField(default=30000)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
