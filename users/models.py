from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    image = models.FileField(upload_to="images/user_profile/%y/%m/%d/", blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)

    @property
    def type_user(self):
        type=""
        if self.is_superuser:
            type="admin"
        elif self.is_staff:
            type="seller"
        else:
            type="user"
        return type








