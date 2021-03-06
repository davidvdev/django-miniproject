# Generated by Django 3.2.7 on 2021-09-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_remove_map_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='columns',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='layout',
            field=models.CharField(default='100111010', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='rows',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
