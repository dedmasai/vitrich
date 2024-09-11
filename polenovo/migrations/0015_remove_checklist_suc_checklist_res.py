# Generated by Django 4.1 on 2024-09-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polenovo', '0014_remove_checklist_fam_remove_checklist_vid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='suc',
        ),
        migrations.AddField(
            model_name='checklist',
            name='res',
            field=models.CharField(choices=[(0, 'Не определен'), (1, 'До семейства'), (2, 'До вида')], default=None, max_length=90),
        ),
    ]
