# Generated by Django 3.1.3 on 2020-11-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                    ('name_client', models.CharField(max_length=50)),
                    ('country',models.CharField(max_length=50)),
                    ('country', models.CharField(max_length=50)),
                    ('user_created', models.CharField(max_length=50)),
                    ('is_active', models.CharField(max_length=50)),
                    ('fechas_de_control', models.CharField(max_length=50)),
            ],
        ),
    ]
