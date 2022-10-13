# Generated by Django 4.1.2 on 2022-10-13 18:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('date_published', models.DateField(default=datetime.date(2000, 1, 1))),
                ('language', models.CharField(choices=[('EN', 'English'), ('SP', 'Spanish'), ('FR', 'French'), ('JP', 'Japanese'), ('CH', 'Chinese')], default='English', max_length=10)),
                ('num_pages', models.IntegerField(default=0)),
                ('checked_out', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
