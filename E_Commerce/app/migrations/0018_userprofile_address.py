# Generated by Django 5.0 on 2024-01-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rename_name_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]