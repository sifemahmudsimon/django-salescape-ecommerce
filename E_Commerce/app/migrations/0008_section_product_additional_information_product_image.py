# Generated by Django 5.0 on 2023-12-19 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_category_catagory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField()),
                ('Availability', models.IntegerField()),
                ('featured_image', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Discount', models.CharField(max_length=50)),
                ('Product_Information', models.TextField()),
                ('model_Name', models.CharField(max_length=50)),
                ('Tags', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Catagorys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='app.catagory')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='section_products', to='app.catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_url', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
