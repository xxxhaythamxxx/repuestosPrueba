# Generated by Django 3.0.5 on 2021-05-15 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repuestosapp', '0008_auto_20210509_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spare',
            name='spare_photo',
            field=models.ImageField(upload_to='spares'),
        ),
    ]
