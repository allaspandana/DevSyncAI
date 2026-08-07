from django.db import models
from tasks.models import Task
from accounts.models import CustomUser



class Bug(models.Model):


    SEVERITY_CHOICES = [

        ('Low', 'Low'),

        ('Medium', 'Medium'),

        ('High', 'High'),

        ('Critical', 'Critical'),

    ]



    PRIORITY_CHOICES = [

        ('Low', 'Low'),

        ('Medium', 'Medium'),

        ('High', 'High'),

        ('Urgent', 'Urgent'),

    ]



    STATUS_CHOICES = [

        ('Open', 'Open'),

        ('Assigned', 'Assigned'),

        ('In Progress', 'In Progress'),

        ('Resolved', 'Resolved'),

        ('Closed', 'Closed'),

    ]



    task = models.ForeignKey(

        Task,

        on_delete=models.CASCADE,

        related_name='bugs'

    )



    assigned_to = models.ForeignKey(

        CustomUser,

        on_delete=models.CASCADE,

        related_name='assigned_bugs'

    )



    title = models.CharField(

        max_length=200

    )



    description = models.TextField()



    severity = models.CharField(

        max_length=20,

        choices=SEVERITY_CHOICES,

        default='Medium'

    )



    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES,

        default='Medium'

    )



    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='Open'

    )



    reported_by = models.ForeignKey(

        CustomUser,

        on_delete=models.CASCADE,

        related_name='reported_bugs'

    )



    reported_date = models.DateTimeField(

        auto_now_add=True

    )



    resolved_date = models.DateField(

        null=True,

        blank=True

    )



    def __str__(self):

        return self.title