# Generated by Django 2.1.5 on 2024-02-09 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20240208_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]