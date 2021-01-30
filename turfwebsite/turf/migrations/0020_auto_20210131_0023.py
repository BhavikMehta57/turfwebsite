# Generated by Django 3.1.5 on 2021-01-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0019_remove_turf_list_price_per_hour_5v5'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf_list',
            name='price_per_hour_5v5_weekdays',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='turf_list',
            name='price_per_hour_5v5_weekends',
            field=models.IntegerField(default=700),
        ),
        migrations.AddField(
            model_name='turf_list',
            name='weekdays_turf_closing_time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='turf_list',
            name='weekdays_turf_opening_time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='turf_list',
            name='weekends_turf_closing_time',
            field=models.TimeField(default='00:00'),
        ),
    ]
