# Generated by Django 3.0.3 on 2020-02-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.CharField(max_length=19)),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
                ('role', models.CharField(max_length=15)),
                ('charge', models.CharField(max_length=30)),
                ('notes', models.CharField(max_length=50)),
            ],
        ),
    ]