# Generated by Django 3.2 on 2021-05-31 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverName', models.CharField(max_length=100)),
                ('vehicleName', models.CharField(max_length=100)),
                ('vehicleRegNo', models.CharField(max_length=10)),
                ('contact', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q2.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='TravelStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eta', models.TimeField()),
                ('fare', models.PositiveIntegerField()),
                ('userLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q2.userlocation')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='q2.vehicleinfo')),
            ],
        ),
    ]
