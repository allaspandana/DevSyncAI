from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = (

        ('ADMIN', 'Admin'),
        ('LEADER', 'Team Leader'),
        ('DEVELOPER', 'Developer'),
        ('TESTER', 'Tester'),

    )


    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='DEVELOPER'
    )


    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )


    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )


    def __str__(self):
        return self.username