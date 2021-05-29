# Generated by Django 3.2 on 2021-04-24 14:31

from django.db import migrations, models
import main_gusto.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to=main_gusto.models.Banner.get_file_name_banners)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to=main_gusto.models.Event.get_file_name_events)),
                ('description', models.TextField(null=True)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
