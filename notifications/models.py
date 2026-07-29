from django.db import models
from accounts.models import CustomUser


class Notification(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=255)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
class ActivityLog(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=100)

    model_name = models.CharField(max_length=100)

    object_name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.model_name}"