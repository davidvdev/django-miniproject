# Generated by Django 3.2.7 on 2021-09-08 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_map_layout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='layout',
        ),
    ]
