from django.db import models
import datetime
from django.conf import settings

# Create your models here.

class Boards(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.id} {self.title}'