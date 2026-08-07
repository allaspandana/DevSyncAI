from django.db import models
from sprints.models import Sprint
from accounts.models import CustomUser



class Task(models.Model):


    STATUS_CHOICES = [

        ('To Do', 'To Do'),

        ('In Progress', 'In Progress'),

        ('In Review', 'In Review'),

        ('Completed', 'Completed'),

        ('Blocked', 'Blocked'),

    ]



    PRIORITY_CHOICES = [

        ('Low', 'Low'),

        ('Medium', 'Medium'),

        ('High', 'High'),

        ('Critical', 'Critical'),

    ]



    sprint = models.ForeignKey(

        Sprint,

        on_delete=models.CASCADE,

        related_name='tasks'

    )



    assigned_to = models.ForeignKey(

        CustomUser,

        on_delete=models.CASCADE,

        related_name='assigned_tasks'

    )



    title = models.CharField(

        max_length=200

    )



    description = models.TextField()



    status = models.CharField(

        max_length=30,

        choices=STATUS_CHOICES,

        default='To Do'

    )



    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES,

        default='Medium'

    )



    due_date = models.DateField()



    estimated_hours = models.IntegerField()



    created_at = models.DateTimeField(

        auto_now_add=True
    )

    def __str__(self):

        return self.title