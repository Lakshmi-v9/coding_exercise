# Generated by Django 4.1.1 on 2022-12-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='id',
        ),
        migrations.RemoveField(
            model_name='weatherstats',
            name='id',
        ),
        migrations.AlterField(
            model_name='weather',
            name='station_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weatherstats',
            name='station_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
