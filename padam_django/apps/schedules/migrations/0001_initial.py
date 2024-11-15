# Generated by Django 3.2.5 on 2024-11-10 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleet', '0002_auto_20211109_1456'),
        ('geography', '0002_busstop'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.bus')),
                ('bus_stops', models.ManyToManyField(to='geography.BusStop')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.driver')),
            ],
            options={
                'unique_together': {('bus', 'driver', 'start_time')},
            },
        ),
    ]
