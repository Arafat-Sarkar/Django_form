# Generated by Django 4.2.7 on 2023-12-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
    ]
