# Generated by Django 5.0 on 2024-01-04 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_rename_delevered_order_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.section'),
        ),
    ]