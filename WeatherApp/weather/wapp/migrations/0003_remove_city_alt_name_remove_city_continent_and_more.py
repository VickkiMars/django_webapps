# Generated by Django 4.0.6 on 2022-08-16 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wapp', '0002_alter_city_options_city_country_code_city_humidity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='alt_name',
        ),
        migrations.RemoveField(
            model_name='city',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='city',
            name='currency_code',
        ),
        migrations.RemoveField(
            model_name='city',
            name='dialing_code',
        ),
        migrations.RemoveField(
            model_name='city',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='city',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='city',
            name='pressure',
        ),
        migrations.RemoveField(
            model_name='city',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='city',
            name='timezone',
        ),
    ]
