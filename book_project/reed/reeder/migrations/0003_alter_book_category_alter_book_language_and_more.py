# Generated by Django 4.0.5 on 2022-10-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reeder', '0002_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='press',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='book',
            name='uploaded_by',
            field=models.CharField(max_length=100),
        ),
    ]
