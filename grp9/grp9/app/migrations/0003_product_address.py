# Generated by Django 3.2.9 on 2021-11-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211108_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.TextField(default=0),
        ),
    ]