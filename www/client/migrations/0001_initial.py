# Generated by Django 3.0.3 on 2020-02-28 04:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('document_id', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
            ],
        ),
    ]
