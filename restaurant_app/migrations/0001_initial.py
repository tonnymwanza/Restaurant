# Generated by Django 5.0 on 2024-03-30 02:57

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            managers=[
                ('food_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text='enter your email', max_length=254)),
                ('phone_number', models.IntegerField()),
                ('date_to_come', models.DateField(blank=True, null=True)),
                ('time_to_come', models.DateTimeField(blank=True, null=True)),
                ('number_of_people', models.IntegerField()),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
