# Generated by Django 5.0 on 2023-12-19 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_banner_area_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main_catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.catagory')),
            ],
        ),
    ]
