# Generated by Django 5.0.7 on 2024-07-19 15:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_monitorias_username'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitorias',
            old_name='username',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='monitorias',
            unique_together={('date', 'owner')},
        ),
    ]
