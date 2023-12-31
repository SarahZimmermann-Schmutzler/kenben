# Generated by Django 5.0 on 2023-12-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0010_alter_subtask_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='tickets',
            field=models.ManyToManyField(blank=True, default=None, related_name='tickets', to='workspace.ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subtasks',
            field=models.ManyToManyField(blank=True, default=None, related_name='subtasks', to='workspace.subtask'),
        ),
    ]
