# Generated by Django 4.1.5 on 2023-04-10 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='appointment',
        ),
    ]