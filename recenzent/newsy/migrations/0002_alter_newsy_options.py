# Generated by Django 3.2.19 on 2023-05-26 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsy',
            options={'ordering': ['-data'], 'verbose_name_plural': 'Newsy'},
        ),
    ]
