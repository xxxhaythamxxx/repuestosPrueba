# Generated by Django 3.0.5 on 2021-05-10 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repuestosapp', '0006_auto_20210509_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_manufacturer',
            field=models.CharField(max_length=20, verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(max_length=30, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='spare_brand',
            field=models.CharField(max_length=15, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='spare_code',
            field=models.CharField(max_length=15, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='spare_name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
    ]
