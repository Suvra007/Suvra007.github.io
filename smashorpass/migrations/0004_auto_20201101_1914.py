# Generated by Django 3.1.2 on 2020-11-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smashorpass', '0003_auto_20201101_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(null=True, upload_to='main/images'),
        ),
    ]