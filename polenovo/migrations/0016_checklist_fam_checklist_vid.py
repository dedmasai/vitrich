# Generated by Django 4.1 on 2024-09-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polenovo', '0015_remove_checklist_suc_checklist_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='fam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checklist',
            name='vid',
            field=models.BooleanField(default=False),
        ),
    ]
