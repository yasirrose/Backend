# Generated by Django 4.2.4 on 2023-09-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
