# Generated by Django 2.0.6 on 2020-06-26 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='docreation',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='docompletion',
            new_name='datecompleted',
        ),
    ]
