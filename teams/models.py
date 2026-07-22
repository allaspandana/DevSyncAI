from django.db import models
from accounts.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    leader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="leading_teams"
    )

    members = models.ManyToManyField(
        CustomUser,
        related_name="teams"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name