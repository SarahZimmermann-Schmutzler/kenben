from django.db import models
import datetime
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.id} {self.title}'

   

class Ticket(models.Model):
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
    description = models.CharField(max_length=300, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    created_at = models.DateField(default=datetime.date.today)
    checked = models.BooleanField(default=False)
    assigned_to = models.ManyToManyField(User, related_name='assigned_to')
    priority = models.CharField(max_length=20, choices=priority_choices, default=low)
    status = models.CharField(max_length=20, choices=status_choices, default=todo)
    due_date = models.DateField(default=datetime.date.today)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tickets', default=None)

    def __str__(self):
        return f'{self.id} {self.title}'
    
    # shows how many days until due_date
    def time_till_due(self):
        today = date.today()
        due = self.due_date
        delta = due - today
        return delta.days
    
    # shows the username of the user
    def assigned_to_usernames(self):
        usernames = [user.username for user in self.assigned_to.all()]
        # return ', '.join(user.username for user in self.assigned_to.all())
        return usernames
    
    # shows the first letter of the usersnames
    def assigned_to_first_letter(self):
        first_letters = []
        usernames = [user.username for user in self.assigned_to.all()]
        for username in usernames:
            first_letter = username[0]
            first_letters.append(first_letter)
        return first_letters


class Subtask(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_at = models.DateField(default=datetime.date.today)
    checked = models.BooleanField(default=False)
    assigned = models.ManyToManyField(User, related_name='members')
    due_date = models.DateField(default=datetime.date.today)
    tickets = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='subtasks', default=None)

    def __str__(self):
        return f'{self.id} {self.title}'