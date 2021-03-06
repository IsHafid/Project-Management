# Generated by Django 3.2 on 2021-07-26 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usersbase_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.AlterField(
            model_name='usersbase',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='usersbase',
            name='statut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userstatut', to='users.statut'),
        ),
    ]
