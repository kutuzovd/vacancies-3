from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    company = models.ForeignKey('vacan.Company', on_delete=models.CASCADE, related_name='users', default=None, null=True,
                                blank=True)
    resume = models.ForeignKey('resume.Resume', on_delete=models.CASCADE, related_name='users', default=None, null=True,
                               blank=True)