# Generated by Django 4.1 on 2022-08-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('con', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_cls',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('son', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 't_student',
            },
        ),
    ]
