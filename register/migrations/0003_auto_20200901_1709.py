# Generated by Django 3.1 on 2020-09-01 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_usermodel_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='Academic',
            new_name='Academic_Acreditation',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='Acreditation',
        ),
    ]