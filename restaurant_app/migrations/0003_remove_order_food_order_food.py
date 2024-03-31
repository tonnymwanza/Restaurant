# Generated by Django 5.0 on 2024-03-30 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
        migrations.AddField(
            model_name='order',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.food'),
        ),
    ]
