# Generated by Django 4.1.5 on 2023-02-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_whattodo_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=True),
        ),
    ]
