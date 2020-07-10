from django.contrib.auth.models import AbstractUser
from django.db import models


# Models
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    fullname = models.CharField(null="", blank=True, max_length=100)

    CATEGORIES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    sex = models.CharField(null="", blank=True, max_length=6, choices=CATEGORIES)
