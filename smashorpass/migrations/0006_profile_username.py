# Generated by Django 3.1.2 on 2020-11-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smashorpass', '0005_auto_20201102_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.TextField(default='Enter username'),
        ),
    ]
