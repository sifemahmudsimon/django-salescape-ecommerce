# Generated by Django 5.0 on 2023-12-19 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner_area',
            old_name='image',
            new_name='Image',
        ),
    ]
