# Generated by Django 3.0.5 on 2021-05-09 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_manufacturer', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=30)),
                ('VIN', models.CharField(blank=True, max_length=18)),
                ('car_from', models.DateField()),
                ('car_to', models.DateField()),
                ('transmission', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_l', models.CharField(max_length=6)),
                ('engine_ide', models.CharField(max_length=10)),
                ('engine_type', models.CharField(max_length=10)),
                ('engine_cylinder', models.IntegerField()),
                ('engine_pistons', models.IntegerField()),
                ('engine_power_kw', models.IntegerField()),
                ('engine_power_hp', models.IntegerField()),
                ('engine_from', models.DateField()),
                ('engine_to', models.DateField()),
                ('car_engine_info', models.ForeignKey(default='Algo', on_delete=django.db.models.deletion.CASCADE, related_name='AutoInfo', to='Repuestosapp.car')),
            ],
        ),
        migrations.CreateModel(
            name='spare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_photo', models.CharField(max_length=10)),
                ('spare_code', models.IntegerField()),
                ('spare_brand', models.CharField(max_length=15)),
                ('spare_name', models.CharField(max_length=20)),
                ('car_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Auto', to='Repuestosapp.car')),
                ('engine_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Engine', to='Repuestosapp.engine')),
            ],
        ),
        migrations.AddField(
            model_name='engine',
            name='members',
            field=models.ManyToManyField(through='Repuestosapp.spare', to='Repuestosapp.car'),
        ),
    ]
