# Generated by Django 3.1.2 on 2020-11-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smashorpass', '0002_auto_20201101_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.TextField(default='Enter full name'),
        ),
    ]
