# Generated by Django 3.1.2 on 2020-11-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smashorpass', '0004_auto_20201101_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]