# Generated by Django 4.0.6 on 2022-08-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_webbeta1_ip1_alter_webbeta1_ip2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUpdateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('beta', models.CharField(max_length=100)),
                ('production', models.CharField(max_length=100)),
            ],
        ),
    ]
