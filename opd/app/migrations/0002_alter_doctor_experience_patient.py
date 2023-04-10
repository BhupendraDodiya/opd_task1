# Generated by Django 4.1.5 on 2023-04-10 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.CharField(choices=[('10 years', '10 years'), ('20 years', '20 years'), ('30 years', '30 years'), ('35 years', '35 years'), ('40 years', '40 years')], max_length=100),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('issue', models.CharField(max_length=100)),
                ('appointment', models.DateTimeField()),
                ('select_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
            ],
        ),
    ]
