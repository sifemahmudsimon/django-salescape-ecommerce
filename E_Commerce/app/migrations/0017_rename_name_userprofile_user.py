# Generated by Django 5.0 on 2024-01-01 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_user_userprofile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='user',
        ),
    ]
