# Generated by Django 4.0 on 2021-12-12 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caloriesApp', '0010_remove_mancat_created_at_remove_mancat_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mancat',
            old_name='utilizator',
            new_name='username',
        ),
    ]
