# Generated by Django 3.2 on 2021-08-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projet', '0002_auto_20210802_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
