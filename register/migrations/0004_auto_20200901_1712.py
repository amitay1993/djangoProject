# Generated by Django 3.1 on 2020-09-01 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20200901_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='LinkedIn',
            new_name='LinkedIn_address',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='Mobile',
            new_name='Mobile_Phone',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='Office',
            new_name='Office_Phone',
        ),
    ]
