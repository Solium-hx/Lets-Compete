# Generated by Django 4.0 on 2022-04-16 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_eventregistered_rename_cart_carts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mini_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
