# Generated by Django 3.2.15 on 2022-09-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=50)),
                ('userEmail', models.CharField(max_length=255)),
            ],
        ),
    ]
