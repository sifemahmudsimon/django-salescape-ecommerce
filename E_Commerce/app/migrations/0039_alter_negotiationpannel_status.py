# Generated by Django 5.0 on 2024-01-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_negotiationpannel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negotiationpannel',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=20),
        ),
    ]
