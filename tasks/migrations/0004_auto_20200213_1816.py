# Generated by Django 3.0.2 on 2020-02-13 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200211_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='task',
            name='timestamp',
        ),
    ]
