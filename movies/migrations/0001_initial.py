# Generated by Django 4.2.4 on 2023-09-06 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
                ('released_at', models.DateField()),
                ('downloads', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('poster', models.CharField(max_length=100)),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.brand')),
                ('tags', models.ManyToManyField(to='movies.tag')),
            ],
        ),
    ]
