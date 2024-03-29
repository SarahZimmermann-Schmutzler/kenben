# Generated by Django 5.0 on 2024-01-11 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0011_alter_board_tickets_alter_ticket_subtasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='tickets',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='subtask',
            name='tickets',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='workspace.ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='workspace.board'),
        ),
    ]
