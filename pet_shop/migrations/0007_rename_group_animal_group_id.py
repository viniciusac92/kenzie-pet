# Generated by Django 3.2.5 on 2021-07-28 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shop', '0006_animal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='group',
            new_name='group_id',
        ),
    ]
