from django.contrib import admin
from .models import Board, Ticket, Subtask

# Register your models here.
admin.site.register(Board)
admin.site.register(Ticket)
admin.site.register(Subtask)