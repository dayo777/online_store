# Generated by Django 5.0 on 2024-09-15 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='owner',
        ),
    ]
