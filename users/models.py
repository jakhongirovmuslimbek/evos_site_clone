from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    image = models.FileField(upload_to="images/user_profile/%y/%m/%d/", blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)








