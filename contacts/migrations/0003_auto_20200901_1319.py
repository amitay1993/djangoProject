# Generated by Django 3.1 on 2020-09-01 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200830_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='password',
        ),
    ]
