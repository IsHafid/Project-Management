# Generated by Django 3.2 on 2021-07-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usersbase_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersbase',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
