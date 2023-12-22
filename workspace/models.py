from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.



class Subtasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default=None)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
    created_at = models.DateField(default=datetime.date.today)
    checked = models.BooleanField(default=False)
    assigned = models.ManyToManyField(User, related_name='members')
    due_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.id} {self.title}'
    
    # funktion wie lange bis due_date


class Tickets(models.Model):
    todo = 'Todo'
    in_progress = 'In Progress'
    await_feedback = 'Awaiting Feedback'
    done = 'Done'
    low = 'Low'
    middle = 'Middle'
    high = 'High'

    status_choices = {
        todo: todo,
        in_progress: in_progress,
        await_feedback: await_feedback,
        done: done,
    }

    priority_choices = {
        low: low,
        middle: middle,
        high: high,
    }

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default=None)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    created_at = models.DateField(default=datetime.date.today)
    checked = models.BooleanField(default=False)
    assigned_to = models.ManyToManyField(User, related_name='assigned_to')
    priority = models.CharField(max_length=20, choices=priority_choices, default=low)
    status = models.CharField(max_length=20, choices=status_choices, default=todo)
    due_date = models.DateField(default=datetime.date.today)
    subtasks = models.ManyToManyField(Subtasks, related_name='subtasks', default=None)

    def __str__(self):
        return f'{self.id} {self.title}'
    
    # funktion wie lange bis due_date

class Boards(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    created_at = models.DateField(default=datetime.date.today)
    tickets = models.ManyToManyField(Tickets, related_name='tickets')

    def __str__(self):
        return f'{self.id} {self.title}'
