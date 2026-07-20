from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Team Leader', 'Team Leader'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
    ]
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Developer'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username