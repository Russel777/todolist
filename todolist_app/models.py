
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    LOW, MEDIUM, HIGH = range(3)
    PRIORITY_CHOICES = ((LOW, 'Low'), (MEDIUM, 'Medium'), (HIGH, 'High'))

    OPEN, IN_PROGRESS, DONE = range(3)
    STATUS_CHOICES = ((OPEN, 'Open'), (IN_PROGRESS, 'In progress'), (DONE, 'Done'))

    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=LOW)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=OPEN)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
