# Generated by Django 4.1 on 2024-09-08 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polenovo', '0003_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='is_published',
        ),
    ]
