# Generated by Django 4.0.3 on 2022-06-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_rename_webservices_webservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]