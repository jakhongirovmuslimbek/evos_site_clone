from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose

class UserProfile(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to="images/user_profile/%y/%m/%d/", blank=True, null=True)
    thumbnail_image=ImageSpecField(
        source='image',
        processors=[Transpose(),],
        format='JPEG',
        options={'quality':60}
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def type_user(self):
        type=""
        if self.is_superuser:
            type="admin"
        elif self.is_staff:
            type="customer"
        else:
            type="user"
        return type








