# Generated by Django 5.0.1 on 2024-02-18 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_managermodel_alter_defendersmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='managermodel',
            options={'verbose_name': 'manage', 'verbose_name_plural': 'manager'},
        ),
    ]
