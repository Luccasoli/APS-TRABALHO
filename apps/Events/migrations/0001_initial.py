# Generated by Django 2.2.5 on 2019-10-03 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConcentrationArea',
            fields=[
                ('concentration_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'concentration areas',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('startDate', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('concentration_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.ConcentrationArea')),
                ('keywords', models.ManyToManyField(to='Events.Keyword')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]