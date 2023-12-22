from django.contrib import admin
from .models import Boards, Tickets, Subtasks

# Register your models here.
admin.site.register(Boards)
admin.site.register(Tickets)
admin.site.register(Subtasks)