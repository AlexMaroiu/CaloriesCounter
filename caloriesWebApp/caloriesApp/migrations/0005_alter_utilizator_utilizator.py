# Generated by Django 4.0 on 2021-12-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('caloriesApp', '0004_utilizator_alter_mancat_utilizator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizator',
            name='utilizator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
