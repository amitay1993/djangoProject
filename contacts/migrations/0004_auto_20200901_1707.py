# Generated by Django 3.1 on 2020-09-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200901_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='phone',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Academic',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Acreditation',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Institution',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='LinkedIn',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Mobile',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Office',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Profession',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='Title',
            field=models.CharField(choices=[('1', 'Mr'), ('2', 'Mrs'), ('3', 'Miss'), ('4', 'Dr'), ('5', 'Prof')], default=('1', 'Mr'), max_length=1),
        ),
    ]
