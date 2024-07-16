# Generated by Django 5.0.1 on 2024-02-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_matchmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('score', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'bombardir',
                'verbose_name_plural': 'bombardirs',
            },
        ),
    ]
