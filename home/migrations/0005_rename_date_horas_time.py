# Generated by Django 5.0.7 on 2024-07-22 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_days_horas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horas',
            old_name='date',
            new_name='time',
        ),
    ]
