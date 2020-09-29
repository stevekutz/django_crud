# Generated by Django 3.1.1 on 2020-09-29 03:16

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('kinds', models.CharField(choices=[('random', 'RANDOM'), ('important', 'IMPORTANT'), ('misc', 'MISC')], default='misc', max_length=50)),
            ],
        ),
    ]
