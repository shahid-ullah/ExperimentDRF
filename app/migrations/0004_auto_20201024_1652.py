# Generated by Django 3.1.2 on 2020-10-24 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201024_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewtestmodel',
            old_name='title1',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='viewtestmodel',
            name='title2',
        ),
    ]
