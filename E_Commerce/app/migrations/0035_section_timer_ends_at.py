# Generated by Django 5.0 on 2024-01-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_product_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='timer_ends_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
