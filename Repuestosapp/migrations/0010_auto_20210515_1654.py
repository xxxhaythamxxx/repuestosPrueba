# Generated by Django 3.0.5 on 2021-05-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repuestosapp', '0009_auto_20210514_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engine',
            name='members',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='car_engine_info',
        ),
        migrations.AddField(
            model_name='engine',
            name='car_engine_info',
            field=models.ManyToManyField(to='Repuestosapp.car'),
        ),
        migrations.RemoveField(
            model_name='spare',
            name='car_info',
        ),
        migrations.AddField(
            model_name='spare',
            name='car_info',
            field=models.ManyToManyField(to='Repuestosapp.car'),
        ),
        migrations.RemoveField(
            model_name='spare',
            name='engine_info',
        ),
        migrations.AddField(
            model_name='spare',
            name='engine_info',
            field=models.ManyToManyField(to='Repuestosapp.engine'),
        ),
    ]